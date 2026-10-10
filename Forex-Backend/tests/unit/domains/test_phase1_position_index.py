"""
Phase 1 Unit Tests: In-Memory PositionIndex & Decoupled SL/TP Execution.

Verifies:
1. Correctness of bisect binary search for BUY/SELL SL/TP triggers vs linear scan.
2. In-memory PositionIndex O(log M + K) scalability.
3. Fail-closed fallback: when index is not ready or desynced, falls back to DB with ERROR log.
4. Reconciliation detection of missing/stale positions.
5. Decoupled async queue execution in SlTpWorker with in-flight deduplication.
"""
from __future__ import annotations

import asyncio
from decimal import Decimal
import logging
import time
from typing import List, Optional

import pytest

from core.domains.common.value_objects import Price, Volume
from core.domains.oms.entities.position import Position
from core.domains.oms.enums import PositionAction
from core.domains.oms.position_index import PositionIndex
from application.workers.sltp_worker import SlTpWorker
from infrastructure.messaging.inprocess_event_bus import InProcessEventBus


def make_position(
    pid: str,
    symbol: str,
    action: PositionAction,
    sl: Optional[str] = None,
    tp: Optional[str] = None,
    account_login: int = 10001,
) -> Position:
    return Position(
        position_id=pid,
        account_login=account_login,
        symbol=symbol,
        action=action,
        volume=Volume(Decimal("1.0")),
        price_open=Price(Decimal("1.10000")),
        price_sl=Price(Decimal(sl)) if sl else None,
        price_tp=Price(Decimal(tp)) if tp else None,
        contract_size=Decimal("100000"),
    )


def test_bisect_matches_linear_scan_all_scenarios():
    """Assert bisect binary search matches linear scan across all 4 SL/TP trigger conditions."""
    index = PositionIndex()
    positions: List[Position] = [
        # Buy SL triggers on Bid <= SL (SL >= Bid)
        make_position("B_SL_1", "EURUSD", PositionAction.BUY, sl="1.0950"),
        make_position("B_SL_2", "EURUSD", PositionAction.BUY, sl="1.0900"),
        make_position("B_SL_3", "EURUSD", PositionAction.BUY, sl="1.0850"),
        # Buy TP triggers on Bid >= TP (TP <= Bid)
        make_position("B_TP_1", "EURUSD", PositionAction.BUY, tp="1.1050"),
        make_position("B_TP_2", "EURUSD", PositionAction.BUY, tp="1.1100"),
        # Sell SL triggers on Ask >= SL (SL <= Ask)
        make_position("S_SL_1", "EURUSD", PositionAction.SELL, sl="1.1050"),
        make_position("S_SL_2", "EURUSD", PositionAction.SELL, sl="1.1100"),
        # Sell TP triggers on Ask <= TP (TP >= Ask)
        make_position("S_TP_1", "EURUSD", PositionAction.SELL, tp="1.0950"),
        make_position("S_TP_2", "EURUSD", PositionAction.SELL, tp="1.0900"),
    ]
    index.rebuild(positions)

    def linear_scan(bid: Decimal, ask: Decimal):
        trig = []
        for p in positions:
            sl = p.price_sl.value if p.price_sl else None
            tp = p.price_tp.value if p.price_tp else None
            if p.action == PositionAction.BUY:
                if sl is not None and bid <= sl:
                    trig.append((p.position_id, "SL"))
                elif tp is not None and bid >= tp:
                    trig.append((p.position_id, "TP"))
            else:
                if sl is not None and ask >= sl:
                    trig.append((p.position_id, "SL"))
                elif tp is not None and ask <= tp:
                    trig.append((p.position_id, "TP"))
        return set(trig)

    test_ticks = [
        (Decimal("1.1000"), Decimal("1.1002")),  # Mid market: no triggers
        (Decimal("1.0920"), Decimal("1.0922")),  # Bid drops below 1.0950 (B_SL_1 triggers; S_TP_1 triggers on ask 1.0922 <= 1.0950)
        (Decimal("1.0840"), Decimal("1.0842")),  # Deep drop: B_SL_1, B_SL_2, B_SL_3, S_TP_1, S_TP_2 trigger
        (Decimal("1.1060"), Decimal("1.1062")),  # Rise: B_TP_1, S_SL_1 trigger
        (Decimal("1.1120"), Decimal("1.1122")),  # Deep rise: B_TP_1, B_TP_2, S_SL_1, S_SL_2 trigger
    ]

    for bid, ask in test_ticks:
        expected = linear_scan(bid, ask)
        result = index.find_triggered("EURUSD", bid, ask)
        actual = {(p.position_id, reason) for p, reason, _ in result}
        assert actual == expected, f"Mismatch at bid={bid}, ask={ask}: actual={actual}, expected={expected}"


