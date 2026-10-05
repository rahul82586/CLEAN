"""Pending-order expiration (MT5's ORDER_TIME_SPECIFIED / REQUEST_EXPIRATION).

Before M9, `orders.time_expiration` was a column nothing read: a pending order
with an expiration rested in the book forever. This worker sweeps expired
pendings — immediately on start (orders that expired while the server was
down) and every EXPIRATION_SWEEP_SECONDS (default 15) — cancels them through
the order's own state machine, and publishes ORDER_CANCELLED so subscribers
(the WebSocket bridge, audit) see it.

Time-based, not tick-based: an expiration must fire in a quiet market too.
DAY-mode expiration (end of the trading day) needs the EOD/session schedule
and is a documented gap; SPECIFIED-time is what this implements.
"""
import asyncio
import logging
import os
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Optional

from application.services.margin_reservation import release_margin
from core.events.domain_events import OrderCancelled
from core.ports.interfaces import IEventBus, IOrderRepository

logger = logging.getLogger(__name__)

DEFAULT_SWEEP_SECONDS = 15


class ExpirationWorker:
    def __init__(
        self,
        order_repo: IOrderRepository,
        event_bus: IEventBus,
        sweep_seconds: Optional[int] = None,
        account_repo: Optional[Any] = None,
    ):
        self.order_repo = order_repo
        self.event_bus = event_bus
        #: N13: the expiry release reads `getattr(self, "account_repo", None)`, and this
        #: constructor never set it - so it was ALWAYS None, `release_margin` fell through
        #: to its "no repository and no account in scope" warning, and every expired
        #: pending stranded its hold on `accounts.margin_reserved` exactly as before the
        #: R5 fix. Optional so existing construction sites keep working, but the server
        #: passes one.
        self.account_repo = account_repo
        if sweep_seconds is None:
            raw = os.environ.get("EXPIRATION_SWEEP_SECONDS", "").strip()
            try:
                sweep_seconds = int(raw) if raw else DEFAULT_SWEEP_SECONDS
            except ValueError:
                logger.warning(
                    "EXPIRATION_SWEEP_SECONDS=%r is not an integer; using %d",
                    raw, DEFAULT_SWEEP_SECONDS,
                )
                sweep_seconds = DEFAULT_SWEEP_SECONDS
        self.sweep_seconds = max(1, sweep_seconds)
        self._running = False

    async def start(self) -> None:
        self._running = True
        logger.info("ExpirationWorker started (sweep every %ds)", self.sweep_seconds)
        while self._running:
            try:
                await self.sweep_once()
            except Exception:  # noqa: BLE001 - the loop must survive a bad sweep
                logger.exception("expiration sweep failed")
            await asyncio.sleep(self.sweep_seconds)

    async def stop(self) -> None:
        self._running = False

    async def sweep_once(self, now: Optional[datetime] = None) -> int:
        """Cancel every pending whose time_expiration has passed. Public for
        tests and for an ops 'sweep now' command."""
        now = now or datetime.now(timezone.utc)
        finder = getattr(self.order_repo, "find_expired_orders", None)
        if finder is None:
            logger.error(
                "order repository has no find_expired_orders; expirations cannot "
                "be enforced"
            )
            return 0
        expired = await finder(now)
        cancelled = 0
        for order in expired:
            try:
                # Release the hold BEFORE cancelling, so a crash between the two cannot
                # leave the reservation stranded with nothing recording why. The old code
                # cancelled and saved without ever calling release_margin, so every
                # expired pending order leaked its hold out of the freemargin the client
                # could still use: reserve_margin subtracts margin_reserved from
                # availability, and nothing ever gave it back.
                hold = Decimal(str(getattr(order, "reserved_margin", 0) or 0))
                if hold > Decimal("0"):
                    await release_margin(
                        getattr(self, "account_repo", None),
                        order.account_login,
                        hold,
                    )
                    order.reserved_margin = Decimal("0")

                order.cancel("expired")  # state machine: CANCELLED + time_done
                await self.order_repo.save(order)
                await self.event_bus.publish(
                    OrderCancelled(
                        aggregate_id=order.ticket_id,
                        payload={
                            "order_id": order.ticket_id,
                            "account_login": str(order.account_login),
                            "symbol": order.symbol,
                            "reason": "expired",
                            "expiration": order.time_expiration.isoformat()
                            if order.time_expiration
                            else None,
                        },
                    )
                )
                cancelled += 1
                logger.info(
                    "order %s (%s %s) cancelled: expired at %s",
                    order.ticket_id, order.symbol,
                    order.order_type.name if hasattr(order.order_type, "name") else order.order_type,
                    order.time_expiration,
                )
            except Exception:  # noqa: BLE001 - one bad order must not stop the sweep
                logger.exception("could not cancel expired order %s", order.ticket_id)
        if cancelled:
            logger.info("expiration sweep cancelled %d order(s)", cancelled)
        return cancelled
