"""Regression tests for the open-items round: H8 (FORTS), M18 (calc-mode validation), C11a.

Every test here fails against `main` @ ce26251 for the reason in its docstring.
"""
from __future__ import annotations

from decimal import Decimal as D

import pytest
from fastapi import HTTPException

from core.domains.market_data.margin import (
    EXCHANGE_FUTURES_FORTS,
    SymbolMarginSpec,
    MarginCalculationError,
    _MOEX_GATEWAY_REQUIRED_CALC_MODES,
    _forts_margin,
)


# --------------------------------------------------------------------------
# H8 — MT5's own worked example, Basic.md:224-252
#
#   Position Buy 3.00 Si-6.18 @ 73640 ; Clearing (settlement) price 73638
#   InitialMarginBuy 7665.41 ; InitialMarginSell 7739.59
#   Tick value 1 ; Tick size 1 ; Margin currency rate 0
#
# Basic.md:220 states where those two live:
#   "InitialMarginBuy is written to the 'Initial margin' field, InitialMarginSell is
#    written to the 'Maintenance Margin' field in symbol properties."
# --------------------------------------------------------------------------

def _si_spec():
    return SymbolMarginSpec(
        name="Si-6.18", contract_size=D("1"), calc_mode=EXCHANGE_FUTURES_FORTS,
        margin_currency="RUB",
        margin_initial=D("7665.41"),        # InitialMarginBuy
        margin_maintenance=D("7739.59"),    # InitialMarginSell
        tick_value=D("1"), tick_size=D("1"),
        settlement_price=D("73638"), margin_currency_rate=D("0"),
    )


def test_h8_forts_buy_side_matches_mt5s_published_arithmetic():
    """MarginPos(buy) = 3*(7665.41 + (73640-73638)*1/1) = 23002.23, and it beats the
    negative sell side, so MAX() is 23002.23."""
    assert _forts_margin(_si_spec(), D("3"), D("73640"), side="BUY") == D("23002.23")


def test_h8_forts_sell_side_uses_initial_margin_sell_not_buy():
    """The defect: both sides used `margin_initial`.

    For a SHORT position the sell side wins, so the wrong constant changes the answer:
      buggy   3 * (7665.41 - 2) = 22990.23
      correct 3 * (7739.59 - 2) = 23212.77
    MT5's example uses different buy and sell values precisely because they differ.
    """
    got = _forts_margin(_si_spec(), D("3"), D("73640"), side="SELL")
    assert got == D("23212.77"), (
        f"the sell side must use InitialMarginSell (the Maintenance Margin field); "
        f"got {got}, which is the InitialMarginBuy answer 22990.23"
    )
    assert got != D("22990.23")


def test_h8_forts_without_a_settlement_price_refuses_and_says_why():
    """No MOEX gateway means no session settlement price; the error must say so rather
    than produce an arbitrary number."""
    spec = SymbolMarginSpec(
        name="Si-6.18", contract_size=D("1"), calc_mode=EXCHANGE_FUTURES_FORTS,
        margin_currency="RUB", tick_value=D("1"), tick_size=D("1"),
    )
    with pytest.raises(MarginCalculationError) as exc:
        _forts_margin(spec, D("1"), D("73640"))
    msg = str(exc.value)
    assert "MOEX" in msg, msg
    assert "settlement" in msg.lower(), msg


def test_h8_the_refusal_set_covers_every_exchange_calc_mode():
    """32-39 are the modes whose inputs come from an exchange gateway, not from symbol
    configuration."""
    assert _MOEX_GATEWAY_REQUIRED_CALC_MODES == frozenset({32, 33, 34, 35, 36, 37, 38, 39})


# --------------------------------------------------------------------------
# H8 / M18 — configuration-time refusal
# --------------------------------------------------------------------------

@pytest.mark.parametrize("mode", [32, 33, 34, 35, 36, 37, 38, 39])
def test_h8_exchange_calc_modes_are_refused_at_configuration_time(mode):
    """MT5, Basic.md:254: "The Exchange FORTS Futures mode must only be used together with
    the MOEX Derivatives Gateway. Otherwise the margin requirements calculation results may
    be unpredictable." This deployment has no such gateway, and the live 362-symbol export
    contains no exchange symbol at all."""
    from api.routers.admin.skeletons import _reject_unsupported_calc_mode

    with pytest.raises(HTTPException) as exc:
        _reject_unsupported_calc_mode(mode)
    assert exc.value.status_code == 400
    assert "MOEX" in exc.value.detail


