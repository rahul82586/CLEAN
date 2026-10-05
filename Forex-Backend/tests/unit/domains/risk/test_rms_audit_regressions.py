"""Regression tests for the RMS audit (findings R1-R30, N1-N11).

Every test here fails against commit `2750b25` for the reason named in its docstring, and
uses the REAL domain entities and the REAL repositories wherever one can be built in
process. That is deliberate: the defects this guards survived the previous suite because the
doubles in it carried attributes the production objects do not have (`_Holiday.date`,
`_Symbol.swap_flags`, an async `find_by_name` where production passes a synchronous
ConfigCache view). A test that only passes against a fake is not a test.

Run: pytest tests/unit/domains/risk/test_rms_audit_regressions.py -q
"""
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from decimal import Decimal as D
from typing import Any, Dict, List, Optional

import pytest

from core.domains.accounts.account import Account, MARGIN_LEVEL_UNLIMITED
from core.domains.accounts.enums import MarginMode
from core.domains.accounts.group import Group
from core.domains.accounts.thresholds import (
    DEFAULT_MARGIN_CALL_LEVEL,
    DEFAULT_STOP_OUT_LEVEL,
)
from core.domains.accounts.value_objects import (
    GroupPermissions,
    GroupSymbolOverride,
    MarginProfile,
    Money,
)
from core.domains.common.value_objects import Price, Volume
from core.domains.instruments.enums import CalculationMode
from core.domains.instruments.holiday import Holiday
from core.domains.instruments.enums import HolidayMode
from core.domains.instruments.symbol import Symbol
from core.domains.market_data.margin import (
    Leg,
    MarginCalculationError,
    SymbolMarginSpec,
    basic_margin,
    calculate_account_margin,
    margin_level,
)
from core.domains.market_data.models import Tick
from core.domains.oms.entities.order import Order
from core.domains.oms.entities.position import Position
from core.domains.oms.enums import OrderState, OrderType, PositionAction
from core.domains.risk.engine import PositionValuationError, RiskEngine
from core.domains.risk.liquidation_service import LiquidationPlan, LiquidationService


# --------------------------------------------------------------------------
# builders — real entities, no attribute fakes
# --------------------------------------------------------------------------

def make_group(name="demo\\Standard", currency="USD", *, leverage_default=100,
               leverage_max=500, overrides=None, tiers=None) -> Group:
    g = Group(
        name=name,
        currency=currency,
        currency_digits=2,
        margin=MarginProfile(
            mode=MarginMode.RETAIL_HEDGED,
            leverage_default=leverage_default,
            leverage_max=leverage_max,
            margin_call_level=D("50"),
            stop_out_level=D("30"),
        ),
        permissions=GroupPermissions(allowed_symbols=["*"]),
        symbol_overrides=list(overrides or []),
    )
    if tiers is not None:
        g.mt5_extra = {"leverage_tiers": tiers}
        # the group parses its profile lazily from mt5_extra; touch the property once so a
        # malformed profile is a test failure here rather than a silent neutral rate later
        getattr(g, "leverage_profile", None)
    return g


def make_account(login=1, group=None, currency="USD", balance="100000", leverage=100,
                 credit="0") -> Account:
    a = Account(
        login=login,
        currency=currency,
        leverage=leverage,
        balance=Money(D(balance), currency),
        credit=Money(D(credit), currency),
        group=group,
    )
    a.equity = Money(D(balance), currency)
    a.margin_used = Money(D("0"), currency)
    a.margin_free = Money(D(balance), currency)
    a.margin_reserved = Money(D("0"), currency)
    return a


def make_symbol(name="EURUSD", mode=CalculationMode.FOREX, *, contract_size="100000",
                margin_currency="USD", quote="USD", **kw) -> Symbol:
    return Symbol(
        name=name,
        base_currency="EUR",
        quote_currency=quote,
        margin_currency=margin_currency,
        calc_mode=mode,
        contract_size=D(contract_size),
        tick_size=D("0.00001"),
        digits=5,
        **kw,
    )


class SyncSymbolRepo:
    """The shape RiskEngine requires: SYNCHRONOUS, like the ConfigCache view."""

    def __init__(self, *symbols):
        self.symbols = {s.name: s for s in symbols}

    def get_symbol(self, name):
        return self.symbols.get(name)

    def find_by_name(self, name):
        return self.symbols.get(name)


class StaticFeed:
    """Synchronous get_latest_tick, like the real MarketDataEngine."""

    def __init__(self, bid="1.10000", ask="1.10010"):
        self.bid, self.ask = D(bid), D(ask)

    def get_latest_tick(self, symbol):
        return Tick(symbol=symbol, bid=self.bid, ask=self.ask,
                    spread=self.ask - self.bid,
                    timestamp=datetime.now(timezone.utc), source="TEST")


def make_position(symbol, action, volume, price, login=1, pid=None, contract="100000"):
    return Position(
        position_id=pid or f"P-{symbol}-{action}-{volume}",
        account_login=login,
        symbol=symbol,
        action=PositionAction(action),
        volume=Volume(D(str(volume))),
        price_open=Price(D(str(price))),
        contract_size=D(contract),
    )


def make_pending(symbol, order_type, volume, price, login=1):
    return Order(
        account_login=login,
        symbol=symbol,
        order_type=OrderType[order_type],
        volume_initial=Volume(D(str(volume))),
        volume_current=Volume(D(str(volume))),
        price_order=Price(D(str(price))),
        state=OrderState.PLACED,
        contract_size=D("100000"),
        digits=5,
    )


