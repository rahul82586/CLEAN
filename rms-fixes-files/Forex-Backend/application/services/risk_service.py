"""
Pre-Trade Risk Service for validating orders before execution.
Encapsulates all margin, permission, and account state checks.
"""
import asyncio
import logging
from decimal import Decimal
from typing import Any, Dict, Optional

from core.domains.accounts.models import Account, Group
from core.domains.instruments.models import Symbol
from core.domains.oms.entities.order import Order, OrderType
from core.domains.oms.retcodes import Retcode
from core.domains.common.value_objects import Money, Price, Volume
from core.events.domain_events import DomainEvent, OrderApproved, OrderRejected, EventType
from core.ports.interfaces import IEventBus, IPositionRepository

logger = logging.getLogger(__name__)


class PreTradeRiskService:
    """
    Service responsible for pre-trade validation.

    Architectural Purpose:
    Centralizes all risk checks required before an order can be accepted.
    Prevents race conditions using per-account asyncio.Lock context managers.
    """

    def __init__(
        self,
        event_bus: Optional[IEventBus] = None,
        position_repo: Optional[IPositionRepository] = None,
        risk_engine: Optional[Any] = None,
        symbol_repo: Optional[Any] = None,
        account_repo: Optional[Any] = None,
        holiday_repo: Optional[Any] = None,
        order_repo: Optional[Any] = None,
    ):
        self.event_bus = event_bus
        self.position_repo = position_repo
        self.risk_engine = risk_engine
        self.symbol_repo = symbol_repo
        self.account_repo = account_repo
        #: The HOLIDAY repository - a different repository from `symbol_repo`.
        #: `_check_holiday` used to probe `symbol_repo`, whose `get_all()` returns
        #: SYMBOLS, so the holiday gate never once ran on the order path.
        self.holiday_repo = holiday_repo
        #: Order repository, for MT5's group LimitOrders - which counts working
        #: ORDERS. The old code counted POSITIONS for it.
        self.order_repo = order_repo
        self._account_locks: Dict[str, asyncio.Lock] = {}
        #: reason for the most recent rejection. validate_order() returns a bool, so a
        #: caller that suppresses event publishing (CreateOrderHandler does, to keep the
        #: approval from firing inside the account lock) would otherwise have to invent
        #: a reason for its own OrderRejected event and its log line.
        self.last_rejection_reason: Optional[str] = None
        #: MT5 code for the most recent rejection (core.domains.oms.retcodes.Retcode).
        #: Kept beside the reason so an API layer can answer with the code MT5 would
        #: have returned (e.g. 10019 NO_MONEY) instead of a generic 10013.
        self.last_rejection_code: Optional[int] = None
        #: symbol -> set of live position sides ("BUY"/"SELL"), refreshed by
        #: _check_order_and_position_limits so the hedge check can see the book
        #: without a second repository round-trip.
        self._live_position_sides: Dict[str, set] = {}

    def get_account_lock(self, account_login: str) -> asyncio.Lock:
        """
        Returns the per-account lock to guarantee single-writer isolation
        during pre-trade risk checks and margin reservations.
        """
        login_key = str(account_login)
        if login_key not in self._account_locks:
            self._account_locks[login_key] = asyncio.Lock()
        return self._account_locks[login_key]

    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def account_lock(self, account_login: str):
        """
        Async context manager providing per-account locking.
        Usage: async with risk_service.account_lock(account_login): ...
        """
        lock = self.get_account_lock(account_login)
        async with lock:
            yield lock

    async def validate_order(
        self,
        order: Order,
        account: Account,
        symbol: Symbol,
        current_price: Price,
        publish_events: bool = True,
    ) -> bool:
        """
        Performs all pre-trade checks under per-account lock protection.
        Uses 'async with' to guarantee lock release even if an exception occurs.
        Returns True if approved, False if rejected.

        `publish_events=False` suppresses the OrderApproved/OrderRejected publish.
        CreateOrderHandler uses it, because an approval published from inside the
        per-account lock is delivered (the bus awaits handlers inline) to an
        ExecutionOrchestrator that then fetches the same account and takes the same
        lock - a self-deadlock - and it is published before the order is persisted, so
        the orchestrator's find_by_id returns None. The handler validates under the
        lock, persists, then publishes.
        """
        account_login = str(getattr(account, 'login', getattr(account, 'login_id', getattr(account, 'id', 'default'))))
        lock = self.get_account_lock(account_login)

        # CRITICAL: Use 'async with' to guarantee lock release on exception
        async with lock:
            logger.info(f"Running pre-trade checks under lock for Order {order.ticket_id} on Account {account_login}")

            # 1. Fetch LIVE account state if account_repo is available
            live_account = account
            if self.account_repo:
                try:
                    fetched = await self.account_repo.find_by_login(account_login)
                    if fetched:
                        live_account = fetched
                except Exception as e:
                    logger.warning(f"Could not refresh live account state for {account_login}: {e}")

            # 2. Account State Check
            if not live_account.can_trade():
                reason = "Account is disabled or pending KYC verification"
                self.last_rejection_code = Retcode.TRADE_DISABLED
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 3. Symbol Permission Check (Group Rules)
            if not self._check_symbol_permission(live_account.group, symbol.name):
                reason = f"Symbol {symbol.name} is not allowed for Group {live_account.group.name if live_account.group else 'Unknown'}"
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                self.last_rejection_code = Retcode.TRADE_DISABLED
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 4. Trading Session Check
            # Symbol has is_trade_session_active(datetime); there is no is_within_session,
            # so this step raised AttributeError for every order that reached it.
            from datetime import datetime, timezone
            _now = datetime.now(timezone.utc)
            if not symbol.is_trade_session_active(_now):
                reason = f"Symbol {symbol.name} is currently outside trading sessions"
                self.last_rejection_code = Retcode.MARKET_CLOSED
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 4a. Maximum quote delay (MT5 Trade tab, `QuotesTimeout`).
            #
            # "time (in seconds) of delay in the receipt of quotes, after which trading
            # will be automatically disabled for this symbol. As quotes start coming
            # again, trade will be enabled automatically."
            #
            # Per symbol, and both directions are automatic: nothing has to be reset when
            # the feed resumes, because the comparison is against the CURRENT tick age.
            #
            # Rejected as MARKET_CLOSED because that is what MT5 does - it disables
            # trading for the symbol rather than reporting a pricing fault - and a client
            # sees the same outcome either way.
            #
            # Placed here, next to the session check, because both ask "is this symbol
            # tradeable right now?" and MT5's pipeline treats them together.
            delay_reason = await self._check_max_quote_delay(symbol, _now)
            if delay_reason is not None:
                logger.warning(f"Order {order.ticket_id} rejected: {delay_reason}")
                self.last_rejection_reason = delay_reason
                self.last_rejection_code = Retcode.MARKET_CLOSED
                if publish_events:
                    await self._publish_rejection(order, delay_reason)
                return False

            # 4b. Holiday Check.
            # MT5 request-processing pipeline: "request time not on a holiday".
            # The instruments domain has carried Holiday since M2 and nothing ever
            # consulted it during order validation, so a configured holiday did not
            # stop trading.
            holiday = None
            if self.symbol_repo is not None:
                holiday = await self._check_holiday(symbol.name, _now)
            if holiday is not None:
                reason = f"Market for {symbol.name} is closed today (holiday: {holiday})"
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                self.last_rejection_code = Retcode.MARKET_CLOSED
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 5. Volume Limits Check
            if not self._check_volume_limits(order.volume, symbol, live_account):
                reason = f"Volume {order.volume.value} exceeds limits for {symbol.name} (Min: {symbol.volume_min}, Max: {symbol.volume_max})"
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                self.last_rejection_code = Retcode.INVALID_VOLUME
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 5a. Stops Level Check.
            # MT5 ``CMTConSymbol::StopsLevel`` / ``IMTConSymbol::StopsLevel``: the
            # minimum distance in POINTS between the current price and SL/TP. Below
            # it the server answers MT_RET_REQUEST_INVALID_STOPS (10016). The field
            # has existed on Symbol since M1 (``stops_level``) and was enforced
            # nowhere, so a client could park SL/TP inside the frozen band.
            if not self._check_stops_level(order, symbol, current_price):
                reason = (
                    f"Invalid stops on {symbol.name}: SL/TP must be at least "
                    f"{symbol.stops_level} points from the current price"
                )
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                self.last_rejection_code = Retcode.INVALID_STOPS
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 5b. Group limits: order count, position count, aggregate volume.
            # MT5 group rule engine (IConGroup LimitOrders/LimitPositions/…):
            # MT_RET_REQUEST_LIMIT_ORDERS (10033), _LIMIT_POSITIONS (10040),
            # _LIMIT_VOLUME (10034). The three fields existed on Group and none of
            # them was ever consulted at order entry.
            if not await self._check_order_and_position_limits(live_account, symbol, order):
                reason = self.last_rejection_reason
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 5c. Group trade-flag checks (hedge prohibition, close-only).
            # MT5 ``MT_RET_REQUEST_HEDGE_PROHIBITED`` (10046) and
            # ``MT_RET_REQUEST_CLOSE_ONLY`` (10044) are group rule-engine outcomes
            # (IConGroup TradeFlags). Both flags exist here as TradeFlags members
            # and were read by nothing.
            if not self._check_group_trade_flags(live_account, order, symbol):
                reason = self.last_rejection_reason
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # 6. Live Margin Requirement Check
            required_margin = await self._check_margin_requirement(
                order, live_account, symbol, current_price
            )
            if required_margin is None:
                reason = "Insufficient free margin to open this position"
                logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                self.last_rejection_reason = reason
                self.last_rejection_code = Retcode.NO_MONEY
                if publish_events:
                    await self._publish_rejection(order, reason)
                return False

            # M6 (M4 debt #1): hold the requirement before approving. Between
            # here and the fill nothing else moves a number the check reads, so
            # without the hold two concurrent orders - across a Redis bus, or
            # across two API nodes - could both pass the same free-margin check
            # and both book. The SQL repository does this as ONE conditional
            # UPDATE (the database serialises the racers); the amount held is
            # recorded on the order so the release at fill/reject is exact.
            from application.services.margin_reservation import (
                release_margin,
                reserve_margin,
            )

            if required_margin > 0:
                if not await reserve_margin(self.account_repo, live_account, required_margin):
                    reason = (
                        "Insufficient free margin to open this position "
                        "(reserved by concurrent in-flight orders)"
                    )
                    self.last_rejection_code = Retcode.NO_MONEY
                    logger.warning(f"Order {order.ticket_id} rejected: {reason}")
                    self.last_rejection_reason = reason
                    if publish_events:
                        await self._publish_rejection(order, reason)
                    return False
                order.reserved_margin = required_margin

            # All checks passed under lock protection
            logger.info(f"Order {order.ticket_id} approved by Pre-Trade Risk Service")
            self.last_rejection_reason = None
            # Cleared together with the reason: a consumer reading only the code
            # after a success would otherwise get whatever the PREVIOUS order was
            # rejected with.
            self.last_rejection_code = None
            if publish_events:
                try:
                    await self._publish_approval(order)
                except Exception:
                    # the approval never reached the orchestrator: un-hold
                    if order.reserved_margin:
                        await release_margin(
                            self.account_repo, live_account.login,
                            order.reserved_margin, account=live_account,
                        )
                        order.reserved_margin = Decimal("0")
                    raise
            return True

    async def _check_max_quote_delay(self, symbol: Any, now: Any) -> Optional[str]:
        """MT5's per-symbol maximum quote delay. Returns a reason, or None to allow.

        `QuotesTimeout` is in SECONDS. A value of 0 means "no limit" and is the common
        case in the reference export - read literally it would disable trading within a
        second of the last tick, so it is treated as disabled.

        This is deliberately NOT wired to the global `*_TICK_AGE_SECONDS` settings. Those
        are ours and answer "may this quote be used at all"; this answers MT5's separate
        question of "is trading enabled for this symbol right now". Mixing them would
        make a per-symbol setting behave globally.

        A symbol with NO tick at all is refused when a delay is configured: MT5 disables
        trading on a symbol whose quotes have not arrived, and "never arrived" is the
        extreme case of that, not an exemption from it.
        """
        timeout = self._symbol_quote_timeout(symbol)
        if timeout <= 0:
            return None                      # 0 disables the check

        tick = await self._latest_tick(symbol.name)
        if tick is None:
            return (
                f"{symbol.name} has no live quote and Max quote delay is "
                f"{timeout}s - trading is disabled for this symbol until quotes arrive"
            )

        age = self._tick_age_seconds(tick, now)
        if age is None:
            return None                      # no timestamp to judge against
        if age > timeout:
            return (
                f"{symbol.name} quote is {age:.0f}s old, beyond its Max quote delay of "
                f"{timeout}s - trading is disabled for this symbol until quotes resume"
            )
        return None

    @staticmethod
    def _symbol_quote_timeout(symbol: Any) -> float:
        """`QuotesTimeout` in seconds, from the entity or its mt5_extra quarantine."""
        import os as _os

        raw = getattr(symbol, "quotes_timeout", None)
        if raw is None:
            extra = getattr(symbol, "mt5_extra", None) or {}
            raw = extra.get("QuotesTimeout")
        if raw is None:
            # Not configured on the symbol: fall back to the environment so a deployment
            # can impose a floor, but default to disabled to match the export.
            raw = _os.environ.get("DEFAULT_MAX_QUOTE_DELAY_SECONDS", "0")
        try:
            return float(raw)
        except (TypeError, ValueError):
            return 0.0

    def _market_data_engine(self) -> Any:
        """The market-data engine, from wherever this service actually holds it.

        `PreTradeRiskService` does NOT own one - its `__init__` takes only
        event_bus, position_repo, risk_engine, symbol_repo and account_repo. The engine
        hangs off the RISK engine:

            RiskEngine.__init__(..., market_data_engine=None)
            -> self.market_data_engine

        The first version of this looked only at `self.market_data_engine` and
        `self.engine`, which a real service never has, so the tick lookup always missed.
        Reads the direct attribute too, so a service or a test that sets one is still
        honoured.
        """
        for holder in (self, getattr(self, "risk_engine", None)):
            if holder is None:
                continue
            engine = getattr(holder, "market_data_engine", None)
            if engine is not None:
                return engine
            engine = getattr(holder, "engine", None)
            # `engine` on the risk engine is the RiskEngine itself, not a feed, so only
            # accept it when it actually exposes a tick lookup.
            if engine is not None and hasattr(engine, "get_latest_tick"):
                return engine
        return None

    async def _latest_tick(self, symbol_name: str) -> Any:
        """The engine's latest tick for a symbol, or None."""
        engine = self._market_data_engine()
        if engine is None:
            return None
        getter = getattr(engine, "get_latest_tick", None)
        if getter is None:
            return None
        try:
            result = getter(symbol_name)
            if hasattr(result, "__await__"):
                result = await result
            return result
        except Exception:                                  # noqa: BLE001
            # A missing feed must not turn into a crash on the order path; the global
            # freshness guard still applies where it is configured.
            return None

    @staticmethod
    def _tick_age_seconds(tick: Any, now: Any) -> Optional[float]:
        """Seconds since the tick's timestamp, or None if it carries no usable one."""
        stamp = None
        for attr in ("timestamp", "time", "ts"):
            stamp = getattr(tick, attr, None)
            if stamp is not None:
                break
        if stamp is None and isinstance(tick, dict):
            stamp = tick.get("timestamp") or tick.get("time")
        if stamp is None:
            return None
        try:
            if getattr(stamp, "tzinfo", None) is None:
                from datetime import timezone as _tz
                stamp = stamp.replace(tzinfo=_tz.utc)
            return max(0.0, (now - stamp).total_seconds())
        except (TypeError, ValueError):
            return None

    async def _check_holiday(self, symbol_name: str, now: Any) -> Optional[str]:
        """Return the holiday description when `now` falls on a configured holiday.

        MT5's request pipeline rejects with MT_RET_REQUEST_MARKET_CLOSED (10018).

        Uses the repository methods that ACTUALLY exist:
        ``get_holidays_for_symbol(symbol)`` on SQLAlchemyHolidayRepository, falling
        back to ``get_active_holidays(datetime)`` / ``get_all()``. The first version
        of this helper probed ``get_holidays`` / ``find_holidays``, neither of which
        exists anywhere, so it was silently dead code.

        The entity is ``core.domains.instruments.holiday.Holiday``: it carries
        description/mode/year/month/day/work_from/work_to/symbols and exposes the
        judgement directly as ``is_active_at(datetime)`` and
        ``applies_to_symbol(name)``. Those are called rather than re-derived.

        Fails OPEN on repository errors: a holiday lookup that cannot run must not
        stop the whole book from trading. It does log, because a silently ignored
        holiday is the bug this method exists to fix.
        """
        # The HOLIDAY repository, not `symbol_repo`. `symbol_repo.get_all()` returns
        # Symbols, and the entity checks below read `.month`/`.day`, which a Symbol does not
        # have - so the old fallback could only ever conclude "not a holiday" and the gate
        # was dead. If no holiday repository is wired the honest answer is "cannot tell",
        # which the caller treats as allowed and this method logs.
        repo = self.holiday_repo
        if repo is None:
            logger.warning(
                "no holiday repository is wired; the holiday trading gate cannot run"
            )
            return None

        # The VERIFIED signatures, so the right one is tried first:
        #   get_active_holidays(check_date: datetime)          <- what this needs
        #   get_holidays_for_symbol(symbol_name: str, year)    <- needs a year too
        #
        # The first version called `get_holidays_for_symbol(symbol_name)` with one argument,
        # raised a TypeError, and `return None`-ed WITHOUT trying the others - so wiring the
        # repository produced a logged error and still no enforcement. An exception in one
        # probe now continues to the next: "this repository cannot answer in that shape" is
        # not the same as "there is no holiday".
        year = getattr(now, "year", None) or datetime.now(_tz.utc).year
        holidays = None
        for name, args in (
            ("get_active_holidays", (now,)),
            ("get_holidays_for_symbol", (symbol_name, year)),
            ("get_all", ()),
        ):
            getter = getattr(repo, name, None)
            if not callable(getter):
                continue
            try:
                holidays = await getter(*args)
            except TypeError as exc:
                logger.warning(
                    "Holiday lookup (%s) could not be called for %s: %s; trying the next",
                    name, symbol_name, exc,
                )
                continue
            except Exception as exc:  # noqa: BLE001 - never fail-closed on an outage
                logger.warning("Holiday lookup (%s) for %s failed: %s", name, symbol_name, exc)
                return None
            if holidays is not None:
                break

        if not holidays:
            return None

        for entry in holidays:
            try:
                # The entity knows both questions; ask it, do not re-implement.
                if hasattr(entry, "applies_to_symbol") and not entry.applies_to_symbol(symbol_name):
                    continue
                if hasattr(entry, "is_active_at"):
                    if entry.is_active_at(now):
                        return str(getattr(entry, "description", None) or "holiday")
                    continue
                # Last resort for a duck-typed row: a plain date match.
                if getattr(entry, "month", None) == now.month and getattr(entry, "day", None) == now.day:
                    return str(getattr(entry, "description", None) or "holiday")
            except Exception:  # noqa: BLE001 - a malformed row is not a rejection
                continue
        return None

    def _check_stops_level(self, order: Order, symbol: Symbol, current_price: Price) -> bool:
        """Enforce MT5 StopsLevel: the minimum SL/TP distance, in POINTS.

        Source: MT5SDK-Doc ... IMTConSymbol/StopsLevel.md; rejection code is
        MT_RET_REQUEST_INVALID_STOPS (10016) per Return-Codes/Trade-Requests.md.

        `stops_level` is points, so the money distance is
        ``stops_level * Point`` (= ``symbol.tick_size``, the price-precision step - NOT
        ``mt5_tick_size``, which is the tick-alignment field and is zero on many
        symbols). A level of 0 means "no limit" in MT5, and is skipped.

        Only the ORDER's own SL/TP is judged; a missing price means there is
        nothing to measure against, and refusing on absence of a reference would
        re-implement the no-price check (which is separate and already above).
        """
        try:
            min_points = int(getattr(symbol, "stops_level", 0) or 0)
        except (TypeError, ValueError):
            min_points = 0
        if min_points <= 0:
            return True

        point = getattr(symbol, "tick_size", None)
        try:
            min_distance = Decimal(str(min_points)) * Decimal(str(point))
        except Exception:  # noqa: BLE001 - unknown point means we cannot judge
            return True
        if min_distance <= 0:
            return True

        try:
            reference = Decimal(str(getattr(current_price, "value", current_price)))
        except Exception:  # noqa: BLE001
            return True

        for level in (getattr(order, "price_sl", None), getattr(order, "price_tp", None)):
            if level is None:
                continue
            try:
                value = Decimal(str(getattr(level, "value", level)))
            except Exception:  # noqa: BLE001
                continue
            if value <= 0:
                continue
            if abs(value - reference) < min_distance:
                return False
        return True

    def _check_group_trade_flags(self, account: Account, order: Order, symbol: Symbol) -> bool:
        """Apply the group rule-engine flags that gate opening a position.

        Sources: MT5SDK-Doc .../Groups/IMTConGroup TradeFlags; the rejection codes are
        MT_RET_REQUEST_HEDGE_PROHIBITED (10046) and MT_RET_REQUEST_CLOSE_ONLY (10044).

        Each branch sets ``last_rejection_reason`` itself, so the caller rejects with
        a reason that names the actual rule rather than a generic message.
        """
        group = getattr(account, "group", None)
        if group is None:
            return True

        # Close-only: buys/sells that OPEN a position are refused. A closing deal
        # arrives as an OUT deal through ClosePositionHandler, not here, so any
        # order reaching pre-trade is an opening request.
        try:
            from core.domains.instruments.enums import TradeMode
        except Exception:  # noqa: BLE001
            TradeMode = None  # type: ignore[assignment]
        if TradeMode is not None and getattr(symbol, "trade_mode", None) == TradeMode.CLOSEONLY:
            self.last_rejection_reason = f"Only position closing is allowed for {symbol.name}"
            self.last_rejection_code = Retcode.CLOSE_ONLY
            return False

        # Hedge prohibition: refuse only when the trade would create an OPPOSITE
        # position on a symbol the account already holds. Refusing every order
        # would break the ordinary same-direction case, which is not what the flag
        # means.
        try:
            from core.domains.accounts.enums import TradeFlags
        except Exception:  # noqa: BLE001
            return True
        has_flag = getattr(group, "has_trade_flag", None)
        if not callable(has_flag):
            return True
        try:
            prohibited = bool(has_flag(TradeFlags.HEDGE_PROHIBIT))
        except Exception:  # noqa: BLE001
            return True
        if not prohibited:
            return True

        live = getattr(self, "_live_position_sides", {}).get(str(getattr(order, "symbol", "")), None)
        if not live:
            return True
        try:
            from core.domains.oms.enums import OrderType
        except Exception:  # noqa: BLE001
            return True
        opening_is_buy = getattr(order, "order_type", None) in (
            OrderType.BUY, OrderType.BUY_LIMIT, OrderType.BUY_STOP, OrderType.BUY_STOP_LIMIT,
        )
        if opening_is_buy and "SELL" in live:
            self.last_rejection_reason = f"Hedging is prohibited: {symbol.name} already has a SELL position"
            self.last_rejection_code = Retcode.HEDGE_PROHIBITED
            return False
        if (not opening_is_buy) and "BUY" in live:
            self.last_rejection_reason = f"Hedging is prohibited: {symbol.name} already has a BUY position"
            self.last_rejection_code = Retcode.HEDGE_PROHIBITED
            return False
        return True

    async def _check_order_and_position_limits(
        self, account: Account, symbol: Symbol, order: Order
    ) -> bool:
        """MT5 group limits: LimitOrders (10033), LimitPositions (10040), volume (10034).

        A limit of 0 means unlimited in MT5 and is skipped. Every gate is skipped
        when the repositories are not wired or the read fails - a limit that cannot
        be counted must not be treated as zero.
        """
        group = getattr(account, "group", None)
        if group is None:
            return True

        login = getattr(account, "login", None)
        try:
            login_key = int(login) if login is not None else None
        except (TypeError, ValueError):
            login_key = None

        # Pending/open order count - MT_RET_REQUEST_LIMIT_ORDERS (10033).
        try:
            limit_orders = int(getattr(group, "limit_orders", 0) or 0)
        except (TypeError, ValueError):
            limit_orders = 0
        # MT5 LimitOrders counts ORDERS; LimitPositions counts POSITIONS. This block
        # used the POSITION finder for both, so an account with 200 open positions
        # and no pending orders was refused for "too many orders", while 200 pending
        # orders and no positions was allowed.
        if limit_orders > 0 and login_key is not None:
            count_orders = await self._count_live_orders(login_key)
            if count_orders is not None and count_orders >= limit_orders:
                self.last_rejection_reason = (
                    f"Reached the limit on the number of orders for this account "
                    f"({count_orders}/{limit_orders})"
                )
                self.last_rejection_code = Retcode.LIMIT_ORDERS
                return False

        # Open-position count - MT_RET_REQUEST_LIMIT_POSITIONS (10040).
        try:
            limit_positions = int(getattr(group, "limit_positions", 0) or 0)
        except (TypeError, ValueError):
            limit_positions = 0
        if limit_positions > 0 and self.position_repo is not None and login_key is not None:
            try:
                count = await self._count_open_positions(login_key)
            except Exception as exc:  # noqa: BLE001
                logger.warning("Position-limit read failed for %s: %s", login_key, exc)
                count = None
            if count is not None and count >= limit_positions:
                self.last_rejection_reason = (
                    f"Reached the limit on the number of positions for this account "
                    f"({count}/{limit_positions})"
                )
                self.last_rejection_code = Retcode.LIMIT_POSITIONS
                return False

        # Populate the per-symbol side map so the hedge-prohibition check can see
        # the open book. One read, reused by _check_group_trade_flags.
        if self.position_repo is not None and login_key is not None:
            finder = getattr(self.position_repo, "get_by_account", None)
            if callable(finder):
                try:
                    rows = await finder(login_key) or []
                except Exception:  # noqa: BLE001 - the hedge check degrades to permissive
                    rows = []
                sides: Dict[str, set] = {}
                for pos in rows:
                    try:
                        if getattr(pos, "time_done", None) is not None:
                            continue
                        sym = str(getattr(pos, "symbol", "") or "")
                        raw_side = str(getattr(getattr(pos, "action", ""), "name", getattr(pos, "action", "")) or "")
                        if not sym or not raw_side:
                            continue
                        sides.setdefault(sym, set()).add(raw_side.upper())
                    except Exception:  # noqa: BLE001
                        continue
                self._live_position_sides = sides

        # Aggregate open volume - MT_RET_REQUEST_LIMIT_VOLUME (10034).
        try:
            limit_volume = Decimal(str(getattr(group, "limit_positions_volume", 0) or 0))
        except Exception:  # noqa: BLE001
            limit_volume = Decimal("0")
        if limit_volume > 0 and self.position_repo is not None and login_key is not None:
            finder = getattr(self.position_repo, "get_by_account", None)
            if callable(finder):
                try:
                    open_positions = await finder(login_key) or []
                except Exception as exc:  # noqa: BLE001
                    logger.warning("Volume-limit read failed for %s: %s", login_key, exc)
                    open_positions = None
                if open_positions is not None:
                    total = Decimal("0")
                    for pos in open_positions:
                        try:
                            vol = getattr(pos, "volume", None)
                            total += Decimal(str(getattr(vol, "value", vol)))
                        except Exception:  # noqa: BLE001
                            continue
                    # `order` is now a real parameter. It used to be an undefined name
                    # whose NameError this except swallowed, so `incoming` silently
                    # became 0 and the gate measured the EXISTING book against the
                    # cap - allowing unlimited additional volume to a client already
                    # at the limit.
                    incoming = None
                    try:
                        vol = getattr(order, "volume", None)
                        incoming = Decimal(str(getattr(vol, "value", vol)))
                    except Exception as exc:  # noqa: BLE001
                        logger.warning(
                            "Volume-limit gate could not read the incoming volume for %s: %s", login_key, exc)
                    if incoming is None:
                        # Cannot count -> do not invent a zero. The docstring already
                        # promises this; now the code keeps it.
                        return True
                    if total + incoming > limit_volume:
                        self.last_rejection_reason = (
                            f"Reached the volume limit for this account "
                            f"({total + incoming} > {limit_volume})"
                        )
                        self.last_rejection_code = Retcode.LIMIT_VOLUME
                        return False
        return True

    async def _count_live_orders(self, login: int) -> Optional[int]:
        """Count live PENDING ORDERS for a login, or None when it cannot be counted.

        MT5's group LimitOrders counts working ORDERS, not positions. The previous
        implementation counted positions for both group limits, so an account with no
        pending orders and 200 open positions was refused for "too many orders", while an
        account resting 200 pending orders and holding no positions was allowed.

        Falls back to the position count only when the order repository is absent, so a
        repository that CAN answer and reports zero is never second-guessed.
        """
        repo = getattr(self, "order_repo", None)
        finder = getattr(repo, "find_pending_orders", None)
        if callable(finder):
            try:
                pending = await finder(login) or []
            except Exception as exc:  # noqa: BLE001
                logger.warning("Pending-order count failed for %s: %s", login, exc)
                return None
            return sum(1 for o in pending if not getattr(o, "time_done", None))

        # No order repository wired: report the position count, which is what the old code
        # used for BOTH limits, so behaviour is unchanged for such a setup.
        return await self._count_open_positions(login)


    async def _count_open_positions(self, login: int) -> Optional[int]:
        """Count open positions for a login, or None when it cannot be counted."""
        finder = getattr(self.position_repo, "get_by_account", None)
        if callable(finder):
            positions = await finder(login) or []
            return sum(1 for p in positions if not getattr(p, "time_done", None))
        pager = getattr(self.position_repo, "find_page", None)
        if callable(pager):
            _rows, total = await pager(limit=1, offset=0, account_login=login)
            return int(total)
        return None

    def _check_symbol_permission(self, group: Optional[Group], symbol_name: str) -> bool:
        """Checks if the group permissions allow trading this symbol."""
        if not group:
            return True
        return group.is_symbol_allowed(symbol_name)

    def _check_volume_limits(
        self, volume: Volume, symbol: Symbol, account: Optional[Account] = None
    ) -> bool:
        """Volume against the SYMBOL limits AND the GROUP per-symbol overrides.

        R2: this read only `symbol.validate_volume(...)`, so a group restricting volume per
        symbol - MT5's normal way to cap one instrument for one client segment - had NO
        effect. A group override of `volume_max = 1.0` on EURUSD did not stop a 5-lot order.

        The TIGHTER bound wins, which is the safe direction: a group may restrict below the
        symbol, never widen above it.

        The symbol half delegates to `Symbol.validate_volume` deliberately - it is the rule
        `CreateOrderHandler` applies, and a second copy of it previously drifted.
        """
        ok, reason = symbol.validate_volume(volume.value)
        if not ok:
            self.last_rejection_reason = reason
            self.last_rejection_code = Retcode.INVALID_VOLUME
            return False

        group = getattr(account, "group", None) if account is not None else None
        if group is None:
            return True
        getter = getattr(group, "get_symbol_config", None)
        if not callable(getter):
            return True
        try:
            overrides = getter(symbol.name) or {}
        except Exception as exc:  # noqa: BLE001
            # A group that cannot be read is NOT permission to skip its caps.
            logger.error(
                "could not read the group symbol config for %s: %s; refused rather than "
                "checked against no group cap at all",
                symbol.name, exc,
            )
            self.last_rejection_reason = (
                "the group per-symbol limits could not be read"
            )
            self.last_rejection_code = Retcode.REQUEST_REJECT
            return False

        try:
            group_min = overrides.get("volume_min")
            group_max = overrides.get("volume_max")
            if group_min is not None and Decimal(str(group_min)) > 0:
                if volume.value < Decimal(str(group_min)):
                    self.last_rejection_reason = (
                        f"Volume {volume.value} below the group minimum "
                        f"{group_min} for {symbol.name}"
                    )
                    self.last_rejection_code = Retcode.INVALID_VOLUME
                    return False
            if group_max is not None and Decimal(str(group_max)) > 0:
                if volume.value > Decimal(str(group_max)):
                    self.last_rejection_reason = (
                        f"Volume {volume.value} above the group maximum "
                        f"{group_max} for {symbol.name}"
                    )
                    self.last_rejection_code = Retcode.INVALID_VOLUME
                    return False
        except (TypeError, ValueError, ArithmeticError) as exc:
            logger.error("unreadable group volume bounds for %s: %s", symbol.name, exc)
            self.last_rejection_reason = (
                "the group per-symbol volume limits are malformed"
            )
            self.last_rejection_code = Retcode.REQUEST_REJECT
            return False

        return True

    async def _check_margin_requirement(
        self,
        order: Order,
        account: Account,
        symbol: Symbol,
        price: Price,
    ) -> Optional[Decimal]:
        """Pre-trade initial margin check, using the MT5-accurate engine.

        MT5 checks INITIAL margin when opening a position and MAINTENANCE margin for
        positions already open; pending orders are always checked at initial. This is the
        opening path, so it uses initial.

        The calculation runs all four MT5 stages - basic, conversion to the deposit
        currency, the operation's rate multiplier, and aggregation - through
        core.domains.market_data.margin, which is where the formulas and MT5's own
        published worked examples are asserted. Nothing here re-derives a formula.

        Split in two (audit N4): `initial_requirement` answers "how much does this order
        need", `_available_margin_check` answers "can the account afford it". Order-lifecycle
        commands need the first without the second, and previously had no way to ask for it -
        which is why `modify_order` grew its own formula.
        """
        required = await self.initial_requirement(order, account, symbol, price)
        if required is None:
            return None
        return await self._available_margin_check(order, account, required)

    async def initial_requirement(
        self,
        order: Order,
        account: Account,
        symbol: Symbol,
        price: Price,
    ) -> Optional[Decimal]:
        """MT5 stages 1-3 for ONE order: how much margin it needs. No availability check.

        Public because the order-lifecycle commands must ASK the RMS for this number rather
        than re-derive it. `modify_order` previously computed
        `(price * volume * contract_size) / 100` and then scaled the existing reservation by
        the price ratio - wrong for Forex and Forex-no-leverage, whose margin has NO price
        term at all (audit N4: a 1.10 -> 1.20 modify moved a 1000 hold to 1090.91 where MT5
        leaves it at 1000). 99 of the 362 symbols in the live export use those two modes.

        Returns None when the requirement cannot be computed; callers treat that as a refusal.
        """
        from core.domains.market_data.margin import (
            MarginCalculationError,
            SymbolMarginSpec,
            apply_rate,
            basic_margin,
            convert_to_deposit,
        )

        order_type = order.order_type.value if hasattr(order.order_type, "value") else str(order.order_type)
        operation = order_type.upper()

        # 1. Symbol spec, then group overrides on top. MT5: "To avoid overriding the
        #    coefficient value for a group, leave the value set to Default" - so a None
        #    override means inherit, never zero.
        spec = SymbolMarginSpec.from_symbol(symbol)
        if account.group is not None:
            overrides = account.group.get_symbol_config(symbol.name)
            spec = self._apply_group_overrides(spec, overrides)

        # 2. Leverage resolves account -> group -> symbol cap, not
        #    min(group.default, group.max) which ignores both the account override and
        #    the per-symbol maximum.
        leverage = self._resolve_leverage(account, symbol)

        # 3. Stages 1-3. A market order with no price raises rather than defaulting to
        #    1.0 - that default understated JPY margin by ~150x.
        # Accepts a Price value object OR a raw number. Every existing caller passes a
        # Price, but assuming the shape turns a wiring mistake into an AttributeError
        # and an HTTP 500 - and a risk gate that crashes is worse than one that
        # rejects, because the caller cannot tell a bug from a business refusal.
        price_value = getattr(price, "value", price) if price is not None else None
        try:
            basic = basic_margin(spec, order.volume.value, price_value, leverage=leverage)
            converted = convert_to_deposit(
                basic,
                margin_currency=spec.margin_currency,
                deposit_currency=account.currency,
                side="BUY" if operation.startswith("BUY") else "SELL",
                rate_lookup=self._rate_lookup,
            )
            required = apply_rate(converted, spec, operation, maintenance=False)

            # N5: MT5 floating leverage is "an ADDITIONAL COEFFICIENT to the initial ...
            # margin values calculated in accordance with the symbol settings". The booked
            # margin applies it through RiskEngine; if the gate did not, the two would
            # disagree in exactly the way the two leverage resolvers did (R1).
            required = required * await self._initial_tier_rate(account, symbol.name)
        except MarginCalculationError as exc:
            # A margin requirement we cannot compute is a rejection, not an approval.
            # The previous code caught every exception here and fell back to a stored
            # free-margin figure, which approved trades on stale data.
            logger.warning(
                "margin check for order %s could not be computed: %s", order.ticket_id, exc
            )
            return None

        return required

    async def _initial_tier_rate(self, account: Account, symbol_name: str) -> Decimal:
        """The floating-leverage INITIAL coefficient for one symbol, or 1.

        Measured over the account's open positions through the SAME RiskEngine method the
        booking path uses, so the gate and the book read one tier table. Short-circuits on
        `profile is None` before touching the repository, so a group without tiers costs
        nothing. Every failure degrades to the NEUTRAL coefficient (1) rather than to a
        refusal: a tier table that cannot be read must not stop the book, and 1 is what MT5
        gives an instrument no rule matches.
        """
        engine = self.risk_engine
        helper = getattr(engine, "initial_tier_rate", None)
        if engine is None or not callable(helper) or self.position_repo is None:
            return Decimal("1")
        group = getattr(account, "group", None)
        if getattr(group, "leverage_profile", None) is None:
            return Decimal("1")
        try:
            positions = await self.position_repo.get_by_account(account.login) or []
        except Exception as exc:  # noqa: BLE001
            logger.warning(
                "floating-leverage measurement could not read positions for %s: %s; using "
                "the neutral coefficient", symbol_name, exc)
            return Decimal("1")
        try:
            return Decimal(str(helper(account, symbol_name, positions)))
        except Exception as exc:  # noqa: BLE001
            logger.warning(
                "floating-leverage coefficient unavailable for %s: %s; using the neutral "
                "coefficient", symbol_name, exc)
            return Decimal("1")

    async def required_margin_for(self, order: Order, account: Account, price: Price):
        """The initial margin `order` needs at `price`, resolved through this service.

        The entry point the order-lifecycle commands use instead of re-deriving a formula.
        Returns None when the symbol is unknown or the requirement cannot be computed, and
        callers MUST treat None as a refusal, never as zero.
        """
        symbol = None
        repo = self.symbol_repo
        if repo is not None:
            for name in ("find_by_name", "get_symbol"):
                getter = getattr(repo, name, None)
                if getter is None:
                    continue
                result = getter(order.symbol)
                if hasattr(result, "__await__"):
                    result = await result
                if result is not None:
                    symbol = result
                    break
        if symbol is None:
            logger.error(
                "required_margin_for: symbol %s is not configured; cannot cost order %s",
                order.symbol, getattr(order, "ticket_id", "?"))
            return None
        return await self.initial_requirement(order, account, symbol, price)

    async def _available_margin_check(
        self, order: Order, account: Account, required: Decimal
    ) -> Optional[Decimal]:
        """Stage 4 of the gate: is `required` covered? Returns it, or None to refuse.

        Deliberately SEPARATE from `initial_requirement`, so a caller that only needs the
        number (modify_order) does not also trigger an availability decision.

        NOTE ON PENDING ORDERS (audit R3): the snapshot below is built from POSITIONS only,
        and that is correct HERE - not an oversight. A resting pending keeps its
        `margin_reserved` hold for its whole life (nothing releases it until the order fills,
        is cancelled or expires), so `reserved_now` already carries every working order.
        Passing `orders` to `calculate_margin_level` as well would count each pending TWICE
        and refuse orders the account can afford. The booked `margin_used`, which has no
        reservation column to lean on, is the path that must include them - and does.
        """
        from core.domains.market_data.margin import available_margin

        reserved_now = (
            account.margin_reserved.amount
            if getattr(account, "margin_reserved", None) is not None
            else Decimal("0")
        )
        available = account.margin_free.amount - reserved_now
        if self.risk_engine is not None and self.position_repo is not None:
            try:
                open_positions = await self.position_repo.get_by_account(account.login)
                snapshot = self.risk_engine.calculate_margin_level(account, open_positions)
                # ^ positions only, on purpose - see the note on this method.
                # Conservative: a positive unrealised gain is not trusted to authorise a
                # new position, only a loss reduces availability. This is the rule
                # tfrmma/oms margin_monitor.hpp documents - a local estimate that has
                # drifted optimistic must not open trades.
                available = available_margin(
                    equity=snapshot.equity,
                    margin_used=snapshot.margin_used + reserved_now,
                    unrealized_pnl=snapshot.equity - account.balance.amount,
                    conservative=True,
                )
            except Exception as exc:  # noqa: BLE001 - but do NOT approve on failure
                logger.error(
                    "live margin snapshot failed for %s; rejecting rather than trusting "
                    "the stored free margin: %s",
                    account.login,
                    exc,
                )
                return None

        if required > available:
            logger.debug(
                "margin check failed for %s: required %s, available %s (reserved in-flight %s)",
                order.ticket_id,
                required,
                available,
                reserved_now,
            )
            return None
        return required

    def _resolve_leverage(self, account: Account, symbol: Symbol) -> int:
        """Delegate to the account's own resolver. There is ONE of these, on purpose.

        This used to be a second implementation, and it disagreed with the booking path by
        10x: it applied the group's ``leverage_max`` while ``Account.effective_leverage()``
        ignored it. The gate charged 100 where every booked figure used 1000 on the same
        account, so ``margin_used`` was understated and stop-out fired late or never.

        It is now a DELEGATION, which is the point: the value of the fix is that the gate
        and the book cannot drift, not which of the two numbers won.
        """
        resolver = getattr(account, "effective_leverage", None)
        if callable(resolver):
            try:
                return int(resolver(symbol))
            except TypeError:
                # An account object whose effective_leverage takes no argument.
                return int(resolver())

        # No resolver at all: derive from the group rather than inventing a number.
        # Returning 1 here would charge full notional margin, which is the safe direction
        # but a surprising figure to produce silently.
        fallback = []
        account_leverage = getattr(account, "leverage", None)
        if account_leverage and account_leverage > 0:
            fallback.append(int(account_leverage))
        margin = getattr(getattr(account, "group", None), "margin", None)
        for name in ("leverage_default", "leverage_max"):
            value = getattr(margin, name, 0) or 0
            if value > 0:
                fallback.append(int(value))
        return min(fallback) if fallback else 100

    def _apply_group_overrides(self, spec, overrides: dict):
        """Overlay a group's per-symbol overrides onto the symbol spec.

        An override value of None means "inherit from the symbol", which MT5 encodes on
        the wire as the string "default". It must never be read as zero: a zero margin
        rate means "no margin charged for this operation type", which is a real and
        dangerous setting, not an absent one.
        """
        from dataclasses import replace as _replace
        from decimal import Decimal as _Decimal

        rates = dict(spec.rates)
        changes = {}
        for key, value in (overrides or {}).items():
            if value is None:
                continue
            if key.startswith("margin_rate_initial_"):
                rates[key.replace("margin_rate_initial_", "initial_")] = _Decimal(str(value))
            elif key.startswith("margin_rate_maintenance_"):
                rates[key.replace("margin_rate_maintenance_", "maintenance_")] = _Decimal(str(value))
            # R8: `contract_size` and `margin_hedged` used to be handled here and could
            # NEVER fire - `GroupSymbolOverride` has no such fields, so both branches were
            # dead code that read like coverage. Removed.
            #
            # STATED LIMIT (corrected): only the two INITIAL MARKET rates
            # (`margin_rate_initial_buy` / `_sell`) can actually arrive here, because those
            # are the only two fields `GroupSymbolOverride` declares
            # (core/domains/accounts/value_objects.py) and the only two
            # `Group.get_symbol_config` returns. The `margin_rate_maintenance_*` branch above
            # is therefore reachable only if the entity grows those fields - it is kept so
            # that adding them needs no change here, not because it fires today.
            #
            # MT5 exposes 16 rate slots; 14 of them (both maintenance market rates and all
            # eight pending rates) have no per-group override at all. Consequence worth
            # knowing: `resolve_rate` inherits a ZERO maintenance rate from the initial one,
            # so a group override on `initial_buy` also changes the maintenance charge for
            # open positions on that symbol. That is MT5's inheritance rule, not a bug, but
            # it means an "initial only" override is not initial only in effect.
        return _replace(spec, rates=rates, **changes)

    def _rate_lookup(self, from_currency: str, to_currency: str, side: str):
        """Currency conversion for margin, delegating to the risk engine.

        Returns None when no rate is available, which convert_to_deposit turns into a
        rejection. Never returns 1.0 as a guess.

        `market_feed` and `side` are now PASSED. They were omitted, and without a feed
        `RiskEngine.get_conversion_rate` falls back to its own `market_data_engine` - which
        is None on the risk engine the container hands this service. Every non-trivial
        conversion therefore failed, and the caller reported it as "Insufficient free
        margin", which is a business refusal rather than the wiring fault it was.

        This matters for the normal case, not an exotic one: MT5 computes margin in the
        symbol's MARGIN currency and converts to the client's deposit currency, and
        ETHUSD/BTCUSD carry CurrencyMargin = ETH/BTC in the live export. Without this, no
        crypto symbol could be margined on a USD account.

        `side` follows MT5: "The Ask price is used for buy deals, and the Bid price is
        used for sell deals." Passing it avoids the function's own BUY default for sells.
        """
        if self.risk_engine is None:
            return None
        getter = getattr(self.risk_engine, "get_conversion_rate", None)
        if getter is None:
            return None
        feed = self._market_feed_for_conversion()
        # R21: inspect the SIGNATURE rather than catching TypeError.
        #
        # The previous form called `getter(from, to, feed, side)` and, on ANY TypeError,
        # retried `getter(from, to)`. A TypeError raised INSIDE the lookup is
        # indistinguishable from "this engine takes 2 arguments", so a genuine rate
        # failure silently retried WITHOUT `side` - converting at the wrong side of the
        # spread. The signature says which call is correct; an exception cannot.
        try:
            import inspect as _inspect

            _params = _inspect.signature(getter).parameters
            _takes_four = len(_params) >= 4 or any(
                prm.kind == _inspect.Parameter.VAR_POSITIONAL for prm in _params.values()
            )
        except (TypeError, ValueError):
            # Un-introspectable (a C function, a partial): the 4-arg call is what the
            # engine this service is built with takes.
            _takes_four = True

        try:
            if _takes_four:
                return getter(from_currency, to_currency, feed, side)
            return getter(from_currency, to_currency)
        except TypeError as exc:
            # Reached only for a genuinely mis-signatured engine, and REPORTED - never a
            # silent retry that drops `side`.
            logger.error(
                "risk engine get_conversion_rate(%s -> %s) rejected the call: %s",
                from_currency, to_currency, exc,
            )
            return None
        except Exception:  # noqa: BLE001 - an unresolvable rate is a refusal, not a crash
            return None

    def _market_feed_for_conversion(self) -> Any:
        """A market-data engine to price a conversion with, or None.

        Prefers anything already held by the service or its risk engine, then the
        process-wide provider the running API registers. Returns None rather than
        raising: an absent feed must degrade to "no rate", which the caller already
        handles as a rejection, not crash the order path.
        """
        for holder in (self, getattr(self, "risk_engine", None)):
            if holder is None:
                continue
            for attr in ("market_data_engine", "market_feed", "feed"):
                candidate = getattr(holder, attr, None)
                if candidate is not None and hasattr(candidate, "get_latest_tick"):
                    return candidate
        try:
            from api.di_providers import get_market_data_engine

            engine = get_market_data_engine()
            if engine is not None and hasattr(engine, "get_latest_tick"):
                return engine
        except Exception:  # noqa: BLE001 - provider may not be registered (e.g. in tests)
            pass
        return None

    async def _publish_approval(self, order: Order) -> None:
        """Publishes OrderApprovedEvent.

        The payload carries the identifier under BOTH `order_id` and `ticket_id`.
        Risk published `ticket_id` while ExecutionOrchestrator read `order_id`, so the
        orchestrator logged "OrderApprovedEvent missing order_id" and returned - the
        approval and the execution never met. Carrying both is cheaper than picking a
        side, and `order_id` is the name the rest of the tree uses.
        """
        if not self.event_bus:
            return
        account_login = getattr(order, 'account_login', getattr(order, 'account_id', ''))
        event = OrderApproved(
            aggregate_id=order.ticket_id,
            payload={
                "order_id": order.ticket_id,
                "ticket_id": order.ticket_id,
                "account_login": account_login,
                "symbol": order.symbol,
                "volume": str(order.volume.value),
                "approved_at": order.updated_at.isoformat()
            }
        )
        await self.event_bus.publish(event)

    async def _publish_rejection(self, order: Order, reason: str) -> None:
        """Publishes OrderRejectedEvent."""
        if not self.event_bus:
            return
        account_login = getattr(order, 'account_login', getattr(order, 'account_id', ''))
        event = OrderRejected(
            aggregate_id=order.ticket_id,
            payload={
                "order_id": order.ticket_id,
                "ticket_id": order.ticket_id,
                "account_login": account_login,
                "reason": reason,
                "rejected_at": order.updated_at.isoformat()
            }
        )
        await self.event_bus.publish(event)