@pytest.mark.parametrize("mode", [0, 1, 2, 3, 4, 5, 64])
def test_h8_the_modes_this_broker_actually_uses_are_still_accepted(mode):
    """The live export's CalcMode distribution is {4: 245, 5: 54, 0: 45, 2: 18}; 1/3/64 are
    legal MT5 modes that need no exchange feed. None of them may be refused."""
    from api.routers.admin.skeletons import _reject_unsupported_calc_mode

    _reject_unsupported_calc_mode(mode)      # must not raise


def test_h8_the_opt_in_escape_hatch_works(monkeypatch):
    """A server that really runs the gateway must be able to opt in."""
    from api.routers.admin import skeletons

    monkeypatch.setenv(skeletons._MOEX_OPT_IN_ENV, "1")
    skeletons._reject_unsupported_calc_mode(34)      # must not raise


# --------------------------------------------------------------------------
# M18 — `_to_mode_int` accepted any integer and silently ignored unknown labels
# --------------------------------------------------------------------------

def test_m18_an_illegal_calc_mode_integer_is_refused():
    """`if isinstance(val, int): return val` let ANY number into `calc_mode`. 14 was in the
    old hand-written map as CRYPTO and is not an MT5 CalcMode at all; once stored,
    `basic_margin` raises on every order for that symbol."""
    from api.routers.admin.skeletons import _CALC_MODES, _to_mode_int

    for bad in (14, 99, -1):
        with pytest.raises(HTTPException) as exc:
            _to_mode_int(bad, 0, _CALC_MODES)
        assert exc.value.status_code == 400


def test_m18_an_unknown_label_is_refused_not_silently_ignored():
    """An unrecognised label returned `default`, so the PUT answered 200 and stored
    nothing - the operator saw a save that did not happen."""
    from api.routers.admin.skeletons import _CALC_MODES, _to_mode_int

    with pytest.raises(HTTPException) as exc:
        _to_mode_int("Crypto", 0, _CALC_MODES)
    assert exc.value.status_code == 400


def test_m18_legal_values_still_resolve():
    from api.routers.admin.skeletons import _CALC_MODES, _to_mode_int

    assert _to_mode_int(4, 0, _CALC_MODES) == 4
    assert _to_mode_int("CFD Leverage", 0, _CALC_MODES) == 4
    assert _to_mode_int("Forex No Leverage", 0, _CALC_MODES) == 5
    assert _to_mode_int("Exchange FORTS Futures", 0, _CALC_MODES) == 34   # legal MT5 value;
    # ...and then refused by _reject_unsupported_calc_mode, which is a separate policy
    # check. Validation and policy stay apart on purpose.


# --------------------------------------------------------------------------
# C11a — the event must be published AFTER the transaction boundary
# --------------------------------------------------------------------------

class _OrderRecordingUoW:
    """Stands in for UnitOfWork and records commit/publish ORDER, which is the only thing
    C11a is about. The real UoW's persistence bug is covered (xfail) in
    tests/integration/test_c11_transaction.py."""

    def __init__(self, log):
        self.log = log
        self.session = None

    async def __aenter__(self):
        self.log.append("enter")
        return self

    async def __aexit__(self, *exc):
        self.log.append("rollback" if exc[0] else "COMMIT")
        return False


