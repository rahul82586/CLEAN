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
        account_repo: Optional[Any] = None
    ):
        self.event_bus = event_bus
        self.position_repo = position_repo
        self.risk_engine = risk_engine
        self.symbol_repo = symbol_repo
        self.account_repo = account_repo
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

            # 4a. Holiday Check.
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
            if not self._check_volume_limits(order.volume, symbol):
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
            if not await self._check_order_and_position_limits(live_account, symbol):
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
        repo = self.symbol_repo
        if repo is None:
            return None

        holidays = None
        for name, args in (
            ("get_holidays_for_symbol", (symbol_name,)),
            ("get_active_holidays", (now,)),
            ("get_all", ()),
        ):
            getter = getattr(repo, name, None)
            if not callable(getter):
                continue
            try:
                holidays = await getter(*args)
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

    async def _check_order_and_position_limits(self, account: Account, symbol: Symbol) -> bool:
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
        if limit_orders > 0 and self.position_repo is not None and login_key is not None:
            finder = getattr(self.position_repo, "get_by_account", None)
            if callable(finder):
                try:
                    open_positions = await finder(login_key) or []
                except Exception as exc:  # noqa: BLE001
                    logger.warning("Order-limit read failed for %s: %s", login_key, exc)
                    open_positions = None
                if open_positions is not None and len(open_positions) >= limit_orders:
                    self.last_rejection_reason = (
                        f"Reached the limit on the number of orders for this account "
                        f"({len(open_positions)}/{limit_orders})"
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
                    incoming = Decimal("0")
                    try:
                        vol = getattr(order, "volume", None)
                        incoming = Decimal(str(getattr(vol, "value", vol)))
                    except Exception:  # noqa: BLE001
                        incoming = Decimal("0")
                    if total + incoming > limit_volume:
                        self.last_rejection_reason = (
                            f"Reached the volume limit for this account "
                            f"({total + incoming} > {limit_volume})"
                        )
                        self.last_rejection_code = Retcode.LIMIT_VOLUME
                        return False
        return True

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

    def _check_volume_limits(self, volume: Volume, symbol: Symbol) -> bool:
        """Validates volume against the symbol's min / max / step.

        Delegates to Symbol.validate_volume, which is the same rule
        CreateOrderHandler already applied a few lines earlier. This was a second
        implementation of it, and the two disagreed: this one compared against
        volume_min / volume_max unconditionally, so a symbol whose limits came back as 0
        from the database rejected every order, and it called is_valid_step(0) which
        raised decimal.InvalidOperation rather than returning a verdict.
        """
        ok, _reason = symbol.validate_volume(volume.value)
        return ok

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
        """
        from core.domains.market_data.margin import (
            MarginCalculationError,
            SymbolMarginSpec,
            apply_rate,
            basic_margin,
            convert_to_deposit,
            available_margin,
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
        price_value = price.value if price is not None else None
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
        except MarginCalculationError as exc:
            # A margin requirement we cannot compute is a rejection, not an approval.
            # The previous code caught every exception here and fell back to a stored
            # free-margin figure, which approved trades on stale data.
            logger.warning(
                "margin check for order %s could not be computed: %s", order.ticket_id, exc
            )
            return None

        # 4. Available margin. Use the live snapshot when we can build one, and treat a
        #    failure to build it as a rejection rather than silently degrading to a
        #    cached number. In-flight reservations (M6) count against availability in
        #    BOTH paths: a second concurrent order must see the first one's hold
        #    whether or not it has filled yet.
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
        """Account override, then group, then the symbol cap. Never zero.

        MT5 applies the most restrictive of these. The previous code used
        min(group.leverage_default, group.leverage_max), which ignored the account's own
        override entirely.
        """
        candidates = []
        account_leverage = getattr(account, "leverage", None)
        if account_leverage and account_leverage > 0:
            candidates.append(int(account_leverage))
        group = getattr(account, "group", None)
        if group is not None:
            default = getattr(group.margin, "leverage_default", 0) or 0
            maximum = getattr(group.margin, "leverage_max", 0) or 0
            if default > 0:
                candidates.append(int(default))
            if maximum > 0:
                candidates.append(int(maximum))
        symbol_max = getattr(symbol, "leverage_max", 0) or 0
        if symbol_max > 0:
            candidates.append(int(symbol_max))
        if not candidates:
            return 1
        return min(candidates)

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
            elif key == "contract_size":
                changes["contract_size"] = _Decimal(str(value))
            elif key == "margin_hedged":
                changes["margin_hedged"] = _Decimal(str(value))
        return _replace(spec, rates=rates, **changes)

    def _rate_lookup(self, from_currency: str, to_currency: str, side: str):
        """Currency conversion for margin, delegating to the risk engine.

        Returns None when no rate is available, which convert_to_deposit turns into a
        rejection. Never returns 1.0 as a guess.
        """
        if self.risk_engine is None:
            return None
        getter = getattr(self.risk_engine, "get_conversion_rate", None)
        if getter is None:
            return None
        try:
            return getter(from_currency, to_currency)
        except Exception:  # noqa: BLE001 - an unresolvable rate is a rejection
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
