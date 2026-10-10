"""Server-side SL/TP execution — the triggers MT5 runs on the trade server.

Phase 1 Optimization:
1. Uses in-memory PositionIndex with bisect binary search for O(log M + K)
   trigger detection. Zero PostgreSQL queries on the tick path.
2. Decoupled Close Execution: On a trigger, enqueues to a bounded asyncio.Queue.
   A separate background worker task consumes the queue and executes the LP
   HTTP call and DB transaction, completely removing network/DB wait from tick ingestion.
3. Fail-Closed Fallback: If PositionIndex is not ready or fails reconciliation,
   logs an ERROR and falls back to position_repo.get_by_symbol.
"""
from __future__ import annotations

import asyncio
import logging
import os
from decimal import Decimal
from typing import Any, List, Optional, Set, Tuple

import httpx
from application.commands.close_position import ClosePositionCommand
from application.monitoring.tick_counters import TICK_COUNTERS
from core.domains.market_data.feed_access import tick_ask, tick_bid, tick_from_event
from core.domains.oms.entities.position import Position
from core.domains.oms.enums import PositionAction
from core.domains.oms.position_index import GLOBAL_POSITION_INDEX, PositionIndex
from core.events.domain_events import EventType
from core.ports.interfaces import IEventBus, IPositionRepository

logger = logging.getLogger(__name__)


