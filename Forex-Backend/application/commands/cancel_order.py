"""
Cancel Order Command Handler.

Cancels a pending order by:
1. Validating order exists and belongs to account
2. Validating order is in a cancellable state (not terminal)
3. Transitioning order state to CANCELLED
4. Releasing reserved margin (if margin was reserved)
5. Emitting OrderCancelled event

Architectural Note:
Only PENDING orders can be cancelled. Market orders that have already
been filled cannot be cancelled — they must be closed via ClosePosition.
"""
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from core.domains.accounts.account import Account
from application.services.margin_reservation import release_margin
from core.domains.common.value_objects import Money
from core.domains.oms.entities.order import Order
from core.domains.oms.enums import OrderState, OrderType
from core.events.domain_events import OrderCancelled
from core.ports.interfaces import (
    IAccountRepository,
    IEventBus,
    IOrderRepository,
)
from application.services.risk_service import PreTradeRiskService

logger = logging.getLogger(__name__)


@dataclass
class CancelOrderCommand:
    """Command to cancel a pending order."""
    account_login: int
    ticket_id: str
    reason: Optional[str] = None


class CancelOrderHandler:
    """Handler for CancelOrderCommand."""

    def __init__(
        self,
        account_repo: IAccountRepository,
        order_repo: IOrderRepository,
        risk_service: PreTradeRiskService,
        event_bus: IEventBus,
    ):
        self.account_repo = account_repo
        self.order_repo = order_repo
        self.risk_service = risk_service
        self.event_bus = event_bus

    async def handle(self, command: CancelOrderCommand) -> Order:
        """Execute the cancel order command."""
        # 1. Fetch order
        order = await self.order_repo.find_by_id(command.ticket_id)
        if not order:
            raise ValueError(f"Order {command.ticket_id} not found")

        # 2. Verify ownership
        if order.account_login != command.account_login:
            raise ValueError(
                f"Order {command.ticket_id} does not belong to account {command.account_login}"
            )

        # 3. Validate state (only non-terminal orders can be cancelled)
        if order.is_terminal():
            raise ValueError(
                f"Cannot cancel order in state {order.state.value}. "
                f"Order is already {order.state.value}."
            )

        # 4. Read the reservation that was ACTUALLY placed.
        #
        # This used to RECOMPUTE the hold as
        #     price_order * unfilled_volume * contract_size / 100
        # - a hardcoded leverage of 100, and the CFD price term applied to every calc
        # mode, with no margin rate and no currency conversion. The amount was already
        # recorded EXACTLY, on the order, when risk_service approved it. Re-deriving it
        # is what made the release wrong in the first place.
        reserved_margin = Decimal('0')
        if order.state in [OrderState.PLACED, OrderState.PARTIALLY_FILLED]:
            reserved_margin = Decimal(str(getattr(order, 'reserved_margin', 0) or 0))

        # 5. Cancel the order (inside per-account lock)
        async with self.risk_service.account_lock(command.account_login):
            # Transition state
            order.cancel(reason=command.reason or "Client cancellation")

            # Release the reservation through the ONE release path.
            #
            # The old code edited margin_used / margin_free in Python and saved the whole
            # row. It never touched accounts.margin_reserved - the column the reservation
            # actually lives in - so the hold survived the cancel forever, and
            # reserve_margin's SQL condition subtracts margin_reserved from availability,
            # so the client's free margin shrank permanently: no expiry, no alert.
            #
            # release_margin prefers the repository's atomic conditional UPDATE, which two
            # concurrent releases cannot both satisfy.
            if reserved_margin > Decimal('0'):
                account = await self.account_repo.find_by_login(command.account_login)
                await release_margin(
                    self.account_repo,
                    command.account_login,
                    reserved_margin,
                    account=account,
                )
                # The hold is released; the order holds nothing any more.
                order.reserved_margin = Decimal('0')

            # Persist order
            saved_order = await self.order_repo.save(order)

        # 6. Emit event
        event = OrderCancelled(
            aggregate_id=saved_order.ticket_id,
            payload={
                "ticket_id": saved_order.ticket_id,
                "account_login": command.account_login,
                "symbol": saved_order.symbol,
                "volume_initial": str(saved_order.volume_initial.value),
                "volume_current": str(saved_order.volume_current.value),
                "reason": command.reason,
            }
        )
        await self.event_bus.publish(event)

        logger.info(f"Order {command.ticket_id} cancelled")

        return saved_order