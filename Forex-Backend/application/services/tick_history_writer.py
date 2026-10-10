"""
Tick History Writer — Phase 0 measurement only.

Subscribes to TICK_RECEIVED.  The handler is SYNCHRONOUS (no await, no
blocking) - it puts the tick into a bounded deque and returns immediately,
adding zero latency to the serial tick path.

A background asyncio.Task flushes the deque to Postgres every
TICK_HISTORY_FLUSH_SECONDS (default 2.0 s) using a bulk INSERT, then
prunes rows older than 24 h.  Fills, closes, and other money events are
NOT affected: this writer only appends market quotes.

Design constraints (from PROMPT):
- MUST NOT await in the event handler (zero tick-path latency added).
- Buffer is bounded (TICK_HISTORY_MAX_BUFFER, default 10 000).
  Overflow drops OLDEST entries with a counter increment, never OOM.
- Auto-prune to 24 h on every flush (temporary until permanent store decided).
- inc_tick_history counter incremented per flushed tick.
"""
from __future__ import annotations

import asyncio
import logging
import os
from collections import deque
from datetime import datetime, timedelta, timezone
from typing import Any, Deque, Optional

from application.monitoring.tick_counters import TICK_COUNTERS
from core.events.domain_events import EventType

logger = logging.getLogger(__name__)

_FLUSH_SECONDS: float = float(os.environ.get("TICK_HISTORY_FLUSH_SECONDS", "2.0"))
_MAX_BUFFER: int = int(os.environ.get("TICK_HISTORY_MAX_BUFFER", "10000"))
_RETAIN_HOURS: int = int(os.environ.get("TICK_HISTORY_RETAIN_HOURS", "24"))