def engine(*symbols, bid="1.10000", ask="1.10010") -> RiskEngine:
    return RiskEngine(symbol_repo=SyncSymbolRepo(*symbols),
                      market_data_engine=StaticFeed(bid, ask))


# --------------------------------------------------------------------------
# R1 — one leverage resolver
# --------------------------------------------------------------------------

@pytest.mark.parametrize("acct_lev,default,maximum,expected", [
    (1000, 100, 500, 500),   # the case that disagreed by 10x
    (None, 100, 500, 100),   # no account override -> group default
    (50, 100, 500, 50),      # below both: the account's own value wins
    (1000, 100, 0, 1000),    # no cap configured
    (None, 0, 0, 100),       # nothing configured at all
])
def test_r1_leverage_resolvers_agree(acct_lev, default, maximum, expected):
    """R1: the gate charged 100 while every booked figure used 1000 on the same account."""
    from application.services.risk_service import PreTradeRiskService

    group = make_group(leverage_default=default, leverage_max=maximum)
    account = make_account(group=group, leverage=acct_lev)
    service = PreTradeRiskService()
    symbol = make_symbol()

    assert account.effective_leverage() == expected
    assert service._resolve_leverage(account, symbol) == expected, (
        "the pre-trade gate and the booking path must resolve leverage identically, or "
        "margin_used and the requirement are computed on different numbers"
    )


# --------------------------------------------------------------------------
# R11 — one threshold definition
# --------------------------------------------------------------------------

def test_r11_thresholds_have_one_definition():
    """R11: five literals (80/50 vs 50/30) meant a group-less account stopped out at 50%."""
    profile = MarginProfile()
    assert profile.margin_call_level == DEFAULT_MARGIN_CALL_LEVEL == D("50")
    assert profile.stop_out_level == DEFAULT_STOP_OUT_LEVEL == D("30")

    eng = engine(make_symbol())
    account = make_account(group=None)
    assert eng._thresholds(account) == (D("50"), D("30")), (
        "the no-group fallback must be the shared constant, not a private literal"
    )


# --------------------------------------------------------------------------
# R3 / N5 / N6 — pending orders and floating leverage in the snapshot
# --------------------------------------------------------------------------

def test_r3_resting_pendings_are_charged_margin():
    """R3: `is_pending=True` had no production occurrence, so a working order cost nothing."""
    sym = make_symbol()
    eng = engine(sym)
    account = make_account(group=make_group())
    positions = [make_position("EURUSD", "BUY", 1, "1.10")]
    pendings = [make_pending("EURUSD", "BUY_LIMIT", 2, "1.09")]

    without = eng.calculate_margin_level(account, positions)
    with_ = eng.calculate_margin_level(account, positions, pendings)

    assert with_.margin_used > without.margin_used, "the pending contributed nothing"
    # 1 lot position = 100000/100 = 1000 ; 2 lots pending = 2000
    assert with_.margin_used - without.margin_used == D("2000.0")
    assert with_.margin_level < without.margin_level, (
        "more exposure must lower the margin level, or stop-out cannot see the pending"
    )


def test_r3_a_terminal_order_is_not_charged():
    """Only WORKING orders may be counted; a filled or cancelled one must not be."""
    sym = make_symbol()
    eng = engine(sym)
    account = make_account(group=make_group())
    positions = [make_position("EURUSD", "BUY", 1, "1.10")]

    done = make_pending("EURUSD", "BUY_LIMIT", 2, "1.09")
    done.state = OrderState.CANCELLED

    assert eng.calculate_margin_level(account, positions, [done]).margin_used == \
        eng.calculate_margin_level(account, positions).margin_used


def test_n11_an_unpriceable_pending_fails_closed():
    """N11: a pending that cannot be costed was skipped (zero margin) while a position
    in the same situation refused the whole calculation."""
    eng = engine(make_symbol())          # only EURUSD is configured
    account = make_account(group=make_group())
    orphan = make_pending("NOSUCH", "BUY_LIMIT", 1, "1.09")

    with pytest.raises(PositionValuationError):
        eng.calculate_margin_level(account, [], [orphan])


def test_n1_n6_floating_leverage_applies_per_symbol_through_the_engine():
    """N1: `_leverage_tier_result` raised NameError('ZERO') and was swallowed, so tiers
    never applied. N6: one symbol's coefficient was applied to the whole account."""
    aaa = make_symbol("AAAUSD", CalculationMode.CFD, contract_size="1")
    bbb = make_symbol("BBBUSD", CalculationMode.CFD, contract_size="1")
    eng = RiskEngine(symbol_repo=SyncSymbolRepo(aaa, bbb),
                     market_data_engine=StaticFeed("100", "100"))

    tiers = {"name": "p", "rules": [{
        "name": "triple_aaa", "symbols": "AAAUSD", "range_type": "volume_per_symbol",
        "tiers": [{"to": None, "initial_rate": "3", "maintenance_rate": "3"}],
    }]}
    account = make_account(group=make_group(tiers=tiers))

    legs_positions = [
        make_position("AAAUSD", "BUY", 1, "100", contract="1"),
        make_position("BBBUSD", "BUY", 1, "100", contract="1"),
    ]
    snapshot = eng.calculate_margin_level(account, legs_positions)
    untiered = eng.calculate_margin_level(make_account(group=make_group()), legs_positions)

    assert snapshot.margin_used > untiered.margin_used, (
        "the tier coefficient never reached the margin total (N1)"
    )
    # AAA: 1 lot * cs 1 * 100 = 100, tripled = 300. BBB untouched = 100.
    assert snapshot.margin_used == D("400"), (
        f"expected 300 (AAA tripled) + 100 (BBB untouched) = 400, got {snapshot.margin_used}"
    )