def test_c11a_deal_created_is_published_after_the_commit():
    """Publishing inside the transaction means a subscriber that opens its own session
    reads a database that has not committed. With the in-process bus handlers run inline
    and awaited, so ConfigCache._on_positions_changed would cache a stale position list;
    with the Redis bus the message leaves the process before the rows exist."""
    import asyncio
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    from tests.integration.trading_harness import (
        InMemoryAccountRepository, InMemoryDealRepository, InMemoryOrderRepository,
        InMemoryPositionRepository, make_account, make_eurusd, make_group,
    )
    from application.commands.record_deal import RecordDealCommand, RecordDealHandler
    from core.domains.oms.entities.order import Order
    from core.domains.oms.enums import DealType, OrderState, OrderType
    from core.domains.common.value_objects import Price, Volume
    from core.domains.market_data.models import Tick
    from datetime import datetime, timezone

    log = []

    class Bus:
        async def publish(self, event):
            log.append(f"publish:{type(event).__name__}")

    class Feed:
        def get_latest_tick(self, n):
            return Tick(symbol=n, bid=D("1.10000"), ask=D("1.10010"), spread=D("0.00010"),
                        timestamp=datetime.now(timezone.utc), source="T")

    group = make_group()
    account = make_account(group=group)
    acc_repo = InMemoryAccountRepository()
    acc_repo.accounts[account.login] = account
    order_repo = InMemoryOrderRepository()
    order = Order(account_login=account.login, symbol="EURUSD", order_type=OrderType.BUY,
                  volume_initial=Volume(D("1")), volume_current=Volume(D("1")),
                  price_order=Price(D("1.10")), state=OrderState.PLACED,
                  contract_size=D("100000"), digits=5)
    asyncio.run(order_repo.save(order))

    sym_repo = type("SR", (), {"symbols": {"EURUSD": make_eurusd("EURUSD")}})()
    sym_repo.find_by_name = lambda name, session=None: _awaitable(
        sym_repo.symbols.get(name))

    handler = RecordDealHandler(
        order_repo=order_repo, account_repo=acc_repo,
        position_repo=InMemoryPositionRepository(), event_bus=Bus(),
        symbol_repo=sym_repo, market_feed=Feed(), deal_repo=InMemoryDealRepository(),
        uow_factory=lambda: _OrderRecordingUoW(log),
    )

    asyncio.run(handler.execute(RecordDealCommand(
        order_id=order.ticket_id, account_login=account.login, symbol="EURUSD",
        volume=D("1"), price=D("1.10"), deal_type=DealType.BUY,
        commission_amount=D("0"), swap_amount=D("0"), profit=D("0"))))

    assert "COMMIT" in log, log
    commit_at = log.index("COMMIT")
    deal_events = [i for i, e in enumerate(log) if e == "publish:DealCreated"]
    assert deal_events, f"DealCreated was never published: {log}"
    assert all(i > commit_at for i in deal_events), (
        f"DealCreated was published BEFORE the commit: {log}"
    )


async def _awaitable(value):
    return value


# --------------------------------------------------------------------------
# R24 — CLOSED AS NOT PRESENT (verified, not assumed)
#
# The audit item described `_market_feed_for_conversion` as swapping
# `risk_service.market_data_engine` for the duration of one await and restoring it in a
# `finally`, which would expose a concurrent `execute()`/`get_margin()`/`stopout_check()`
# to the wrong feed. That is NOT what this tree does.
#
# Verified two ways:
#   * `_market_feed_for_conversion` (application/services/risk_service.py:1226-1249) is a
#     plain `def` that RETURNS a candidate feed - it walks `self` and `self.risk_engine`
#     for an attribute exposing `get_latest_tick`, falls back to `api.di_providers`, and
#     returns None. It assigns to nothing.
#   * A repo-wide search for an assignment to `market_data_engine` outside constructors and
#     keyword arguments finds none in api/ or application/.
#
# So there is no shared-state mutation to guard, and a guard test would be asserting on
# code that does not exist. Nothing to fix; the item is closed as not-present. If a swap is
# ever introduced, the invariant to hold is: no `await` between taking and restoring a
# feed on an object other coroutines can reach.
# --------------------------------------------------------------------------

def test_r24_market_feed_for_conversion_does_not_mutate_shared_state():
    """Locks in the finding above: the helper must stay a pure reader.

    If this fails, someone reintroduced the swap the audit item described - at which point
    the real fix is to pass the feed as a parameter rather than to guard the mutation."""
    import ast
    import os

    root = os.path.abspath(__file__)
    for _ in range(5):                       # tests/unit/domains/risk/<this file> -> repo root
        root = os.path.dirname(root)
    src = open(os.path.join(root, "application", "services", "risk_service.py"),
               encoding="utf-8").read()
    tree = ast.parse(src)

    fn = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.AsyncFunctionDef, ast.FunctionDef)) \
                and node.name == "_market_feed_for_conversion":
            fn = node
            break
    assert fn is not None, (
        "_market_feed_for_conversion not found in risk_service.py; update this test")

    writes = [n for n in ast.walk(fn)
              if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign))
              and any(isinstance(t, ast.Attribute) for t in getattr(n, "targets", []) or [])]
    assert not writes, (
        f"_market_feed_for_conversion now WRITES to an attribute (line "
        f"{writes[0].lineno}). It must stay a pure reader: a feed swapped onto a service "
        f"object other coroutines can reach is visible to a concurrent "
        f"execute()/get_margin()/stopout_check() between two awaits, which would price a "
        f"conversion with the wrong currency pair. Pass the feed as a parameter instead.")
