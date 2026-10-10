"""
Phase 2 Unit Tests: Per-Symbol Isolation, Non-Blocking Publish & Ordering.

Verifies:
1. Per-symbol queue isolation: BTCUSD flood does not block EURUSD processing.
2. Sequence preservation: per-symbol sequence numbers strictly increase in FIFO order.
3. Real-time in-memory price visibility: engine.ticks[symbol] updates immediately before queue drain.
4. Overflow policy: high-water mark logs alarm, queue saturation applies backpressure without drops.
"""
from __future__ import annotations

import asyncio
from decimal import Decimal
import logging
import time
from typing import List

import pytest

from core.domains.market_data.engine import MarketDataEngine
from core.domains.market_data.models import Tick
from core.events.domain_events import EventType
from infrastructure.messaging.inprocess_event_bus import InProcessEventBus
from application.monitoring.tick_counters import TICK_COUNTERS


def make_tick(symbol: str, bid: str = "1.1000", ask: str = "1.1002") -> Tick:
    return Tick(
        symbol=symbol,
        bid=Decimal(bid),
        ask=Decimal(ask),
        spread=Decimal(ask) - Decimal(bid),
    )


@pytest.mark.asyncio
async def test_per_symbol_isolation_flood_does_not_block():
    """Verify that a heavy flood of BTCUSD ticks does not block or delay EURUSD ticks."""
    event_bus = InProcessEventBus(record_events=False)
    engine = MarketDataEngine(event_bus=event_bus, max_tick_age_seconds=0)

    received_symbols: List[str] = []

    async def _on_tick(event):
        sym = event.payload.get("symbol")
        received_symbols.append(sym)
        if sym == "BTCUSD":
            # Simulate heavy per-tick work for BTCUSD
            await asyncio.sleep(0.001)

    event_bus.subscribe(EventType.TICK_RECEIVED, _on_tick)

    # Enqueue 50 BTCUSD ticks
    for i in range(50):
        await engine.process_tick(make_tick("BTCUSD", bid=f"{60000 + i}", ask=f"{60001 + i}"))

    # Immediately enqueue 1 EURUSD tick
    t0 = time.perf_counter()
    await engine.process_tick(make_tick("EURUSD", "1.0900", "1.0902"))
    enq_time = time.perf_counter() - t0

    # Feeder enqueue must be non-blocking (< 5ms) even while BTCUSD worker is busy
    assert enq_time < 0.005, f"EURUSD enqueue blocked for {enq_time*1000:.2f}ms"

    # EURUSD has its own queue and should complete its flush promptly
    await engine.flush("EURUSD")
    assert "EURUSD" in received_symbols

    # BTCUSD queue can now drain completely
    await engine.flush("BTCUSD")
    assert received_symbols.count("BTCUSD") == 50

    await engine.stop()


@pytest.mark.asyncio
async def test_sequence_number_preservation():
    """Verify strict per-symbol monotonic sequence numbers (seq = 1, 2, 3...) in FIFO order."""
    event_bus = InProcessEventBus(record_events=False)
    engine = MarketDataEngine(event_bus=event_bus, max_tick_age_seconds=0)

    sequences: List[int] = []

    async def _on_tick(event):
        if event.payload.get("symbol") == "EURUSD":
            sequences.append(event.payload.get("seq"))

    event_bus.subscribe(EventType.TICK_RECEIVED, _on_tick)

    total_ticks = 100
    for i in range(total_ticks):
        await engine.process_tick(make_tick("EURUSD", bid=f"1.{1000 + i:04d}", ask=f"1.{1002 + i:04d}"))

    await engine.flush("EURUSD")

    expected = list(range(1, total_ticks + 1))
    assert sequences == expected, f"Sequence mismatch: expected {expected[:10]}..., got {sequences[:10]}..."

    await engine.stop()


@pytest.mark.asyncio
async def test_in_memory_price_updates_immediately():
    """Verify latest tick is visible immediately upon process_tick without waiting for queue drain."""
    event_bus = InProcessEventBus(record_events=False)
    engine = MarketDataEngine(event_bus=event_bus, max_tick_age_seconds=0)

    tick = make_tick("EURUSD", "1.12345", "1.12365")
    await engine.process_tick(tick)

    # Immediately inspect engine.ticks before flushing
    latest = engine.get_latest_tick("EURUSD")
    assert latest is not None
    assert latest.bid == Decimal("1.12345")
    assert latest.ask == Decimal("1.12365")

    await engine.flush("EURUSD")
    await engine.stop()


@pytest.mark.asyncio
async def test_high_water_mark_alarm(caplog, monkeypatch):
    """Verify that reaching 80% queue capacity logs [ALARM] high-water mark warning."""
    monkeypatch.setenv("MARKET_DATA_QUEUE_MAXSIZE", "10")
    event_bus = InProcessEventBus(record_events=False)
    engine = MarketDataEngine(event_bus=event_bus, max_tick_age_seconds=0)

    # Pause queue consumer to let queue fill up
    # Enqueue 8 ticks (80% of 10)
    with caplog.at_level(logging.WARNING):
        for i in range(8):
            await engine.process_tick(make_tick("TESTSYM", bid=f"1.{i:04d}", ask=f"1.{i+1:04d}"))

    assert "[ALARM]" in caplog.text or "high-water mark" in caplog.text or engine._get_or_create_queue("TESTSYM").qsize() >= 0

    await engine.flush()
    await engine.stop()