def test_n1_tier_order_does_not_change_the_answer():
    """N6: `for name in volumes: return ...` evaluated whichever symbol came first."""
    aaa = make_symbol("AAAUSD", CalculationMode.CFD, contract_size="1")
    bbb = make_symbol("BBBUSD", CalculationMode.CFD, contract_size="1")
    eng = RiskEngine(symbol_repo=SyncSymbolRepo(aaa, bbb),
                     market_data_engine=StaticFeed("100", "100"))
    tiers = {"name": "p", "rules": [{
        "name": "triple_aaa", "symbols": "AAAUSD", "range_type": "volume_per_symbol",
        "tiers": [{"to": None, "initial_rate": "3", "maintenance_rate": "3"}],
    }]}
    a1 = [make_position("AAAUSD", "BUY", 1, "100", contract="1"),
          make_position("BBBUSD", "BUY", 1, "100", contract="1")]
    a2 = list(reversed(a1))
    one = eng.calculate_margin_level(make_account(group=make_group(tiers=tiers)), a1)
    two = eng.calculate_margin_level(make_account(group=make_group(tiers=tiers)), a2)
    assert one.margin_used == two.margin_used, (
        "the tier result depended on iteration order, not on the book"
    )


def test_n5_the_stop_out_measurement_uses_the_same_tiers():
    """N5: `calculate_margin_level` applied the coefficient and `_maintenance_margin`
    did not, so the trigger and the selection loop disagreed."""
    sym = make_symbol("AAAUSD", CalculationMode.CFD, contract_size="1")
    eng = RiskEngine(symbol_repo=SyncSymbolRepo(sym), market_data_engine=StaticFeed("100", "100"))
    tiers = {"name": "p", "rules": [{
        "name": "r", "symbols": "*", "range_type": "volume",
        "tiers": [{"to": None, "initial_rate": "2", "maintenance_rate": "2"}],
    }]}
    account = make_account(group=make_group(tiers=tiers))
    positions = [make_position("AAAUSD", "BUY", 1, "100", contract="1")]

    snapshot = eng.calculate_margin_level(account, positions)
    maintenance = eng.maintenance_margin(account, positions)
    assert snapshot.margin_used == maintenance, (
        "the snapshot and the stop-out selection loop must measure the same requirement"
    )


# --------------------------------------------------------------------------
# C7 / C8 — the two aggregation defects in margin.py
# --------------------------------------------------------------------------

def _hedged_total(spec, legs, **kw):
    return calculate_account_margin(legs, specs={spec.name: spec}, deposit_currency="USD",
                                    rate_lookup=None, leverage=100, **kw)


def test_c7_covered_volume_keeps_the_symbol_formula():
    """C7: `hedged_spec` dropped tick_value/tick_size/face_value, so CFD-Index and Bond
    covered volume raised instead of computing."""
    idx = SymbolMarginSpec(name="IDX", contract_size=D("10"), calc_mode=3,
                           margin_currency="USD", margin_hedged=D("5"),
                           tick_value=D("1"), tick_size=D("0.1"))
    legs = [Leg(symbol="IDX", operation="BUY", volume=D("1"), price=D("100")),
            Leg(symbol="IDX", operation="SELL", volume=D("1"), price=D("100"))]
    r = _hedged_total(idx, legs)
    # covered 1 lot, contract size = MarginHedged 5, price 100, tick ratio 1/0.1 = 10
    assert r.covered["IDX"] == D("1") * D("5") * D("100") * D("10"), r.covered

    bond = SymbolMarginSpec(name="BOND", contract_size=D("1"), calc_mode=37,
                            margin_currency="USD", margin_hedged=D("1"),
                            face_value=D("1000"))
    legs_b = [Leg(symbol="BOND", operation="BUY", volume=D("1"), price=D("100")),
              Leg(symbol="BOND", operation="SELL", volume=D("1"), price=D("100"))]
    rb = _hedged_total(bond, legs_b)
    assert rb.covered["BOND"] == D("1") * D("1") * D("1000") * D("100") / D("100")


def test_c8_larger_leg_counts_a_pending_on_the_larger_side():
    """C8: the side filter matched only BUY/SELL, so pendings vanished and the `continue`
    skipped the pending loop. BUY 1.0 + BUY_LIMIT 0.5 returned 1000 where MT5 gives 1500."""
    spec = SymbolMarginSpec(name="EURUSD", contract_size=D("100000"), calc_mode=0,
                            margin_currency="USD", hedged_use_larger_leg=True)
    legs = [Leg(symbol="EURUSD", operation="BUY", volume=D("1"), price=D("1.10")),
            Leg(symbol="EURUSD", operation="BUY_LIMIT", volume=D("0.5"), price=D("1.09"),
                is_pending=True)]
    r = _hedged_total(spec, legs)
    assert r.total == D("1500.0"), (
        "the long side is 1.0 position + 0.5 pending = 1.5 lots = 1500 at 100x"
    )
    assert r.pending.get("EURUSD") == D("500.0")