class TickHistoryWriter:
    """Buffered, non-blocking writer for the tick_history table.

    Parameters
    ----------
    session_factory:
        async_sessionmaker from DatabaseManager.  Passed at construction so
        the writer does not need to import the database module (DI boundary).
    event_bus:
        IEventBus instance.  Used to subscribe to TICK_RECEIVED.
    """

    def __init__(self, session_factory: Any, event_bus: Any) -> None:
        self._session_factory = session_factory
        self._event_bus = event_bus
        self._buffer: Deque[dict] = deque(maxlen=_MAX_BUFFER)
        self._overflow_dropped: int = 0
        self._flush_task: Optional[asyncio.Task] = None
        self._running = False
        self._subscribed = False

    # ── lifecycle ────────────────────────────────────────────────────────

    async def start(self) -> None:
        """Subscribe to tick events and start the flush loop."""
        self._running = True
        if not self._subscribed:
            self._event_bus.subscribe(EventType.TICK_RECEIVED, self._on_tick_event)
            self._subscribed = True
        self._flush_task = asyncio.create_task(
            self._flush_loop(), name="tick_history_flush"
        )
        logger.info(
            "TickHistoryWriter started (flush every %.1fs, buffer %d, retain %dh)",
            _FLUSH_SECONDS, _MAX_BUFFER, _RETAIN_HOURS,
        )

    async def stop(self) -> None:
        """Flush remaining buffer and stop."""
        self._running = False
        if self._subscribed:
            try:
                self._event_bus.unsubscribe(EventType.TICK_RECEIVED, self._on_tick_event)
            except Exception:  # noqa: BLE001
                pass
            self._subscribed = False
        if self._flush_task and not self._flush_task.done():
            self._flush_task.cancel()
        # Final drain
        if self._buffer:
            await self._flush_buffer()
        logger.info("TickHistoryWriter stopped")

    # ── event handler — MUST be synchronous and non-blocking ─────────────

    def _on_tick_event(self, event: Any) -> None:
        """Called synchronously by the event bus for every TICK_RECEIVED.

        This method MUST NOT await anything.  It puts one dict into the
        bounded deque and returns immediately so the serial tick path
        (engine.py L208 await event_bus.publish) is not delayed.

        maxlen on the deque means the oldest entry is silently dropped by
        Python when the buffer is full.  We track that separately.
        """
        payload = getattr(event, "payload", None)
        if payload is None:
            return
        symbol = payload.get("symbol")
        if not symbol:
            return
        # If buffer is at capacity, deque.append silently drops the leftmost
        # entry.  Detect overflow by checking length before append.
        was_full = len(self._buffer) >= _MAX_BUFFER
        self._buffer.append({
            "symbol": symbol,
            "bid": payload.get("bid"),
            "ask": payload.get("ask"),
            "spread": payload.get("spread"),
            "source": payload.get("source"),
            "timestamp": payload.get("timestamp"),
        })
        if was_full:
            self._overflow_dropped += 1
            if self._overflow_dropped == 1 or self._overflow_dropped % 500 == 0:
                logger.warning(
                    "TickHistoryWriter buffer full (%d): %d oldest ticks dropped total. "
                    "Raise TICK_HISTORY_MAX_BUFFER or reduce TICK_HISTORY_FLUSH_SECONDS.",
                    _MAX_BUFFER, self._overflow_dropped,
                )

    # ── flush loop ───────────────────────────────────────────────────────

    async def _flush_loop(self) -> None:
        while self._running:
            try:
                await asyncio.sleep(_FLUSH_SECONDS)
                await self._flush_buffer()
            except asyncio.CancelledError:
                break
            except Exception:  # noqa: BLE001
                logger.exception("TickHistoryWriter flush iteration failed")

    async def _flush_buffer(self) -> None:
        """Drain the in-memory buffer into the database."""
        if not self._buffer:
            return

        # Atomically drain current buffer so new ticks can accumulate
        # while we await the DB write.
        rows = []
        while self._buffer:
            rows.append(self._buffer.popleft())

        if not rows:
            return

        try:
            await self._insert_and_prune(rows)
            # Credit the counter per-symbol
            by_symbol: dict[str, int] = {}
            for r in rows:
                sym = r.get("symbol", "")
                by_symbol[sym] = by_symbol.get(sym, 0) + 1
            for sym, count in by_symbol.items():
                TICK_COUNTERS.inc_tick_history(sym, count)
        except Exception as exc:  # noqa: BLE001
            logger.error(
                "TickHistoryWriter: failed to flush %d rows: %s — "
                "rows are dropped (buffer already drained).",
                len(rows), exc,
            )

    async def _insert_and_prune(self, rows: list) -> None:
        """Bulk INSERT rows then DELETE older than retain window."""
        from sqlalchemy import text

        cutoff: datetime = datetime.now(timezone.utc) - timedelta(hours=_RETAIN_HOURS)

        async with self._session_factory() as session:
            async with session.begin():
                # Bulk insert using core INSERT for speed (no ORM overhead).
                from infrastructure.persistence.tick_history_models import TickHistoryModel

                parsed_rows = []
                for r in rows:
                    ts_raw = r.get("timestamp")
                    if ts_raw is None:
                        continue
                    if isinstance(ts_raw, str):
                        try:
                            ts = datetime.fromisoformat(ts_raw)
                        except ValueError:
                            continue
                    elif isinstance(ts_raw, datetime):
                        ts = ts_raw
                    else:
                        continue
                    if ts.tzinfo is None:
                        ts = ts.replace(tzinfo=timezone.utc)

                    def _decimal_or_none(v: Any) -> Any:
                        if v is None:
                            return None
                        from decimal import Decimal
                        try:
                            return Decimal(str(v))
                        except Exception:  # noqa: BLE001
                            return None

                    parsed_rows.append({
                        "symbol": r["symbol"],
                        "bid": _decimal_or_none(r.get("bid")),
                        "ask": _decimal_or_none(r.get("ask")),
                        "spread": _decimal_or_none(r.get("spread")),
                        "source": r.get("source"),
                        "timestamp": ts,
                    })

                if parsed_rows:
                    # Phase 3: Fast binary COPY via asyncpg when connected to PostgreSQL
                    copied_fast = False
                    try:
                        conn = await session.connection()
                        raw_conn = await conn.get_raw_connection()
                        driver_conn = getattr(raw_conn, "driver_connection", None)
                        if driver_conn and hasattr(driver_conn, "copy_records_to_table"):
                            records = [
                                (
                                    r["symbol"],
                                    r["bid"],
                                    r["ask"],
                                    r["spread"],
                                    r["source"],
                                    r["timestamp"],
                                )
                                for r in parsed_rows
                            ]
                            await driver_conn.copy_records_to_table(
                                "tick_history",
                                records=records,
                                columns=["symbol", "bid", "ask", "spread", "source", "timestamp"],
                            )
                            copied_fast = True
                    except Exception as e:
                        logger.debug("asyncpg copy_records_to_table fallback to bulk insert: %s", e)

                    if not copied_fast:
                        await session.execute(
                            TickHistoryModel.__table__.insert(),
                            parsed_rows,
                        )

                # Prune rows outside the retention window.
                await session.execute(
                    text(
                        "DELETE FROM tick_history WHERE timestamp < :cutoff"
                    ),
                    {"cutoff": cutoff},
                )
