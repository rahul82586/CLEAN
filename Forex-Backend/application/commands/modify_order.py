"""
Modify Order Command Handler.

Modifies a pending order's price, stop loss, or take profit:
1. Validates order exists and belongs to account
2. Validates order is in a modifiable state (PLACED or PARTIALLY_FILLED)
3. Recalculates margin if price changes
4. Updates order fields
5. Emits OrderModified event

Architectural Note:
Only PENDING orders can be modified. Filled orders cannot be modified —
use ModifyDeal (Trade Modification) for post-fill changes.
"""
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from core.domains.accounts.account import Account
from core.domains.common.value_objects import Money, Price
from core.domains.oms.entities.order import Order
from core.domains.oms.enums import OrderState
from core.events.domain_events import OrderModified
from core.ports.interfaces import (
    IAccountRepository,
    IEventBus,
    IOrderRepository,
)
from application.services.risk_service import PreTradeRiskService

logger = logging.getLogger(__name__)


@dataclass
class ModifyOrderCommand:
    """Command to modify a pending order."""
    account_login: int
    ticket_id: str
    new_price: Optional[Decimal] = None
    new_stop_loss: Optional[Decimal] = None
    new_take_profit: Optional[Decimal] = None
    new_expiration: Optional[datetime] = None
    reason: Optional[str] = None


class ModifyOrderHandler:
    """Handler for ModifyOrderCommand."""

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

    async def handle(self, command: ModifyOrderCommand) -> Order:
        """Execute the modify order command."""
        # 1. Fetch order
        order = await self.order_repo.find_by_id(command.ticket_id)
        if not order:
            raise ValueError(f"Order {command.ticket_id} not found")

        # 2. Verify ownership
        if order.account_login != command.account_login:
            raise ValueError(
                f"Order {command.ticket_id} does not belong to account {command.account_login}"
            )

        # 3. Validate state (only pending orders can be modified)
        if order.state not in [OrderState.PLACED, OrderState.PARTIALLY_FILLED]:
            raise ValueError(
                f"Cannot modify order in state {order.state.value}. "
                f"Only PLACED or PARTIALLY_FILLED orders can be modified."
            )

        # 4. Calculate margin delta if price changes
        old_price = order.price_order.value
        new_price = command.new_price if command.new_price is not None else old_price
        margin_delta = Decimal('0')

        if new_price != old_price:
            # Calculate margin difference
            # New margin - Old margin = Delta
            volume = order.volume_current.value
            contract_size = order.contract_size

            # R16: do NOT re-derive the requirement with a local formula.
            #
            # This was `(price * volume * contract_size) / Decimal('100')` - the FOURTH
            # independent margin formula in the codebase: hardcoded leverage 100, the CFD
            # price term applied to Forex, no calc mode, no margin rate, no conversion.
            #
            # The reservation was already computed by `risk_service` and stored on the
            # order, so scaling THAT by the price ratio is exact.
            volume = order.volume_current.value
            old_margin = Decimal(str(getattr(order, "reserved_margin", 0) or 0))
            if old_price != 0 and old_margin > 0:
                new_margin = old_margin * (new_price / old_price)
                margin_delta = new_margin - old_margin
            else:
                margin_delta = Decimal("0")

        # 5. Modify the order (inside per-account lock)
        async with self.risk_service.account_lock(command.account_login):
            # Check if account has enough margin for price increase
            if margin_delta > Decimal('0'):
                account = await self.account_repo.find_by_login(command.account_login)
                if account and margin_delta > account.margin_free.amount:
                    raise ValueError(
                        f"Insufficient margin for price change. "
                        f"Required additional: {margin_delta}, "
                        f"Available: {account.margin_free.amount}"
                    )

            # Apply modifications
            if command.new_price is not None:
                order.price_order = Price(command.new_price)

            if command.new_stop_loss is not None:
                order.price_sl = Price(command.new_stop_loss)

            if command.new_take_profit is not None:
                order.price_tp = Price(command.new_take_profit)

            if command.new_expiration is not None:
                order.time_expiration = command.new_expiration

            # R16: move the RESERVATION, not `margin_used`.
            #
            # This edited `account.margin_used` / `margin_free` and full-row saved, never
            # touching `orders.reserved_margin` or `accounts.margin_reserved`. A pending
            # order holds a RESERVATION; it does not consume position margin until it fills,
            # which is why the two columns exist separately. Writing `margin_used` here also
            # made a pending order look like a filled position to every reader of it.
            if margin_delta != Decimal("0"):
                from application.services.margin_reservation import (
                    release_margin,
                    reserve_margin,
                )

                account = await self.account_repo.find_by_login(command.account_login)
                if account:
                    if margin_delta > 0:
                        # `reserve_margin` is a conditional SQL update: it REFUSES rather
                        # than over-committing the account.
                        held = await reserve_margin(self.account_repo, account, margin_delta)
                        if not held:
                            raise ValueError(
                                f"Insufficient free margin for the price change. "
                                f"Additional required: {margin_delta}"
                            )
                    else:
                        await release_margin(
                            self.account_repo,
                            command.account_login,
                            -margin_delta,
                            account=account,
                        )
                    # The order now records exactly what it holds.
                    order.reserved_margin = max(Decimal("0"), old_margin + margin_delta)

            # Persist order
            saved_order = await self.order_repo.save(order)

        # 6. Emit event
        event = OrderModified(
            aggregate_id=saved_order.ticket_id,
            payload={
                "ticket_id": saved_order.ticket_id,
                "account_login": command.account_login,
                "symbol": saved_order.symbol,
                "new_price": str(command.new_price) if command.new_price else None,
                "new_stop_loss": str(command.new_stop_loss) if command.new_stop_loss else None,
                "new_take_profit": str(command.new_take_profit) if command.new_take_profit else None,
                "reason": command.reason,
            }
        )
        await self.event_bus.publish(event)

        logger.info(f"Order {command.ticket_id} modified")

        return saved_order