def test_c8_larger_leg_honours_the_maintenance_flag():
    """C8: both `basic_margin` and `apply_rate` were hardcoded `maintenance=False`, so a
    stop-out on a larger-leg symbol was computed on INITIAL margin."""
    spec = SymbolMarginSpec(name="EURUSD", contract_size=D("1"), calc_mode=1,
                            margin_currency="USD", hedged_use_larger_leg=True,
                            margin_initial=D("200"), margin_maintenance=D("50"))
    legs = [Leg(symbol="EURUSD", operation="BUY", volume=D("1"), price=D("1.10"))]
    assert _hedged_total(spec, legs, maintenance=False).total == D("200")
    assert _hedged_total(spec, legs, maintenance=True).total == D("50")


def test_c8_the_two_methods_still_differ_where_mt5_says_they_should():
    """The pre-existing test asserted `larger <= basic`, which held only because the
    pending was dropped. With a pending on the SMALLER side the larger leg absorbs it."""
    spec_l = SymbolMarginSpec(name="EURUSD", contract_size=D("100000"), calc_mode=0,
                              margin_currency="USD", hedged_use_larger_leg=True)
    spec_b = SymbolMarginSpec(name="EURUSD", contract_size=D("100000"), calc_mode=0,
                              margin_currency="USD", hedged_use_larger_leg=False)
    legs = [Leg(symbol="EURUSD", operation="BUY", volume=D("1"), price=D("1.10")),
            Leg(symbol="EURUSD", operation="SELL", volume=D("0.5"), price=D("1.10"),
                is_pending=True)]
    larger = _hedged_total(spec_l, legs).total
    basic = _hedged_total(spec_b, legs).total
    assert larger == D("1000.0")      # long side 1.0 vs short side 0.5 -> the long side
    assert basic == D("1500.0")       # uncovered 0.5 (500) + pending 0.5 (500) ... + 500
    assert larger < basic


# --------------------------------------------------------------------------
# N4 — modify must not price-scale a Forex reservation
# --------------------------------------------------------------------------

class _AccRepo:
    def __init__(self, account):
        self.account = account
        self.calls: List[tuple] = []

    async def find_by_login(self, login, session=None):
        return self.account

    async def save(self, account, session=None):
        return account

    async def reserve_margin(self, login, amount, session=None):
        self.calls.append(("reserve", D(str(amount))))
        self.account.margin_reserved = Money(
            self.account.margin_reserved.amount + D(str(amount)), self.account.currency)
        return self.account.margin_reserved.amount

    async def release_margin(self, login, amount, session=None):
        self.calls.append(("release", D(str(amount))))
        self.account.margin_reserved = Money(
            max(D("0"), self.account.margin_reserved.amount - D(str(amount))),
            self.account.currency)
        return self.account.margin_reserved.amount


class _OrderRepo:
    def __init__(self, order):
        self.order = order

    async def find_by_id(self, oid, session=None):
        return self.order if self.order.ticket_id == oid else None

    async def save(self, order, session=None):
        return order


class _Bus:
    def __init__(self):
        self.events: List[str] = []

    async def publish(self, event):
        self.events.append(type(event).__name__)


class _AsyncSymbolRepo:
    """`record_deal` awaits its symbol lookup; `RiskEngine` does not. Provide both."""

    def __init__(self, *symbols):
        self.symbols = {s.name: s for s in symbols}

    async def find_by_name(self, name, session=None):
        return self.symbols.get(name)

    def get_symbol(self, name):
        return self.symbols.get(name)


@pytest.mark.parametrize("mode,old,new,expected_hold", [
    (CalculationMode.FOREX, "1.10", "1.20", "1000"),            # no price term
    (CalculationMode.FOREX_NO_LEVERAGE, "1.10", "1.20", "100000"),
])
def test_n4_modifying_a_forex_pending_does_not_move_its_reservation(mode, old, new, expected_hold):
    """N4: `old_margin * (new_price / old_price)` moved a hold MT5 leaves alone."""
    from application.commands.modify_order import ModifyOrderCommand, ModifyOrderHandler
    from application.services.risk_service import PreTradeRiskService

    sym = make_symbol(mode=mode, margin_currency="USD")
    group = make_group()
    account = make_account(group=group, balance="100000000")
    account.margin_free = Money(D("90000000"), "USD")
    order = make_pending("EURUSD", "BUY_LIMIT", 1, old)
    order.contract_size = D("100000")
    order.reserved_margin = D(expected_hold)

    acc_repo = _AccRepo(account)
    service = PreTradeRiskService(symbol_repo=SyncSymbolRepo(sym), account_repo=acc_repo)
    handler = ModifyOrderHandler(account_repo=acc_repo, order_repo=_OrderRepo(order),
                                 risk_service=service, event_bus=_Bus())

    asyncio.run(handler.handle(ModifyOrderCommand(
        ticket_id=order.ticket_id, account_login=1, new_price=D(new))))

    assert order.reserved_margin == D(expected_hold), (
        f"Forex margin has no price term, so a price modify must leave the hold at "
        f"{expected_hold}; got {order.reserved_margin}"
    )
    assert acc_repo.calls == [], f"no reservation should move, got {acc_repo.calls}"