class SlTpWorker:
    """Fires SL/TP triggers off every tick for the ticked symbol."""

    def __init__(
        self,
        position_repo: IPositionRepository,
        close_position_handler: Any,
        event_bus: IEventBus,
        position_index: Optional[PositionIndex] = None,
        risk_service: Any = None,
        max_queue_size: int = 1000,
    ):
        self.position_repo = position_repo
        self.close_handler = close_position_handler
        self.event_bus = event_bus
        self.position_index = position_index
        self.risk_service = risk_service
        self._running = False
        self._subscribed = False
        self._in_flight: Set[str] = set()
        self._close_queue: asyncio.Queue = asyncio.Queue(maxsize=max_queue_size)
        self._close_worker_task: Optional[asyncio.Task] = None

    async def start(self) -> None:
        """Subscribe to the tick stream and start the decoupled close execution worker."""
        self._running = True
        if self.position_index and not self.position_index.is_ready:
            getter = getattr(self.position_repo, "get_open_positions", None)
            if getter is not None:
                try:
                    positions = await getter()
                    self.position_index.rebuild(positions)
                    logger.info("SlTpWorker initialized PositionIndex with %d positions", len(positions))
                except Exception as e:
                    logger.exception("Failed to build PositionIndex at SlTpWorker start: %s", e)
        if self._close_worker_task is None or self._close_worker_task.done():
            self._close_worker_task = asyncio.create_task(
                self._run_close_worker(), name="sltp_close_worker"
            )
        if not self._subscribed:
            self.event_bus.subscribe(EventType.TICK_RECEIVED, self.on_tick_event)
            self._subscribed = True
        logger.info("SlTpWorker started (server-side SL/TP armed, execution decoupled)")

    async def stop(self) -> None:
        self._running = False
        if self._close_worker_task and not self._close_worker_task.done():
            self._close_worker_task.cancel()
            try:
                await self._close_worker_task
            except asyncio.CancelledError:
                pass
        try:
            self.event_bus.unsubscribe(EventType.TICK_RECEIVED, self.on_tick_event)
        except Exception:  # noqa: BLE001 - shutdown must not raise
            pass
        logger.info("SlTpWorker stopped")

    async def on_tick_event(self, event: Any) -> None:
        if not self._running:
            return
        tick = tick_from_event(event)
        if tick is None:
            return
        bid, ask = tick_bid(tick), tick_ask(tick)
        if bid is None or ask is None:
            return
        try:
            bid, ask = Decimal(str(bid)), Decimal(str(ask))
            await self.process_tick(str(tick.symbol), bid, ask)
        except Exception:  # noqa: BLE001 - one bad tick must not kill the subscription
            logger.exception("SL/TP processing failed for tick %s", getattr(tick, "symbol", "?"))

    async def process_tick(self, symbol: str, bid: Decimal, ask: Decimal) -> int:
        """Check open positions in `symbol`; enqueue triggered ones for decoupled close.
        Returns the number of positions enqueued (public for tests/ops)."""
        TICK_COUNTERS.inc_sltp_worker(symbol)

        # Ensure close worker task is alive
        if self._running and (self._close_worker_task is None or self._close_worker_task.done()):
            self._close_worker_task = asyncio.create_task(
                self._run_close_worker(), name="sltp_close_worker"
            )

        triggered: List[Tuple[Position, str, Decimal]] = []

        # 1. Evaluate from in-memory index if ready (hot path: O(log M + K), no DB)
        if self.position_index and self.position_index.is_ready:
            triggered = self.position_index.find_triggered(symbol, bid, ask)
        else:
            # Fallback path if index not ready or absent (FAIL-CLOSED with loud error)
            getter = getattr(self.position_repo, "get_by_symbol", None)
            if getter is None:
                logger.error(
                    "position repository has no get_by_symbol; SL/TP triggers cannot "
                    "be evaluated for %s", symbol,
                )
                return 0
            logger.error("PositionIndex is not ready; falling back to DB get_by_symbol for %s", symbol)
            positions = await getter(symbol)
            for position in positions:
                trig = self._trigger_for(position, bid, ask)
                if trig is not None:
                    triggered.append((position, trig[0], trig[1]))

        enqueued = 0
        for position, reason, market_price in triggered:
            if position.position_id in self._in_flight:
                continue
            self._in_flight.add(position.position_id)
            try:
                self._close_queue.put_nowait((position, reason, market_price))
                enqueued += 1
            except asyncio.QueueFull:
                logger.error(
                    "SL/TP close queue full (depth=%d); dropping trigger for %s",
                    self._close_queue.maxsize, position.position_id,
                )
                self._in_flight.discard(position.position_id)

        # Yield to let the close worker start immediately
        if enqueued > 0:
            await asyncio.sleep(0)

        return enqueued

    async def _run_close_worker(self) -> None:
        """Background consumer: executes LP HTTP calls and DB transactions outside tick path."""
        while self._running:
            try:
                item = await self._close_queue.get()
            except asyncio.CancelledError:
                break
            except Exception:  # noqa: BLE001
                continue

            position, reason, market_price = item
            pid = position.position_id
            try:
                # Per-account lock: PreTradeRiskService account_lock from shared instance
                lock_ctx = (
                    self.risk_service.account_lock(str(position.account_login))
                    if self.risk_service and hasattr(self.risk_service, "account_lock")
                    else None
                )

                if lock_ctx is not None:
                    async with lock_ctx:
                        await self._execute_close(position, reason, market_price)
                else:
                    await self._execute_close(position, reason, market_price)
            except Exception as exc:  # noqa: BLE001
                logger.exception("Error executing SL/TP close for %s: %s", pid, exc)
            finally:
                self._in_flight.discard(pid)
                self._close_queue.task_done()

    async def _execute_close(self, position: Position, reason: str, market_price: Decimal) -> None:
        """Executes the LP HTTP call (if A-Book) and commits the local close transaction."""
        ext_id = getattr(position, "external_id", None)
        exec_price = market_price

        # --- A-BOOK STP Flow (Gorbunkov Semen rule: LP-First Confirmation) ---
        if ext_id:
            lp_success = False
            lp_already_closed = False
            try:
                pos_act_str = str(getattr(position, "action", "")).upper()
                lp_side = "buy" if "BUY" in pos_act_str else "sell"
                vol_float = float(position.volume.value if hasattr(position.volume, "value") else position.volume)
                lp_base_url = os.environ.get("BROKER_LP_URL", "http://127.0.0.1:8000")
                lp_endpoint = f"{lp_base_url.rstrip('/')}/api/v1/close-position"

                async with httpx.AsyncClient(timeout=5.0) as client:
                    resp = await client.post(lp_endpoint, json={
                        "symbol": position.symbol,
                        "ticket": str(ext_id),
                        "volume": vol_float,
                        "side": lp_side,
                        "price": 0.0,
                        "deviation": 50,
                    })
                    if resp.status_code == 200:
                        data = resp.json()
                        lp_success = (
                            data.get("status") in ("OK", "CLOSED", "success")
                            or data.get("success", False)
                            or (isinstance(data.get("data"), dict) and data["data"].get("success", False))
                        )
                        if "price" in data and data["price"]:
                            exec_price = Decimal(str(data["price"]))
                        elif isinstance(data.get("data"), dict) and data["data"].get("price"):
                            exec_price = Decimal(str(data["data"]["price"]))
                    elif resp.status_code >= 400:
                        lp_err = resp.text
                        try:
                            lp_err = resp.json().get("detail", resp.text)
                        except Exception:
                            pass
                        if "not found" in str(lp_err).lower() or "already closed" in str(lp_err).lower():
                            lp_already_closed = True
                        else:
                            logger.error(
                                "LP close rejected for position %s (ticket %s, status %s): %s",
                                position.position_id, ext_id, resp.status_code, lp_err
                            )
            except Exception as e:
                msg = str(e).lower()
                if "already closed" in msg or "not found" in msg:
                    lp_already_closed = True
                else:
                    logger.error("LP close failed for position %s (ticket %s): %s", position.position_id, ext_id, e)

            if not lp_success and not lp_already_closed:
                return
            if lp_already_closed:
                logger.warning("LP ticket %s was already closed at bridge; syncing local position at %s", ext_id, exec_price)

        # --- Execute Local Position Close ---
        try:
            await self.close_handler.handle(
                ClosePositionCommand(
                    account_login=position.account_login,
                    position_id=position.position_id,
                    volume=position.volume.value if hasattr(position.volume, "value") else Decimal(str(position.volume)),
                    price=exec_price,
                    comment=f"{reason} triggered at {exec_price}",
                    reason=reason,
                    venue_leg_already_unwound=bool(ext_id),
                )
            )
            # Remove from in-memory index
            if self.position_index:
                self.position_index.remove(position.position_id)
            logger.info(
                "position %s (%s %s) closed by %s at %s (route=%s)",
                position.position_id,
                position.action.name if hasattr(position.action, "name") else position.action,
                position.symbol, reason, exec_price, "A-BOOK" if ext_id else "B-BOOK",
            )
        except Exception as exc:  # noqa: BLE001
            msg = str(exc).lower()
            if "already closed" in msg or "not found" in msg:
                logger.info(
                    "position %s was already closed by another worker/process; skipping duplicate close",
                    position.position_id,
                )
                if self.position_index:
                    self.position_index.remove(position.position_id)
            else:
                logger.exception(
                    "%s close FAILED for position %s - position remains open and will retry",
                    reason, position.position_id,
                )

    async def flush(self) -> None:
        """Wait until all currently queued close tasks have finished executing (for tests/shutdown)."""
        await self._close_queue.join()

    @staticmethod
    def _trigger_for(position: Position, bid: Decimal, ask: Decimal) -> Optional[Tuple[str, Decimal]]:
        """('SL'|'TP', market trigger price) when triggered, else None."""
        act_str = str(getattr(position, "action", "")).upper()
        is_buy = "BUY" in act_str

        sl_raw = getattr(position, "price_sl", None)
        tp_raw = getattr(position, "price_tp", None)
        sl = Decimal(str(sl_raw.value if hasattr(sl_raw, "value") else sl_raw)) if sl_raw else None
        tp = Decimal(str(tp_raw.value if hasattr(tp_raw, "value") else tp_raw)) if tp_raw else None

        if is_buy:
            if sl is not None and sl > Decimal("0") and bid <= sl:
                return "SL", bid
            if tp is not None and tp > Decimal("0") and bid >= tp:
                return "TP", bid
        else:
            if sl is not None and sl > Decimal("0") and ask >= sl:
                return "SL", ask
            if tp is not None and tp > Decimal("0") and ask <= tp:
                return "TP", ask
        return None
