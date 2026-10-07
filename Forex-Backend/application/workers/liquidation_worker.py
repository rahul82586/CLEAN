"""
Liquidation Worker - Executes Liquidation Plans in Response to Stop-Out Events.

This worker:
1. Subscribes to StopOutEntered events from the Event Bus
2. Fetches the account and its open positions
3. Calls LiquidationService to calculate which positions to close
4. Executes the closure by creating closing Orders and Deals
5. Updates Positions and Account state
6. Emits PositionClosed events
"""
import asyncio
import logging
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict, Optional

from core.domains.accounts.account import Account
from core.domains.accounts.enums import SOActivation
from core.domains.common.value_objects import Money, Price, Volume
from core.domains.instruments.symbol import Symbol
from core.domains.market_data.models import Tick
from core.domains.market_data.feed_access import await_tick, tick_bid, tick_ask
from core.domains.oms.entities.deal import Deal
from core.domains.oms.entities.order import Order
from core.domains.oms.entities.position import Position
from core.domains.oms.enums import (
    DealEntry, DealReason, DealType, OrderState, OrderType, PositionAction
)
from core.domains.risk.liquidation_service import LiquidationService
from core.events.domain_events import DomainEvent, StopOutEntered, PositionClosed
from core.domains.accounts.thresholds import (
    DEFAULT_MARGIN_CALL_LEVEL,
    DEFAULT_STOP_OUT_LEVEL,
)
from core.ports.interfaces import (
    IAccountRepository,
    IDealRepository,
    IEventBus,
    IMarketDataFeed,
    IOrderRepository,
    IPositionRepository,
    ISymbolRepository,
)

logger = logging.getLogger(__name__)




async def _open_pendings_for_margin(account_login: Any) -> list:
    """Open pending orders for the margin engine, or [] when they cannot be read.

    R3: the engine can only cost pending orders if it is HANDED them, and nothing passed
    them - so `margin_used` excluded every working order and `margin_level` was overstated.

    `[]` on any failure reproduces the previous positions-only figure. That is the safe
    degradation: it never invents exposure and never crashes the valuation.
    """
    try:
        from api.di_providers import get_order_repo

        repo = get_order_repo()
    except Exception:  # noqa: BLE001
        return []
    if repo is None:
        return []
    for name in ("find_pending_orders", "get_open_orders", "get_pending_orders"):
        getter = getattr(repo, name, None)
        if getter is None:
            continue
        try:
            result = getter(str(account_login))
            if hasattr(result, "__await__"):
                result = await result
        except Exception as exc:  # noqa: BLE001
            logger.error(
                "could not list pending orders for %s via %s: %s", account_login, name, exc
            )
            return []
        out = []
        for order in (result or []):
            try:
                if getattr(order, "is_pending", None):
                    out.append(order)
            except Exception:  # noqa: BLE001
                continue
        return out
    return []