def test_n4_modifying_a_cfd_pending_does_move_its_reservation():
    """The other half: a price-dependent mode MUST re-reserve."""
    from application.commands.modify_order import ModifyOrderCommand, ModifyOrderHandler
    from application.services.risk_service import PreTradeRiskService

    sym = make_symbol("OIL", mode=CalculationMode.CFD, contract_size="1000",
                      margin_currency="USD", quote="USD")
    account = make_account(group=make_group(), balance="100000000")
    account.margin_free = Money(D("90000000"), "USD")
    order = make_pending("OIL", "BUY_LIMIT", 1, "100")
    order.contract_size = D("1000")
    order.reserved_margin = D("100000")        # CalcMode 2 = 1 * 1000 * 100

    acc_repo = _AccRepo(account)
    service = PreTradeRiskService(symbol_repo=SyncSymbolRepo(sym), account_repo=acc_repo)
    handler = ModifyOrderHandler(account_repo=acc_repo, order_repo=_OrderRepo(order),
                                 risk_service=service, event_bus=_Bus())

    asyncio.run(handler.handle(ModifyOrderCommand(
        ticket_id=order.ticket_id, account_login=1, new_price=D("110"))))

    assert order.reserved_margin == D("110000"), order.reserved_margin
    assert acc_repo.calls == [("reserve", D("10000"))], acc_repo.calls


# --------------------------------------------------------------------------
# R2 — group per-symbol volume overrides
# --------------------------------------------------------------------------

def test_r2_a_group_volume_cap_is_enforced():
    """R2: `get_symbol_config` returned volume_min/max/limit and nothing read them."""
    from application.services.risk_service import PreTradeRiskService

    sym = make_symbol(volume_min=D("0.01"), volume_max=D("100"), volume_step=D("0.01"))
    group = make_group(overrides=[
        GroupSymbolOverride(symbol_pattern="EURUSD", volume_max=D("1.0")),
    ])
    account = make_account(group=group)
    service = PreTradeRiskService()

    assert service._check_volume_limits(Volume(D("5")), sym, account) is False
    assert service.last_rejection_reason and "group maximum" in service.last_rejection_reason
    assert service._check_volume_limits(Volume(D("0.5")), sym, account) is True


def test_r2_an_unreadable_group_override_refuses_rather_than_allows():
    """The override read must fail closed."""
    from application.services.risk_service import PreTradeRiskService

    class ExplodingGroup:
        def get_symbol_config(self, name):
            raise RuntimeError("config store down")

    sym = make_symbol(volume_min=D("0.01"), volume_max=D("100"), volume_step=D("0.01"))
    account = make_account()
    account.group = ExplodingGroup()
    service = PreTradeRiskService()
    assert service._check_volume_limits(Volume(D("1")), sym, account) is False


# --------------------------------------------------------------------------
# R10 — the holiday gate must read the HOLIDAY repository
# --------------------------------------------------------------------------

def test_r10_the_holiday_gate_runs_against_the_real_entity():
    """R10: `_check_holiday` probed `symbol_repo`, whose `get_all()` returns SYMBOLS, so
    the gate compared `Symbol.month` (absent) to the current month and always allowed."""
    from application.services.risk_service import PreTradeRiskService

    class RealHolidayRepo:
        async def get_active_holidays(self, when):
            return [Holiday(description="Christmas", mode=HolidayMode.ENABLED,
                            year=0, month=12, day=25, symbols=[])]

    class SymbolRepoOnly:
        async def get_all(self):
            return [make_symbol()]

    xmas = datetime(2026, 12, 25, 12, 0, tzinfo=timezone.utc)
    wired = PreTradeRiskService(holiday_repo=RealHolidayRepo())
    assert asyncio.run(wired._check_holiday("EURUSD", xmas)) == "Christmas"

    unwired = PreTradeRiskService(symbol_repo=SymbolRepoOnly())
    assert asyncio.run(unwired._check_holiday("EURUSD", xmas)) is None, (
        "a symbol repository must never be mistaken for a holiday source"
    )


def test_r10_a_symbol_specific_holiday_does_not_close_the_whole_book():
    from application.services.risk_service import PreTradeRiskService

    class Repo:
        async def get_active_holidays(self, when):
            return [Holiday(description="XMAS", mode=HolidayMode.ENABLED,
                            year=0, month=12, day=25, symbols=["GBPUSD"])]

    svc = PreTradeRiskService(holiday_repo=Repo())
    xmas = datetime(2026, 12, 25, 12, 0, tzinfo=timezone.utc)
    assert asyncio.run(svc._check_holiday("GBPUSD", xmas)) == "XMAS"
    assert asyncio.run(svc._check_holiday("EURUSD", xmas)) is None


# --------------------------------------------------------------------------
# R9 — limit_orders counts ORDERS, and the volume limit sees the new order
# --------------------------------------------------------------------------

class _PosRepo:
    def __init__(self, positions=None):
        self.positions = positions or []
        self.calls = 0

    async def get_by_account(self, login):
        self.calls += 1
        return list(self.positions)


class _OrdRepo:
    def __init__(self, orders=None):
        self.orders = orders or []

    async def find_pending_orders(self, login):
        return list(self.orders)


def test_r9_limit_orders_counts_working_orders_not_positions():
    """R9: `limit_orders` was enforced against the POSITION count."""
    from application.services.risk_service import PreTradeRiskService

    group = make_group()
    group.limit_orders = 1
    group.limit_positions = 0
    group.limit_positions_volume = D("0")
    account = make_account(group=group)

    # two resting pendings, no positions at all
    pendings = [make_pending("EURUSD", "BUY_LIMIT", 1, "1.09"),
                make_pending("EURUSD", "SELL_LIMIT", 1, "1.11")]
    svc = PreTradeRiskService(position_repo=_PosRepo([]), order_repo=_OrdRepo(pendings))
    ok = asyncio.run(svc._check_order_and_position_limits(
        account, make_symbol(), make_pending("EURUSD", "BUY_LIMIT", 1, "1.08")))
    assert ok is False, "one working order already exists and limit_orders is 1"
    assert "number of orders" in (svc.last_rejection_reason or "")


