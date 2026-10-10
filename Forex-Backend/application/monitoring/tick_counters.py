"""
Tick Pipeline Counters — Phase 0 measurement.

A single process-wide singleton of per-symbol, per-stage counters.
All increments use plain int arithmetic (CPython GIL protects them;
no threading.Lock needed for single-writer-per-stage use).

NO per-tick logging. Expose via GET /api/v1/admin/metrics/ticks.

Counters
--------
received        ticks seen by TickIngestor before engine
stale_dropped   ticks rejected by engine staleness filter
noise_dropped   ticks rejected by engine noise filter
accepted        ticks that passed all engine filters
published       ticks after event_bus.publish() returned
margin_pipeline ticks entering TickMarginPipeline._process_tick_now
sltp_worker     ticks entering SlTpWorker.process_tick
bar_aggregator  ticks entering BarAggregator.process_tick (any TF)
tick_history    ticks flushed to tick_history table (batched)

Conservation invariant (checked every TICK_CONSERVATION_CHECK_SECONDS):
    accepted == margin_pipeline  (unexplained drop → WARNING)
    accepted == sltp_worker      (unexplained drop → WARNING)
"""
from __future__ import annotations

import asyncio
import logging
import os
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict

logger = logging.getLogger(__name__)

_CHECK_INTERVAL: float = float(os.environ.get("TICK_CONSERVATION_CHECK_SECONDS", "30"))


@dataclass
class _SymbolCounters:
    received: int = 0
    stale_dropped: int = 0
    noise_dropped: int = 0
    accepted: int = 0
    published: int = 0
    margin_pipeline: int = 0
    margin_coalesced_dropped: int = 0
    sltp_worker: int = 0
    bar_aggregator: int = 0
    tick_history: int = 0

    def to_dict(self) -> dict:
        unexplained_margin = self.accepted - (self.margin_pipeline + self.margin_coalesced_dropped)
        unexplained_sltp = self.accepted - self.sltp_worker
        return {
            "received": self.received,
            "stale_dropped": self.stale_dropped,
            "noise_dropped": self.noise_dropped,
            "accepted": self.accepted,
            "published": self.published,
            "margin_pipeline": self.margin_pipeline,
            "margin_coalesced_dropped": self.margin_coalesced_dropped,
            "sltp_worker": self.sltp_worker,
            "bar_aggregator": self.bar_aggregator,
            "tick_history": self.tick_history,
            "conservation_ok": (unexplained_margin == 0 and unexplained_sltp == 0),
            "unexplained_margin_drop": unexplained_margin,
            "unexplained_sltp_drop": unexplained_sltp,
        }


class TickCounters:
    """Process-wide per-symbol tick counter store."""

    def __init__(self) -> None:
        self._symbols: Dict[str, _SymbolCounters] = defaultdict(_SymbolCounters)
        self._conservation_task: asyncio.Task | None = None

    def _get(self, symbol: str) -> _SymbolCounters:
        return self._symbols[symbol]

    # ── increment helpers (called from hot path, must be non-blocking) ──

    def inc_received(self, symbol: str) -> None:
        self._symbols[symbol].received += 1

    def inc_stale_dropped(self, symbol: str) -> None:
        self._symbols[symbol].stale_dropped += 1

    def inc_noise_dropped(self, symbol: str) -> None:
        self._symbols[symbol].noise_dropped += 1

    def inc_accepted(self, symbol: str) -> None:
        self._symbols[symbol].accepted += 1

    def inc_published(self, symbol: str) -> None:
        self._symbols[symbol].published += 1

    def inc_margin_pipeline(self, symbol: str) -> None:
        self._symbols[symbol].margin_pipeline += 1

    def inc_margin_coalesced_dropped(self, symbol: str) -> None:
        self._symbols[symbol].margin_coalesced_dropped += 1

    def inc_sltp_worker(self, symbol: str) -> None:
        self._symbols[symbol].sltp_worker += 1

    def inc_bar_aggregator(self, symbol: str) -> None:
        self._symbols[symbol].bar_aggregator += 1

    def inc_tick_history(self, symbol: str, n: int = 1) -> None:
        self._symbols[symbol].tick_history += n

    # ── read ────────────────────────────────────────────────────────────

    def snapshot(self) -> Dict[str, dict]:
        """Return a serialisable snapshot of all symbol counters."""
        return {sym: c.to_dict() for sym, c in sorted(self._symbols.items())}

    def reset(self) -> None:
        """Reset all counters (for testing)."""
        self._symbols.clear()

    # ── background conservation check ───────────────────────────────────

    def start_conservation_check(self) -> None:
        """Start the periodic conservation-check task (call once at startup)."""
        if self._conservation_task is None or self._conservation_task.done():
            self._conservation_task = asyncio.create_task(
                self._run_conservation_loop(), name="tick_conservation_check"
            )

    def stop_conservation_check(self) -> None:
        if self._conservation_task and not self._conservation_task.done():
            self._conservation_task.cancel()

    async def _run_conservation_loop(self) -> None:
        while True:
            try:
                await asyncio.sleep(_CHECK_INTERVAL)
                self._check_conservation()
            except asyncio.CancelledError:
                break
            except Exception:  # noqa: BLE001
                logger.exception("tick conservation check raised unexpectedly")

    def _check_conservation(self) -> None:
        for sym, c in self._symbols.items():
            if c.accepted == 0:
                continue
            margin_drop = c.accepted - (c.margin_pipeline + c.margin_coalesced_dropped)
            sltp_drop = c.accepted - c.sltp_worker
            if margin_drop != 0:
                logger.warning(
                    "TICK CONSERVATION: %s accepted=%d margin_pipeline=%d "
                    "coalesced=%d unexplained_drop=%d",
                    sym, c.accepted, c.margin_pipeline, c.margin_coalesced_dropped, margin_drop,
                )
            if sltp_drop != 0:
                logger.warning(
                    "TICK CONSERVATION: %s accepted=%d sltp_worker=%d "
                    "unexplained_drop=%d",
                    sym, c.accepted, c.sltp_worker, sltp_drop,
                )


# ── process-wide singleton ───────────────────────────────────────────────────

TICK_COUNTERS: TickCounters = TickCounters()
