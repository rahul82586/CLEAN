"""
Phase 0 Replay Harness — ops/replay_harness.py

Feeds synthetic ticks at configurable rates through the REAL pipeline
(MarketDataEngine + InProcessEventBus + real subscribers) wired to
lightweight in-memory repositories.  No PostgreSQL required.

Usage
-----
    python ops/replay_harness.py [options]

    --eurusd-rate N   ticks/s for EURUSD  (default: 10)
    --btcusd-rate N   ticks/s for BTCUSD  (default: 100)
    --duration  N     seconds to run       (default: 30)

Output
------
    Ticks/s in and out per consumer, p50/p99 end-to-end latency,
    conservation check result, final counter snapshot.

Notes
-----
- This harness proves Phase 0 counters work and gives a baseline.
- It does NOT test money paths (no fills, no closes).
- SlTpWorker and TickMarginPipeline are wired with stub repos that return
  [] immediately, so DB round-trips are absent.  This isolates the
  pipeline overhead.
"""
from __future__ import annotations

import argparse
import asyncio
import logging
import sys
import time
from collections import deque
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from statistics import median, quantiles
from typing import List

# Add project root to path so imports work without installation
sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(
    level=logging.WARNING,  # silence INFO from workers; harness prints its own
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("replay_harness")

# ─── Stub repositories (no DB) ───────────────────────────────────────────────

class _StubPositionRepo:
    async def get_by_symbol(self, symbol: str) -> list:
        return []

    async def get_by_account(self, login: int) -> list:
        return []


class _StubAccountRepo:
    async def find_by_login(self, login: int):
        return None


class _StubSymbolRepo:
    async def find_by_name(self, name: str):
        return None


# ─── Latency recorder (attached to event bus) ────────────────────────────────

class _LatencyRecorder:
    """Records e2e latency: time from tick received to publish returned."""

    def __init__(self) -> None:
        self.samples: deque[float] = deque(maxlen=100_000)  # us

    def record(self, start_ns: int) -> None:
        elapsed_us = (time.perf_counter_ns() - start_ns) / 1_000
        self.samples.append(elapsed_us)

    def report(self) -> dict:
        if not self.samples:
            return {"p50_us": None, "p99_us": None, "samples": 0}
        data = sorted(self.samples)
        n = len(data)
        p50 = data[n // 2]
        p99 = data[int(n * 0.99)]
        return {"p50_us": round(p50, 1), "p99_us": round(p99, 1), "samples": n}


# ─── Instrumented tick feed ───────────────────────────────────────────────────

class _SyntheticFeed:
    """Generates ticks at a fixed rate for a single symbol."""

    def __init__(self, symbol: str, rate_per_sec: float) -> None:
        self.symbol = symbol
        self._interval = 1.0 / rate_per_sec
        self._running = False
        self.name = f"synthetic_{symbol}"

    async def stream_ticks(self):
        from core.domains.market_data.models import Tick

        bid = Decimal("1.10000")
        spread = Decimal("0.00020")
        self._running = True
        while self._running:
            bid += Decimal("0.00001")
            ask = bid + spread
            tick = Tick(
                symbol=self.symbol,
                bid=bid,
                ask=ask,
                spread=spread,
                timestamp=datetime.now(timezone.utc),
                source="HARNESS",
            )
            yield tick
            await asyncio.sleep(self._interval)

    def stop(self) -> None:
        self._running = False


# ─── Main harness ─────────────────────────────────────────────────────────────

async def run(eurusd_rate: float, btcusd_rate: float, duration: float) -> None:
    from application.monitoring.tick_counters import TICK_COUNTERS
    from application.services.tick_ingestor import TickIngestor
    from application.workers.sltp_worker import SlTpWorker
    from core.domains.market_data.engine import MarketDataEngine
    from infrastructure.messaging.inprocess_event_bus import InProcessEventBus

    TICK_COUNTERS.reset()

    event_bus = InProcessEventBus(record_events=False)

    engine = MarketDataEngine(
        event_bus=event_bus,
        symbol_repo=None,
        redis_cache=None,
        bar_repository=None,
        max_tick_age_seconds=0,  # disable stale filter in harness
    )

    # Wire a stub SlTpWorker with PositionIndex (in-memory hot path)
    from core.domains.oms.position_index import PositionIndex
    pos_index = PositionIndex()
    pos_index.rebuild([])

    stub_pos_repo = _StubPositionRepo()

    class _NoopCloseHandler:
        async def handle(self, cmd): ...

    sltp = SlTpWorker(
        position_repo=stub_pos_repo,
        close_position_handler=_NoopCloseHandler(),
        event_bus=event_bus,
        position_index=pos_index,
    )
    await sltp.start()

    # Wire a stub TickMarginPipeline
    from application.services.tick_margin_pipeline import TickMarginPipeline
    from core.domains.risk.engine import RiskEngine

    class _StubRiskEngine:
        market_data_engine = engine
        def get_conversion_rate(self, *a, **kw): return Decimal("1")

    margin_pipeline = TickMarginPipeline(
        position_repo=stub_pos_repo,
        account_repo=_StubAccountRepo(),
        symbol_repo=_StubSymbolRepo(),
        risk_engine=_StubRiskEngine(),
        event_bus=event_bus,
        coalesce_seconds=0.0,
        position_index=pos_index,
    )
    from application.di.market_data_setup import on_tick_received
    from core.events.domain_events import EventType

    async def _on_margin_tick(event: Any) -> None:
        await on_tick_received(event, margin_pipeline)

    event_bus.subscribe(EventType.TICK_RECEIVED, _on_margin_tick)

    # Feeds
    eu_feed = _SyntheticFeed("EURUSD", eurusd_rate)
    btc_feed = _SyntheticFeed("BTCUSD", btcusd_rate)

    ingestor = TickIngestor(market_data_engine=engine, feeds=[eu_feed, btc_feed])

    latency = _LatencyRecorder()

    # Wrap process_tick to measure e2e latency
    _orig_process = engine.process_tick

    async def _timed_process(tick):
        t0 = time.perf_counter_ns()
        await _orig_process(tick)
        latency.record(t0)

    engine.process_tick = _timed_process  # type: ignore[method-assign]

    print(f"\n{'='*60}")
    print(f"  Replay Harness - Phase 0 Baseline")
    print(f"  EURUSD: {eurusd_rate}/s  BTCUSD: {btcusd_rate}/s  duration: {duration}s")
    print(f"{'='*60}\n")

    TICK_COUNTERS.reset()
    t_start = time.perf_counter()

    await ingestor.start()
    await asyncio.sleep(duration)

    eu_feed.stop()
    btc_feed.stop()
    await ingestor.stop()
    await engine.flush()
    await sltp.flush()

    elapsed = time.perf_counter() - t_start

    # ── Report ──────────────────────────────────────────────────────────
    snap = TICK_COUNTERS.snapshot()
    lat = latency.report()

    print(f"  Elapsed: {elapsed:.1f}s\n")
    print(f"  {'Symbol':<10} {'Rcvd':>7} {'Accepted':>9} {'Published':>10} "
          f"{'MarginPipe':>11} {'SltpWrk':>9} {'BarAgg':>8} {'Conservation':>14}")
    print(f"  {'-'*82}")

    total_rcvd = 0
    all_ok = True
    for sym, c in snap.items():
        ok = "[PASS]" if c["conservation_ok"] else "[FAIL]"
        if not c["conservation_ok"]:
            all_ok = False
        print(
            f"  {sym:<10} {c['received']:>7} {c['accepted']:>9} {c['published']:>10} "
            f"{c['margin_pipeline']:>11} {c['sltp_worker']:>9} {c['bar_aggregator']:>8} "
            f"{ok:>14}"
        )
        total_rcvd += c["received"]

    total_rate = total_rcvd / elapsed if elapsed > 0 else 0
    print(f"\n  Total ticks received: {total_rcvd}  ({total_rate:.1f}/s combined)")
    print(f"\n  Latency (tick received -> publish returned):")
    print(f"    p50 = {lat['p50_us']} us    p99 = {lat['p99_us']} us    "
          f"samples = {lat['samples']}")

    if not all_ok:
        print("\n  [!] Conservation check FAILED -- see unexplained_*_drop in counters:")
        for sym, c in snap.items():
            if not c["conservation_ok"]:
                print(f"    {sym}: {c}")
    else:
        print("\n  [OK] Conservation check PASSED -- no unexplained tick drops")

    print(f"\n{'='*60}\n")

    await sltp.stop()
    await engine.stop()


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 0 tick pipeline replay harness")
    parser.add_argument("--eurusd-rate", type=float, default=10.0,
                        help="EURUSD ticks/s (default: 10)")
    parser.add_argument("--btcusd-rate", type=float, default=100.0,
                        help="BTCUSD ticks/s (default: 100)")
    parser.add_argument("--duration", type=float, default=30.0,
                        help="Run duration in seconds (default: 30)")
    args = parser.parse_args()

    asyncio.run(run(
        eurusd_rate=args.eurusd_rate,
        btcusd_rate=args.btcusd_rate,
        duration=args.duration,
    ))


if __name__ == "__main__":
    main()