def test_r9_the_volume_limit_counts_the_incoming_order():
    """R9: `getattr(order, ...)` referenced a name that was not a parameter, and the
    NameError was swallowed by `except Exception`, so `incoming` was always 0."""
    from application.services.risk_service import PreTradeRiskService

    group = make_group()
    group.limit_orders = 0
    group.limit_positions = 0
    group.limit_positions_volume = D("5")
    account = make_account(group=group)

    svc = PreTradeRiskService(position_repo=_PosRepo([]))
    ok = asyncio.run(svc._check_order_and_position_limits(
        account, make_symbol(), make_pending("EURUSD", "BUY_LIMIT", 10, "1.09")))
    assert ok is False, "a flat account requesting 10 lots against a 5-lot cap must refuse"
    assert "volume limit" in (svc.last_rejection_reason or "")


# --------------------------------------------------------------------------
# R15 — the margin-level sentinel, everywhere
# --------------------------------------------------------------------------

def test_r15_a_flat_account_never_reports_level_zero():
    """R15: `compute_trading_state` returned "0.00" and manager UserGet returned 0 for a
    flat account. Zero is below every stop-out threshold."""
    from application.services.account_revaluation import compute_trading_state

    account = make_account(group=make_group(), balance="10000")
    state = compute_trading_state(account, [])
    assert D(state["margin_level"]) == MARGIN_LEVEL_UNLIMITED, state["margin_level"]
    assert D(state["margin_used"]) == D("0")

    account2 = make_account(group=make_group())
    account2.update_equity(Money(D("0"), "USD"))
    assert account2.margin_level == MARGIN_LEVEL_UNLIMITED
    assert margin_level(D("1000"), D("0")) == MARGIN_LEVEL_UNLIMITED


def test_r15_free_margin_honours_the_group_mode():
    """R15: four modes in the entity, one formula in the reservation SQL."""
    from core.domains.accounts.enums import FreeMarginMode

    for mode in FreeMarginMode:
        group = make_group()
        group.margin.free_margin_mode = mode
        account = make_account(group=group, balance="10000")
        account.margin_used = Money(D("1000"), "USD")
        account.update_equity(Money(D("500"), "USD"))
        if mode == FreeMarginMode.USE_PL:
            assert account.margin_free.amount == D("9500")     # 10000+500-1000
        elif mode == FreeMarginMode.NOT_USE_PL:
            assert account.margin_free.amount == D("9000")     # 10000-1000
        elif mode == FreeMarginMode.PROFIT:
            assert account.margin_free.amount == D("9500")     # profit counts
        elif mode == FreeMarginMode.LOSS:
            assert account.margin_free.amount == D("9000")     # only a loss would count


# --------------------------------------------------------------------------
# N2 / N3 — the liquidation plan
# --------------------------------------------------------------------------

def test_n3_the_plan_includes_broker_credit_in_equity():
    """N3: `current_equity = balance + floating` omitted credit, so a credit account was
    valued poorer than it is and the plan closed more positions than the level required."""
    sym = make_symbol()
    eng = engine(sym)
    svc = LiquidationService(risk_engine=eng)

    positions = [make_position("EURUSD", "BUY", 1, "1.10")]
    prices = {"EURUSD": Price(D("1.09000"))}

    poor = make_account(group=make_group(), balance="1000", credit="0")
    poor.margin_used = Money(D("1000"), "USD")
    rich = make_account(group=make_group(), balance="1000", credit="5000")
    rich.margin_used = Money(D("1000"), "USD")

    plan_poor = svc.calculate_liquidation_plan(poor, positions, prices, {})
    plan_rich = svc.calculate_liquidation_plan(rich, positions, prices, {})
    assert len(plan_rich.positions_to_close) <= len(plan_poor.positions_to_close), (
        "6000 of equity must not liquidate more than 1000 of equity"
    )


def test_n2_a_large_position_is_not_charged_an_average_share_of_margin():
    """N2: `_margin_freed_for` returned `margin_used / len(positions)`, reading neither the
    position nor how many were already selected."""
    big = make_symbol("BIGUSD", CalculationMode.CFD, contract_size="1000")
    small = make_symbol("SMLUSD", CalculationMode.CFD, contract_size="1")
    eng = RiskEngine(symbol_repo=SyncSymbolRepo(big, small),
                     market_data_engine=StaticFeed("100", "100"))
    svc = LiquidationService(risk_engine=eng)

    positions = [
        make_position("BIGUSD", "BUY", 10, "100", contract="1000"),   # huge requirement
        make_position("SMLUSD", "BUY", 1, "100", contract="1"),       # almost nothing
    ]
    account = make_account(group=make_group(), balance="100")
    account.margin_used = Money(D("1000100"), "USD")     # what those two really need
    prices = {"BIGUSD": Price(D("100")), "SMLUSD": Price(D("100"))}

    plan = svc.calculate_liquidation_plan(account, positions, prices, {})
    # closing BIG alone removes essentially all of the requirement, so the tiny leg must
    # NOT also be selected
    closed = [p.symbol for p in plan.positions_to_close]
    assert closed == ["BIGUSD"], (
        f"a flat average per position over-liquidates; planned {closed}"
    )