class LiquidationWorker:
    """
    Background worker that listens for StopOutEntered events and executes liquidations.
    
    Architectural Note:
    This worker runs as a background task. It subscribes to StopOutEntered events
    and processes them asynchronously. Each liquidation is wrapped in a Unit of Work
    to ensure atomicity (all updates succeed or all fail).
    """
    
    def __init__(
        self,
        account_repo: IAccountRepository,
        position_repo: IPositionRepository,
        order_repo: IOrderRepository,
        deal_repo: IDealRepository,
        symbol_repo: ISymbolRepository,
        market_data_feed: IMarketDataFeed,
        event_bus: IEventBus,
        liquidation_service: LiquidationService,
        risk_engine: Optional[Any] = None,
    ):
        self.account_repo = account_repo
        self.position_repo = position_repo
        self.order_repo = order_repo
        self.deal_repo = deal_repo
        self.symbol_repo = symbol_repo
        self.market_data_feed = market_data_feed
        self.event_bus = event_bus
        #: The platform's RiskEngine, built against the synchronous ConfigCache symbol
        #: view. Optional only for backwards compatibility; without it this worker builds
        #: one from the async symbol repository, and RiskEngine._symbol() refuses an async
        #: lookup - so margin would fail to recompute after a liquidation.
        self.risk_engine = risk_engine
        self.liquidation_service = liquidation_service
        # R4: hand the engine to the plan so it values PnL through
        # `calculate_position_pnl` - the same primitive `calculate_margin_level` uses -
        # rather than falling back to an unconverted rate of 1.0. Placed AFTER
        # `self.risk_engine` is assigned, because that is what it reads.
        if liquidation_service is not None and getattr(
            liquidation_service, "risk_engine", None
        ) is None:
            liquidation_service.risk_engine = risk_engine

        self._running = False
        self._task: Optional[asyncio.Task] = None
    
    async def start(self) -> None:
        """Start the worker, subscribe to StopOutEntered events, and start safety poll loop."""
        if self._running:
            return
        
        self._running = True
        self.event_bus.subscribe(StopOutEntered, self._on_stop_out_entered)
        self._task = asyncio.create_task(self._poll_loop())
        logger.info("LiquidationWorker started, subscribed to StopOutEntered events, and polling loop running")
    
    async def stop(self) -> None:
        """Stop the worker and unsubscribe from events."""
        if not self._running:
            return
        
        self._running = False
        self.event_bus.unsubscribe(StopOutEntered, self._on_stop_out_entered)
        if self._task is not None:
            self._task.cancel()
            self._task = None
        logger.info("LiquidationWorker stopped")

    async def _poll_loop(self) -> None:
        """Periodic safety poll: checks database for accounts in STOP_OUT state."""
        while self._running:
            try:
                await asyncio.sleep(5)
                if not self._running:
                    break
                finder = getattr(self.account_repo, "find_page", None)
                if finder is not None:
                    try:
                        rows, _ = await finder(so_active=True, limit=100)
                        for acc in rows:
                            so_val = getattr(acc.so_activation, "value", acc.so_activation)
                            so_name = str(getattr(acc.so_activation, "name", acc.so_activation)).upper()
                            if so_val == 2 or so_name == "STOP_OUT":
                                logger.warning(f"Stop-out poll found account {acc.login} in STOP_OUT state")
                                await self._execute_liquidation(acc.login)
                    except Exception as poll_err:
                        logger.error(f"Error in LiquidationWorker poll check: {poll_err}")
            except asyncio.CancelledError:
                break
            except Exception as loop_err:
                logger.error(f"Error in LiquidationWorker poll loop: {loop_err}")
    
    async def _on_stop_out_entered(self, event: StopOutEntered) -> None:
        # The margin level that TRIGGERED this stop-out, used for MT5's "[so XX%]" deal
        # comment. Taken from the event payload so the comment states the level the server
        # decided on, not one recomputed later after positions have already moved.
        try:
            payload = getattr(event, "payload", None) or {}
            raw_level = payload.get("margin_level")
            self._stop_out_level_pct = float(str(raw_level)) if raw_level is not None else None
        except (TypeError, ValueError):
            self._stop_out_level_pct = None
        """
        Handler for StopOutEntered events.
        
        This is called asynchronously when an account enters stop-out state.
        """
        account_login = event.payload.get("account_login")
        if not account_login:
            logger.error(f"StopOutEntered event missing account_login: {event.payload}")
            return
        
        logger.warning(f"StopOutEntered for account {account_login}, starting liquidation")
        
        try:
            await self._execute_liquidation(account_login)
        except Exception as e:
            logger.error(f"Liquidation failed for account {account_login}: {e}", exc_info=True)
    
    async def _execute_liquidation(self, account_login: int) -> None:
        """
        Execute the full liquidation process for an account.
        
        Steps:
        1. Fetch account and open positions
        2. Get current prices for all positions
        3. Calculate liquidation plan
        4. Execute closure for each position
        5. Update account state
        6. Emit events
        """
        # 1. Fetch account
        account = await self.account_repo.find_by_login(account_login)
        if not account:
            logger.error(f"Account {account_login} not found")
            return
        
        # 2. Fetch open positions
        open_positions = await self.position_repo.get_by_account(account_login)
        if not open_positions:
            logger.info(f"No open positions for account {account_login}")
            return
        
        # 3. Get current prices for all positions
        current_prices = {}
        conversion_rates = {}
        #: symbol -> (bid, ask). R12: value each leg on ITS OWN side.
        symbol_quotes: dict = {}
        # Built from the repositories this worker already holds. The engine is what
        # resolves cross rates, including the triangulation a JPY or AUD position needs
        # on a USD account; the hardcoded Decimal('1.0') it replaces assumed every
        # position's quote currency was the account currency.
        from core.domains.risk.engine import RiskEngine

        conversion_engine = self.risk_engine or RiskEngine(
            symbol_repo=self.symbol_repo, market_data_engine=self.market_data_feed
        )
        symbols = set(p.symbol for p in open_positions)
        
        for symbol_name in symbols:
            symbol = await self.symbol_repo.find_by_name(symbol_name)
            if not symbol:
                logger.error(f"Symbol {symbol_name} not found")
                continue
            
            # Get latest tick. await_tick accepts both the synchronous
            # MarketDataEngine.get_latest_tick and an async adapter; awaiting the
            # engine's Tick directly raised TypeError, so a stop-out could never be
            # executed against the real market data stack.
            tick = await await_tick(self.market_data_feed, symbol_name)
            if tick:
                bid, ask = tick_bid(tick), tick_ask(tick)
            # R12: keep BOTH sides. This used to pick ONE price for the whole symbol:
            #
            #     if any(BUY on this symbol): current_prices[s] = bid
            #     elif ask is not None:       current_prices[s] = ask
            #
            # In hedging mode (the default) an account can hold a BUY and a SELL on the same
            # symbol. The SELL was then valued at the BID, so its loss was UNDERSTATED, the
            # worst-loss-first sort ranked the wrong leg first, and the closing price was wrong
            # for that leg. A symbol holding only SELLs with no ask got no entry at all.
            #
            # `symbol_quotes` carries both sides for per-leg valuation; `current_prices` keeps
            # a representative price for the closing ORDER.
            if bid is not None or ask is not None:
                symbol_quotes[symbol_name] = (
                    Decimal(str(bid)) if bid is not None else None,
                    Decimal(str(ask)) if ask is not None else None,
                )
            if bid is not None:
                current_prices[symbol_name] = Price(Decimal(str(bid)))
            elif ask is not None:
                current_prices[symbol_name] = Price(Decimal(str(ask)))
            
            # Get conversion rate (simplified - in production, use RiskEngine)
            # Resolve the real rate. Hardcoding 1.0 here made worst-loss-first sort on
            # UNCONVERTED PnL, so on a USD account a -100,000 JPY loss (~-$667) ranked as
            # worse than a -$900 loss and the wrong position was closed first.
            try:
                conversion_rates[symbol_name] = conversion_engine.get_conversion_rate(
                    getattr(symbol, "quote_currency", "") or account.currency,
                    account.currency,
                )
            except Exception as exc:  # noqa: BLE001
                logger.error(
                    "cannot resolve %s -> %s for liquidation of %s; skipping rather than "
                    "sorting on an unconverted PnL: %s",
                    getattr(symbol, "quote_currency", "?"),
                    account.currency,
                    symbol_name,
                    exc,
                )
                continue
        
        # 4. Calculate liquidation plan
        plan = self.liquidation_service.calculate_liquidation_plan(
            account=account,
            open_positions=open_positions,
            current_prices=current_prices,
            conversion_rates=conversion_rates,
            symbol_quotes=symbol_quotes,   # R12: per-leg bid/ask
        )
        
        # --- MT5 step 1: release PENDING-order margin first ---------------
        #
        # "The terminal deletes a pending order with the largest margin reserved ...
        #  Orders without a reserved margin are not deleted."
        #
        # This step did not exist, so a stop-out closed a POSITION even when cancelling a
        # pending order would have restored the level. Cancelling costs the client nothing;
        # closing realises a loss. MT5 does the cheap action first.
        released = await self._release_pending_margin(account_login)
        if released:
            logger.info(
                "stop-out for account %s cancelled %d pending order(s) to release margin",
                account_login, released,
            )

        if not plan.positions_to_close:
            logger.info(f"No positions need to be closed for account {account_login}")
            return
        
        logger.warning(
            f"Liquidation plan for account {account_login}: "
            f"closing {len(plan.positions_to_close)} positions, "
            f"recovering {plan.total_pnl_recovered.amount} {plan.total_pnl_recovered.currency}"
        )
        
        # 5. Execute closure for each position
        for position in plan.positions_to_close:
            await self._close_position(account, position, current_prices.get(position.symbol))
        
        # 6. Update account state
        # Recalculate margin_used and margin_free
        remaining_positions = await self.position_repo.get_by_account(account_login)

        # Recomputed through the same MT5-accurate engine every other margin figure in
        # the platform comes from. This used to sum Position.calculate_margin_required(),
        # a sixth independent formula: volume * contract * PRICE_OPEN / leverage. Three
        # things were wrong with it here - it valued margin at the entry price instead of
        # the current one, it applied no currency conversion at all (so a USDJPY position
        # on a USD account was margined in yen), and it ignored the maintenance rates and
        # the per-symbol aggregation the engine handles. The numbers it wrote are exactly
        # what the stop-out recovery check below compares against, so an account could be
        # declared recovered - or never recovered - on a figure nothing else agreed with.
        total_margin_used = Decimal('0')
        total_pnl = Decimal('0')
        snapshot = None
        try:
            # R3: include working orders. This figure is what the recovery check below
            # compares against, so leaving pendings out makes an account read as more
            # recovered than it is.
            _remaining_pendings = await self._open_pending_orders(account_login)
            snapshot = conversion_engine.calculate_margin_level(
                account, remaining_positions, _remaining_pendings
            )
        except Exception as exc:  # noqa: BLE001 - fall back, but say so loudly
            # N9: this text described the pre-R13 behaviour. That fallback is gone - the
            # account is now LEFT IN STOP-OUT with its margins untouched and an alarm is
            # raised - so the log said the opposite of what the code does.
            logger.error(
                "could not recompute margin for %s through the risk engine after "
                "liquidation: %s. The account will be LEFT IN STOP-OUT with its margins "
                "unchanged and an alarm raised; no recovery is assumed.",
                account_login, exc,
            )

        if snapshot is not None:
            total_margin_used = snapshot.margin_used
            account.margin_used = Money(snapshot.margin_used, account.currency)
            account.equity = Money(snapshot.equity, account.currency)
            account.margin_free = Money(snapshot.margin_free, account.currency)
            account.margin_level = snapshot.margin_level
        else:
            # R13: DO NOT FABRICATE A RECOVERY.
            #
            # This branch used to write `margin_used = 0`, `margin_free = equity` and
            # `margin_level = 999999`, then compare that 999999 against the stop-out level
            # below, conclude the account had RECOVERED, clear every `so_*` marker and save
            # the row. An account whose margin could not be computed was declared healthy
            # with zero margin - and `margin_used = 0` makes every later `margin_level` read
            # 999999, so stop-out could never fire again for that account.
            #
            # The account stays in stop-out, nothing is written, nothing is cleared, and an
            # operator is told. A risk system must fail toward refusing, not toward
            # declaring health it did not measure.
            logger.critical(
                "POST-LIQUIDATION RECOMPUTE FAILED for account %s. The account is left "
                "in stop-out with its margins UNCHANGED; no recovery is assumed and no "
                "margin figure is fabricated. Manual review required.",
                account_login,
            )
            await self._alarm_recovery_unverified(account_login)
            return

        if snapshot is None and account.margin_used.amount > Decimal('0'):
            account.recompute_margin_level()
        
        # Check if we've recovered from stop-out
        # Percent fallback, matching MarginProfile's default.
        stop_out_level = (account.group.margin.stop_out_level if account.group
                          else DEFAULT_STOP_OUT_LEVEL)  # R11: one definition
        if account.margin_level >= stop_out_level:
            account.so_activation = SOActivation.NONE
            account.so_time = None
            account.so_level = None
            account.so_equity = None
            account.so_margin = None
            logger.info(f"Account {account_login} recovered from stop-out, margin_level={account.margin_level}")
        
        # R20: prefer a COLUMN-SCOPED write.
        #
        # `save()` is a full-row `session.merge`, so an account object read before a tick
        # landed resurrects stale profit / equity / margin_level. The tick pipeline avoids
        # exactly this by using `update_valuation`, so this sweep - which runs concurrently
        # with those ticks - does the same when the repository offers it, falling back to
        # `save` otherwise.
        _updater = getattr(self.account_repo, "update_valuation", None)
        if callable(_updater):
            try:
                await _updater(
                    account.login,
                    margin_used=account.margin_used.amount,
                    margin_free=account.margin_free.amount,
                    equity=account.equity.amount,
                    margin_level=account.margin_level,
                )
            except TypeError:
                # A differently-shaped updater: fall back rather than fail the sweep.
                await self.account_repo.save(account)
        else:
            await self.account_repo.save(account)
        
        logger.info(
            f"Liquidation complete for account {account_login}: "
            f"margin_level={account.margin_level}, "
            f"equity={account.equity.amount}"
        )
    
    async def _release_pending_margin(self, account_login: int) -> int:
        """Cancel pending orders, largest reserved margin first, while below stop-out.

        MT5's first stop-out action, and the one that costs the client least: a pending
        order holds margin but has no position and no unrealised loss, so cancelling it can
        restore the level without closing anything.

        Returns the number of orders cancelled. Re-reads the account before each
        cancellation so it stops as soon as the level is restored rather than cancelling
        everything.

        "Orders without a reserved margin are not deleted" - an order whose reserved_margin
        is zero or absent is skipped, per the doc.
        """
        cancelled = 0
        for _ in range(50):                      # bounded: never loop forever
            orders = await self._open_pending_orders(account_login)
            if not orders:
                return cancelled

            def reserved(order):
                value = getattr(order, "reserved_margin", None)
                return getattr(value, "amount", value) or 0

            candidates = [o for o in orders if reserved(o) and reserved(o) > 0]
            if not candidates:
                return cancelled

            target = max(candidates, key=reserved)

            # Stop as soon as the level is healthy again.
            #
            # Read the SAME attributes the production path reads:
            #   margin_level        an ATTRIBUTE (account.py:54), not a callable. Calling it
            #                       raised TypeError, and the bare except below swallowed
            #                       that - so this condition never ran and the loop
            #                       cancelled up to 50 orders regardless of the level.
            #   stop_out_level      an attribute of the GROUP's margin profile, not of the
            #                       account. `getattr(account, ...)` always missed, so the
            #                       threshold block was dead. Line 289 of this file reads it
            #                       correctly; this now matches.
            account = await self.account_repo.find_by_login(str(account_login))
            if account is None:
                return cancelled

            group_margin = getattr(getattr(account, "group", None), "margin", None)
            stop_out_level = getattr(group_margin, "stop_out_level", None)
            if stop_out_level is None:
                # Same percent fallback the recovery check at line 289 uses, so the two
                # cannot disagree about what "recovered" means.
                stop_out_level = DEFAULT_STOP_OUT_LEVEL  # R11: one definition

            current_level = getattr(account, "margin_level", None)
            if current_level is not None:
                try:
                    if Decimal(str(current_level)) >= Decimal(str(stop_out_level)):
                        return cancelled
                except (TypeError, ValueError, ArithmeticError) as exc:
                    # Logged, not swallowed. A silent pass here is what hid the TypeError
                    # that made this whole step a no-op.
                    logger.warning(
                        "stop-out: could not compare margin level %r against %r (%s)",
                        current_level, stop_out_level, exc,
                    )

            try:
                # Release the HOLD as well as cancelling the order. Cancel alone leaves
                # `accounts.margin_reserved` set forever, which is the R5 leak: the client's
                # free margin shrinks permanently with no expiry and no alert.
                hold = getattr(target, "reserved_margin", None)
                target.cancel("stop-out: released reserved margin")
                await self.order_repo.save(target)
                await self._release_hold(account_login, hold)
                await self._announce_cancellation(target, account_login, "stop-out")
                cancelled += 1
                logger.info("stop-out released pending order %s (reserved %s)",
                            getattr(target, "ticket_id", "?"), reserved(target))
            except Exception as exc:              # noqa: BLE001
                logger.error("could not cancel pending order during stop-out: %s", exc)
                return cancelled
        return cancelled

    async def _announce_cancellation(self, order: Any, account_login: int, reason: str) -> None:
        """Publish OrderCancelled for a stop-out cancellation (audit R14 completion).

        The row was cancelled and the hold released, but nothing was published - so the
        client's terminal kept showing a working order that no longer existed, the
        WebSocket bridge had nothing to push, and ConfigCache never refreshed. Every other
        cancellation path in the codebase (`cancel_order.py`, `expiration_worker.py`)
        publishes this event; a stop-out is not a reason to be quieter about it.

        Never raises: a missed notification must not abort a liquidation that is already
        releasing the client's margin.
        """
        try:
            from core.events.domain_events import OrderCancelled

            await self.event_bus.publish(
                OrderCancelled(
                    aggregate_id=getattr(order, "ticket_id", ""),
                    payload={
                        "ticket_id": getattr(order, "ticket_id", ""),
                        "order_id": getattr(order, "ticket_id", ""),
                        "account_login": str(account_login),
                        "symbol": getattr(order, "symbol", ""),
                        "volume_initial": str(
                            getattr(getattr(order, "volume_initial", None), "value", "")
                        ),
                        "volume_current": str(
                            getattr(getattr(order, "volume_current", None), "value", "")
                        ),
                        "reason": reason,
                    },
                )
            )
        except Exception as exc:  # noqa: BLE001
            logger.error(
                "could not publish OrderCancelled for stop-out cancellation of %s: %s",
                getattr(order, "ticket_id", "?"), exc,
            )

    async def _release_hold(self, account_login: int, hold: Any) -> None:
        """Atomically release a reservation, when the repository supports it.

        Uses `release_margin` rather than editing `margin_used`/`margin_reserved` in Python:
        the repository's version is a conditional SQL update, so two concurrent releases
        cannot both succeed. (The cancel path used to edit the attributes and save the row -
        that was the R5 leak, and it now calls this same helper.)

        A missing amount, a missing repository or a repository without `release_margin` is
        reported and skipped - never guessed at, because guessing here either strands margin
        or invents free margin.
        """
        amount = getattr(hold, "amount", hold)
        if amount is None:
            return
        try:
            amount = Decimal(str(amount))
        except (TypeError, ValueError):
            logger.warning("stop-out: unreadable reserved_margin %r; not released", hold)
            return
        if amount <= 0:
            return

        release = getattr(self.account_repo, "release_margin", None)
        if release is None:
            logger.error(
                "stop-out: account repository has no release_margin; %s stays reserved "
                "for account %s", amount, account_login,
            )
            return
        try:
            await release(str(account_login), amount)
            logger.info(
                "stop-out released reservation %s on account %s", amount, account_login
            )
        except Exception as exc:                  # noqa: BLE001
            logger.error(
                "stop-out could not release reservation %s on account %s: %s",
                amount, account_login, exc,
            )

    async def _alarm_recovery_unverified(self, account_login: int) -> None:
        """Announce that a liquidated account could NOT be re-valued.

        R13: recovery after a stop-out is a RISK DECISION and must be based on a margin
        level the engine actually produced. When the recompute fails the account is left in
        stop-out, so somebody has to be told - otherwise it simply sits there while an
        operator believes the sweep ran.
        """
        try:
            await self.event_bus.publish(
                DomainEvent(
                    aggregate_id=str(account_login),
                    payload={
                        "kind": "liquidation_recompute_failed",
                        "account_login": str(account_login),
                        "action_required": (
                            "account left in stop-out; margin could not be recomputed "
                            "after liquidation"
                        ),
                    },
                )
            )
        except Exception as exc:  # noqa: BLE001 - the alarm must never mask the fault
            logger.error("could not publish the liquidation alarm: %s", exc)


    async def _open_pending_orders(self, account_login: int) -> list:
        """Open pending orders for an account, or [] when the repository cannot say."""
        for name in ("get_open_orders", "get_pending_orders", "find_pending_orders"):
            getter = getattr(self.order_repo, name, None)
            if getter is None:
                continue
            try:
                result = getter(str(account_login))
                if hasattr(result, "__await__"):
                    result = await result
                return [o for o in (result or [])
                        if not getattr(o, "is_market", lambda: True)()]
            except Exception as exc:              # noqa: BLE001
                logger.error("could not list pending orders for %s: %s", account_login, exc)
                return []
        return []

    async def _close_position(
        self,
        account: Account,
        position: Position,
        current_price: Optional[Price],
    ) -> None:
        """
        Close a single position by creating a closing Order and Deal.
        
        MT5 Logic:
        1. Create a closing Order (opposite side of position)
        2. Create a Deal with entry=OUT
        3. Update Position volume to 0
        4. Emit PositionClosed event
        """
        if not current_price:
            logger.error(f"No current price for {position.symbol}, cannot close position")
            return
        
        # Determine closing side (opposite of position)
        if position.action == PositionAction.BUY:
            close_side = "SELL"
            deal_type = DealType.SELL
        else:
            close_side = "BUY"
            deal_type = DealType.BUY
        
        # R4: value the closed PnL ONCE, in the account's currency, BEFORE writing the
        # deal or the balance. This used to convert at 1.0 in the plan and then book the
        # raw `position.profit` here - so on a USD account a -15,000 JPY loss was booked
        # as -$15,000 (150x out at a rate of 150), and the deal and the balance were two
        # different numbers for one event.
        realised_pnl = None
        _pnl_engine = getattr(self, "risk_engine", None)
        if _pnl_engine is not None:
            try:
                realised_pnl = Money(
                    _pnl_engine.calculate_position_pnl(account, position),
                    account.currency,
                )
            except Exception as exc:  # noqa: BLE001
                logger.error(
                    "liquidation: cannot value %s (%s) in %s: %s",
                    position.position_id, position.symbol, account.currency, exc,
                )
                realised_pnl = None

        # 1. Create closing Order
        closing_order = Order(
            account_login=account.login,
            symbol=position.symbol,
            order_type=OrderType[close_side],
            volume_initial=position.volume,
            volume_current=position.volume,
            price_order=current_price,
            state=OrderState.FILLED,
            reason="LIQUIDATION",
            # MT5 marks a stop-out deal "[so XX%]", where XX is the margin level at which
            # the stop-out occurred. The previous "[LIQUIDATION] ..." string could not be
            # recognised as a stop-out by a client, a report, or the compensation logic.
            comment=(f"[so {self._stop_out_level_pct:.0f}%]"
                     if getattr(self, "_stop_out_level_pct", None) is not None
                     else "[so]") + f" closing {position.position_id}",
        )
        
        await self.order_repo.save(closing_order)
        
        # 2. Create Deal
        closing_deal = Deal(
            order_id=closing_order.ticket_id,
            position_id=position.position_id,
            account_login=account.login,
            symbol=position.symbol,
            deal_type=deal_type,
            entry=DealEntry.OUT,
            reason=DealReason.SO,  # Stop-out
            volume=position.volume,
            price=current_price,
            profit=realised_pnl if realised_pnl is not None else position.profit,  # CONVERTED (R4)
            swap=position.swap,
            commission=position.commission,
            comment=closing_order.comment,
        )
        
        await self.deal_repo.save(closing_deal)

        # 2b. Book the realised PnL to the account balance.
        #
        # RecordDealHandler does this for a client-initiated close; the liquidation path
        # wrote the deal straight to the repository and skipped it, so a stopped-out
        # account kept its pre-loss balance while its position - and the loss with it -
        # disappeared. Step 6 below then recomputed equity as balance + PnL over the
        # REMAINING positions, which no longer included the closed one: the client's
        # realised loss was simply deleted, the margin level jumped, and the account
        # could carry on trading with money it had already lost.
        # R4: book CONVERTED money, in the account's own currency.
        #
        # This used to add `position.profit.amount` to `account.balance.amount` and
        # re-wrap the sum in the BALANCE's currency:
        #
        #     account.balance = Money(
        #         account.balance.amount + position.profit.amount,
        #         account.balance.currency,
        #     )
        #
        # which deliberately bypasses `Money.__add__`'s currency guard - it adds a JPY
        # amount to a USD amount and declares the result USD. A -15,000 JPY loss on a USD
        # account became -$15,000: a 150x overstatement at a rate of 150.
        if realised_pnl is None:
            # Booking `position.profit` here would put a quote-currency figure onto a
            # deposit-currency balance, which IS the defect. Refuse and say so, so the
            # post-liquidation recompute and an operator can reconcile it.
            logger.error(
                "liquidation of %s did not book a balance change: the position could not "
                "be valued in %s. The stored profit is %s and must be reconciled manually.",
                position.position_id, account.currency, position.profit,
            )
        elif realised_pnl.amount != 0:
            account.balance = Money(
                account.balance.amount + realised_pnl.amount, account.currency
            )
            logger.info(
                "liquidation of %s realised %s %s onto account %s balance",
                position.position_id, realised_pnl.amount, account.currency, account.login,
            )

        # 3. Update Position
        # H3: captured BEFORE the zeroing below. The PositionClosed payload used to read
        # `position.volume.value` after this line had already set it to 0, so every
        # liquidation told the client - and the WebSocket bridge, and anything downstream -
        # that it had closed ZERO lots.
        closed_volume = position.volume.value

        position.volume = Volume(Decimal('0'))
        position.time_done = datetime.now(timezone.utc)
        position.deal_close = closing_deal.deal_id
        
        await self.position_repo.save(position)
        
        # 4. Emit PositionClosed event
        event = PositionClosed(
            aggregate_id=position.position_id,
            payload={
                "position_id": position.position_id,
                "account_login": account.login,
                "symbol": position.symbol,
                "volume_closed": str(closed_volume),
                "close_price": str(current_price.value),
                "realized_pnl": str(realised_pnl.amount if realised_pnl is not None else position.profit.amount),  # R4: converted, matching the deal and the balance
                "deal_id": closing_deal.deal_id,
                "reason": "LIQUIDATION",
            },
        )
        
        await self.event_bus.publish(event)
        
        logger.info(
            f"Position {position.position_id} closed: "
            f"volume={position.volume.value}, "
            f"price={current_price.value}, "
            f"pnl={realised_pnl.amount if realised_pnl is not None else position.profit.amount}"
        )