def test_position_index_speed_benchmark():
    """Verify O(log M + K) bisect execution on 5,000 positions.
    Normal tick with 0 triggers must execute in microseconds (< 50us).
    """
    index = PositionIndex()
    positions: List[Position] = []

    # 2500 Buys with SL 1.0100 to 1.0350, TP 1.1600 to 1.1850
    for i in range(2500):
        sl = f"1.{100 + (i % 250):04d}"
        tp = f"1.{1600 + (i % 250):04d}"
        positions.append(make_position(f"B_{i}", "EURUSD", PositionAction.BUY, sl=sl, tp=tp))

    # 2500 Sells with SL 1.1600 to 1.1850, TP 1.0100 to 1.0350
    for i in range(2500):
        sl = f"1.{1600 + (i % 250):04d}"
        tp = f"1.{100 + (i % 250):04d}"
        positions.append(make_position(f"S_{i}", "EURUSD", PositionAction.SELL, sl=sl, tp=tp))

    index.rebuild(positions)

    # Mid market tick at 1.1000 (well between 1.0350 and 1.1600): 0 triggered
    bid = Decimal("1.1000")
    ask = Decimal("1.1002")

    t0 = time.perf_counter()
    for _ in range(5000):
        _ = index.find_triggered("EURUSD", bid, ask)
    elapsed = time.perf_counter() - t0

    avg_micros = (elapsed / 5000) * 1_000_000
    assert avg_micros < 50, f"Average index lookup with 0 triggers took {avg_micros:.1f}us, expected < 50us"


def test_reconciliation_detects_mismatch(caplog):
    """Reconciliation logs ERROR and marks index unverified if DB desynced."""
    index = PositionIndex()
    p1 = make_position("P1", "EURUSD", PositionAction.BUY, sl="1.0900")
    p2 = make_position("P2", "EURUSD", PositionAction.BUY, sl="1.0850")
    index.rebuild([p1, p2])

    assert index.reconcile_with_db([p1, p2]) is True

    # DB has p3 that memory missed
    p3 = make_position("P3", "EURUSD", PositionAction.SELL, sl="1.1100")
    with caplog.at_level(logging.ERROR):
        ok = index.reconcile_with_db([p1, p2, p3])
    assert ok is False
    assert "POSITION INDEX RECONCILIATION MISMATCH" in caplog.text


@pytest.mark.asyncio
async def test_sltp_worker_fallback_when_index_not_ready(caplog):
    """If PositionIndex is not ready, SlTpWorker logs ERROR and falls back to position_repo."""
    class MockRepo:
        def __init__(self):
            self.queried = False
            self.pos = make_position("P_FALLBACK", "EURUSD", PositionAction.BUY, sl="1.0950")

        async def get_by_symbol(self, symbol: str):
            self.queried = True
            return [self.pos]

    class MockCloseHandler:
        def __init__(self):
            self.closed = []

        async def handle(self, cmd):
            self.closed.append(cmd)

    repo = MockRepo()
    close_handler = MockCloseHandler()
    index = PositionIndex()
    # deliberately do NOT call index.rebuild() -> index.is_ready is False

    worker = SlTpWorker(
        position_repo=repo,
        close_position_handler=close_handler,
        event_bus=InProcessEventBus(),
        position_index=index,
    )
    await worker.start()

    with caplog.at_level(logging.ERROR):
        # Tick at 1.0900 triggers Buy SL at 1.0950
        count = await worker.process_tick("EURUSD", Decimal("1.0900"), Decimal("1.0902"))

    assert repo.queried is True, "SlTpWorker must query DB when index is not ready"
    assert "PositionIndex is not ready; falling back to DB" in caplog.text
    assert count == 1

    await worker.flush()
    assert len(close_handler.closed) == 1
    assert close_handler.closed[0].position_id == "P_FALLBACK"

    await worker.stop()


@pytest.mark.asyncio
async def test_sltp_worker_decoupled_execution_and_inflight_dedup():
    """Verify tick path enqueues closes without waiting and deduplicates duplicate triggers."""
    executed_events = []

    class MockCloseHandler:
        async def handle(self, cmd):
            await asyncio.sleep(0.01)  # Simulate network / DB delay
            executed_events.append(cmd.position_id)

    class MockRepo:
        async def get_by_symbol(self, symbol: str):
            return []

    p = make_position("P_HOT", "EURUSD", PositionAction.BUY, sl="1.0950")
    index = PositionIndex()
    index.rebuild([p])

    worker = SlTpWorker(
        position_repo=MockRepo(),
        close_position_handler=MockCloseHandler(),
        event_bus=InProcessEventBus(),
        position_index=index,
    )
    await worker.start()

    # First tick triggers P_HOT
    t0 = time.perf_counter()
    enqueued1 = await worker.process_tick("EURUSD", Decimal("1.0900"), Decimal("1.0902"))
    tick_time = time.perf_counter() - t0

    # Tick path returns immediately (does NOT await the 10ms sleep in close handler)
    assert tick_time < 0.005, f"Tick path blocked for {tick_time*1000:.2f}ms; execution must be decoupled!"
    assert enqueued1 == 1

    # Second tick immediately arrives while close is in-flight: deduplication must drop it
    enqueued2 = await worker.process_tick("EURUSD", Decimal("1.0890"), Decimal("1.0892"))
    assert enqueued2 == 0, "Duplicate trigger while in-flight must not be enqueued twice"

    await worker.flush()
    assert executed_events == ["P_HOT"]

    await worker.stop()