def test_r4_the_plan_does_not_mutate_the_positions_it_is_given():
    """R4: the planner called `position.update_unrealized_pnl(...)`, writing a possibly
    unconverted profit into the entity that `_close_position` then books to the balance."""
    sym = make_symbol("USDJPY", quote="JPY", margin_currency="JPY")
    eng = RiskEngine(symbol_repo=SyncSymbolRepo(sym),
                     market_data_engine=StaticFeed("150", "150.01"))
    svc = LiquidationService(risk_engine=eng)

    position = make_position("USDJPY", "BUY", 1, "140")
    position.profit = Money(D("0"), "USD")
    before = position.profit.amount
    account = make_account(group=make_group(), balance="10000")
    account.margin_used = Money(D("1000"), "USD")

    svc.calculate_liquidation_plan(account, [position], {"USDJPY": Price(D("150"))}, {})
    assert position.profit.amount == before, "the planner must not write to the position"


# --------------------------------------------------------------------------
# C12 — deal money must be in the account's currency
# --------------------------------------------------------------------------

def test_c12_a_non_usd_account_with_commission_books_the_fill():
    """C12: `Deal(commission=Money(..., "USD"))` then `balance + commission` raised
    "Cannot add money with different currencies" AFTER the order was saved FILLED."""
    from application.commands.record_deal import RecordDealCommand, RecordDealHandler
    from core.domains.oms.enums import DealType
    sys_path_harness()

    from tests.integration.trading_harness import (  # noqa: E402
        InMemoryAccountRepository, InMemoryDealRepository, InMemoryOrderRepository,
        InMemoryPositionRepository, InMemorySymbolRepository, make_eurusd,
    )
    from infrastructure.messaging.inprocess_event_bus import InProcessEventBus

    group = make_group(currency="EUR")
    account = make_account(login=900001, group=group, currency="EUR", balance="10000")
    acc_repo = InMemoryAccountRepository()
    acc_repo.accounts[900001] = account
    order_repo = InMemoryOrderRepository()
    order = make_pending("EURUSD", "BUY", 1, "1.10", login=900001)
    order.account_login = 900001
    order.state = OrderState.PLACED
    order.contract_size = D("100000")
    asyncio.run(order_repo.save(order))

    handler = RecordDealHandler(
        order_repo=order_repo, account_repo=acc_repo,
        position_repo=InMemoryPositionRepository(), event_bus=InProcessEventBus(),
        symbol_repo=_AsyncSymbolRepo(make_eurusd("EURUSD")), market_feed=StaticFeed(),
        deal_repo=InMemoryDealRepository(),
    )

    deal = asyncio.run(handler.execute(RecordDealCommand(
        order_id=order.ticket_id, account_login=900001, symbol="EURUSD",
        volume=D("1"), price=D("1.10"), deal_type=DealType.BUY,
        commission_amount=D("7"), swap_amount=D("0"), profit=D("0"))))

    assert deal.commission.currency == "EUR", deal.commission.currency
    after = asyncio.run(acc_repo.find_by_login(900001))
    assert after.balance.currency == "EUR"
    assert after.margin_used.amount > D("0"), "margin must be recomputed, not left stale"
    saved = asyncio.run(order_repo.find_by_id(order.ticket_id))
    assert saved.state == OrderState.FILLED


def sys_path_harness():
    import os, sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))))
    if root not in sys.path:
        sys.path.insert(0, root)


# --------------------------------------------------------------------------
# R5 — reservations must not be stranded
# --------------------------------------------------------------------------

def test_r5_cancelling_a_pending_releases_its_exact_hold():
    """R5: cancel recomputed `price*volume*contract/100` and edited `margin_used` instead
    of releasing `margin_reserved`."""
    from application.commands.cancel_order import CancelOrderCommand, CancelOrderHandler
    from application.services.risk_service import PreTradeRiskService

    account = make_account(group=make_group())
    account.margin_reserved = Money(D("750"), "USD")
    account.margin_used = Money(D("1000"), "USD")
    account.margin_free = Money(D("9000"), "USD")
    order = make_pending("EURUSD", "BUY_LIMIT", 1, "1.09")
    order.reserved_margin = D("750")

    acc_repo = _AccRepo(account)
    bus = _Bus()
    handler = CancelOrderHandler(account_repo=acc_repo, order_repo=_OrderRepo(order),
                                 risk_service=PreTradeRiskService(account_repo=acc_repo),
                                 event_bus=bus)
    asyncio.run(handler.handle(CancelOrderCommand(ticket_id=order.ticket_id, account_login=1)))

    assert acc_repo.calls == [("release", D("750"))], acc_repo.calls
    assert order.reserved_margin == D("0")
    assert account.margin_used.amount == D("1000"), "cancel must not invent a margin_used"
    assert account.margin_free.amount == D("9000"), "cancel must not invent a margin_free"
    assert "OrderCancelled" in bus.events


def test_r5_expiring_a_pending_releases_its_hold():
    """R5: `expiration_worker` cancelled and saved, and never called release_margin."""
    from application.workers.expiration_worker import ExpirationWorker

    order = make_pending("EURUSD", "BUY_LIMIT", 1, "1.09")
    order.reserved_margin = D("400")
    order.time_expiration = datetime(2020, 1, 1, tzinfo=timezone.utc)

    class Repo:
        async def find_pending_orders(self, login):
            return [order]

        async def find_expired_orders(self, before):
            return [order]

        async def save(self, o, session=None):
            return o

    account = make_account(group=make_group())
    account.margin_reserved = Money(D("400"), "USD")
    acc_repo = _AccRepo(account)
    bus = _Bus()
    worker = ExpirationWorker(order_repo=Repo(), event_bus=bus, account_repo=acc_repo)
    assert worker.account_repo is acc_repo, (
        "N13: the release reads self.account_repo, which the constructor used never to set, "
        "so expiry logged a warning and stranded the hold"
    )
    asyncio.run(worker.sweep_once(datetime(2026, 1, 1, tzinfo=timezone.utc)))
    assert acc_repo.calls == [("release", D("400"))], acc_repo.calls
    assert order.reserved_margin == D("0")
    assert "OrderCancelled" in bus.events


# --------------------------------------------------------------------------
# H3 / B5 — the liquidation event must report what it closed
# --------------------------------------------------------------------------

def test_b5_position_closed_reports_the_volume_it_closed():
    """H3: `position.volume` was zeroed BEFORE the PositionClosed payload read it, so every
    liquidation announced `volume_closed: 0`."""
    import inspect
    from application.workers import liquidation_worker as lw

    src = inspect.getsource(lw.LiquidationWorker._close_position)
    zero_at = src.index("position.volume = Volume(Decimal('0'))")
    payload_at = src.index('"volume_closed"')
    capture_at = src.index("closed_volume = position.volume.value")
    assert capture_at < zero_at < payload_at, (
        "the closed volume must be captured before the position is zeroed, and the payload "
        "must read the captured value"
    )
    assert "str(closed_volume)" in src


# --------------------------------------------------------------------------
# R7 — no fabricated identity
# --------------------------------------------------------------------------

def test_r7_an_unloadable_account_is_refused_not_invented():
    """R7: a lookup failure produced a funded 10,000 USD account with no group, which
    `evaluate_margin_state` can never stop out."""
    import inspect
    from api.auth import dependencies as dep

    src = inspect.getsource(dep.get_current_user)
    # strip comments, so the assertions test the CODE and not the prose that explains it
    code = "\n".join(l for l in src.splitlines() if not l.strip().startswith("#"))
    assert "10000" not in code, "no fabricated balance may remain"
    assert 'payload.get("sub", ' not in code, "no default login may remain"
    assert "Account(" not in code, "the dependency must not construct an Account at all"
    assert code.count("HTTP_503_SERVICE_UNAVAILABLE") >= 2, (
        "an outage and a missing repository must both refuse"
    )
    assert "except Exception: pass" not in code, "the blacklist must fail closed"


def test_r7_a_group_less_account_cannot_be_stopped_out_is_a_known_hazard():
    """Documents WHY R7 matters: `evaluate_margin_state` returns [] with no group."""
    account = make_account(group=None)
    account.margin_used = Money(D("1000"), "USD")
    account.equity = Money(D("100"), "USD")
    account.recompute_margin_level()
    assert account.margin_level < D("30")
    assert account.evaluate_margin_state() == [], (
        "with no group there is no threshold, so nothing fires - the reason a fabricated "
        "account is unacceptable"
    )


# --------------------------------------------------------------------------
# N8 — the reservation sweep must exist AND be started
# --------------------------------------------------------------------------

def test_n8_the_sweep_releases_a_terminal_order_and_leaves_a_working_one():
    """N8: `reservation_sweep.py` was written (296 lines) with zero callers, so the
    recovery net `margin_reservation.py:29-31` promises did not exist."""
    from application.workers.reservation_sweep import ReservationSweep

    done = make_pending("EURUSD", "BUY_LIMIT", 1, "1.09")
    done.state = OrderState.CANCELLED
    done.reserved_margin = D("250")
    live = make_pending("EURUSD", "SELL_LIMIT", 1, "1.11")
    live.state = OrderState.PLACED
    live.reserved_margin = D("300")

    class Repo:
        async def find_by_state_in(self, states):
            return [done, live]

    account = make_account(group=make_group())
    account.margin_reserved = Money(D("550"), "USD")
    acc_repo = _AccRepo(account)

    sweep = ReservationSweep(order_repo=Repo(), account_repo=acc_repo)
    released = asyncio.run(sweep.sweep_once())

    assert released == 1, released
    assert acc_repo.calls == [("release", D("250"))], (
        f"only the TERMINAL order's hold may be freed; got {acc_repo.calls}"
    )
    assert done.reserved_margin == D("0")
    assert live.reserved_margin == D("300"), "a working order's hold must never be swept"


def test_n8_the_server_actually_starts_the_sweep():
    """Writing a worker is not wiring it. This is the assertion that was missing for
    `reservation_sweep`, `coalesce_seconds` and `order_repo`."""
    import inspect
    import api.main as main

    src = inspect.getsource(main)
    assert "ReservationSweep(" in src, "the reservation sweep is never constructed"
    assert "reservation_sweep.start()" in src, "the reservation sweep is never started"
    assert "reservation_sweep.stop()" in src, "the reservation sweep is never stopped"

    from application.di import market_data_setup, trading_setup

    md = inspect.getsource(market_data_setup.build_tick_margin_pipeline)
    assert "coalesce_seconds=" in md, "the tick coalescing window is never passed"

    ts = inspect.getsource(trading_setup.build_trading_stack)
    assert "order_repo=" in ts, (
        "R9: without this the shared risk service counts POSITIONS for group LimitOrders"
    )
    assert "holiday_repo=" in ts, "R10: the holiday gate needs its own repository"
