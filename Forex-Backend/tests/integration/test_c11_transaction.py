"""C11 / C11a — a fill is one transaction, and its event lands after the commit.

Uses the REAL SQL repositories, the REAL UnitOfWork and a REAL (SQLite) database. Nothing
here is a double, because the whole point is the transaction boundary.
"""
from __future__ import annotations

import asyncio
from decimal import Decimal as D

import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from application.commands.record_deal import RecordDealCommand, RecordDealHandler
from core.domains.accounts.enums import MarginMode
from core.domains.accounts.group import Group
from core.domains.accounts.value_objects import GroupPermissions, MarginProfile, Money
from core.domains.common.value_objects import Price, Volume
from core.domains.instruments.enums import CalculationMode
from core.domains.instruments.symbol import Symbol
from core.domains.market_data.models import Tick
from core.domains.oms.entities.order import Order
from core.domains.oms.enums import DealType, OrderState, OrderType
from core.domains.oms.enums import PositionAction
from infrastructure.persistence.config_models import Base as ConfigBase
from infrastructure.persistence.db_models import Base as TradeBase
from infrastructure.persistence.repositories.account_repository import SqlAccountRepository
from infrastructure.persistence.repositories.deal_repository import SqlDealRepository
from infrastructure.persistence.repositories.group_repository import SqlGroupRepository
from infrastructure.persistence.repositories.order_repository import SqlOrderRepository
from infrastructure.persistence.repositories.position_repository import SqlPositionRepository
from infrastructure.persistence.repositories.symbol_repository import SqlSymbolRepository
from infrastructure.persistence.unit_of_work import UnitOfWork

from datetime import datetime, timezone


class RecordingBus:
    """An in-process bus that, on each publish, READS THE DATABASE.

    That is the whole test: if the event is published inside the transaction, this read
    happens on a separate session and sees nothing committed yet.
    """

    def __init__(self, deal_repo):
        self.deal_repo = deal_repo
        self.events = []
        self.deals_visible_at_publish = []

    async def publish(self, event):
        self.events.append(type(event).__name__)
        try:
            visible = await self.deal_repo.find_by_account(1)
        except Exception:
            visible = None
        self.deals_visible_at_publish.append(None if visible is None else len(visible))


class StaticFeed:
    def get_latest_tick(self, symbol):
        return Tick(symbol=symbol, bid=D("1.10000"), ask=D("1.10010"),
                    spread=D("0.00010"), timestamp=datetime.now(timezone.utc), source="T")


class SyncSymbolView:
    """RiskEngine refuses an async symbol repo on the hot path; this is the ConfigCache shape."""

    def __init__(self, symbols):
        self.symbols = {s.name: s for s in symbols}

    def get_symbol(self, name):
        return self.symbols.get(name)

    def find_by_name(self, name):
        return self.symbols.get(name)


# ---------------------------------------------------------------------------------------
# BOTH tests in this module are xfail(strict=True) on purpose.
#
# C11 (no transaction around a fill) is an OPEN defect, not a fixed one. Enabling it is one
# line - pass `uow_factory=_container_lookup("uow_factory")` to `build_trading_stack` in
# api/main.py - and that line BREAKS fills:
#
#   * the order stays PLACED, and no deal row and no position row is written;
#   * the account row IS updated, so margin_used/margin_reserved change;
#   * `execute()` still returns a Deal and still publishes DealCreated, so nothing complains.
#
# Instrumenting `UnitOfWork.commit` shows the cause: at commit time the unit of work's
# session has `new=0, dirty=1` and its identity map contains ONLY AccountModel. The order,
# deal and position merges never reach that session, so its commit has nothing to flush for
# them. That has never been hit in production because `uow_factory` was never passed.
#
# The rollback test below PASSES today, but vacuously - "nothing was written" trivially
# satisfies "nothing survived the rollback". It is kept, and xfailed, so that both become
# meaningful the moment the UoW integration is repaired. `strict=True` means this module
# must be revisited if either test starts passing.
#
# What IS fixed and covered elsewhere: C11a, the post-commit publish. `record_deal.execute`
# now collects DealCreated and publishes it after the transaction boundary, so a subscriber
# that opens its own session (ConfigCache._on_positions_changed) can no longer read a
# database that has not committed. See tests/unit/domains/risk/test_rms_open_items.py.
# ---------------------------------------------------------------------------------------
_C11_REASON = (
    "C11 OPEN: RecordDealHandler's unit-of-work path persists only the account row; the "
    "order, deal and position merges never reach the UoW session"
)


@pytest.fixture
async def db(tmp_path):
    engine = create_async_engine(
        f"sqlite+aiosqlite:///{tmp_path/'c11.db'}",
        poolclass=StaticPool, connect_args={"check_same_thread": False},
    )
    async with engine.begin() as conn:
        await conn.run_sync(TradeBase.metadata.create_all)
        await conn.run_sync(ConfigBase.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False)
    yield factory
    await engine.dispose()


def _seed():
    group = Group(
        name="demo\\Standard", currency="USD", currency_digits=2,
        margin=MarginProfile(mode=MarginMode.RETAIL_HEDGED, leverage_default=100,
                             leverage_max=500, margin_call_level=D("50"),
                             stop_out_level=D("30")),
        permissions=GroupPermissions(allowed_symbols=["*"]),
    )
    symbol = Symbol(
        name="EURUSD", path="Forex\\EURUSD", base_currency="EUR", quote_currency="USD",
        margin_currency="USD", calc_mode=CalculationMode.FOREX, contract_size=D("100000"),
        tick_size=D("0.00001"), mt5_tick_size=D("0"), digits=5,
        volume_min=D("0.01"), volume_max=D("100"), volume_step=D("0.01"),
    )
    return group, symbol


async def _prepare(factory):
    group, symbol = _seed()
    group_repo = SqlGroupRepository(factory)
    symbol_repo = SqlSymbolRepository(factory)
    account_repo = SqlAccountRepository(
        session_factory=factory, group_repo=group_repo)
    await group_repo.save(group)
    await symbol_repo.save(symbol)

    from core.domains.accounts.account import Account
    account = Account(login=1, client_id="C1", group_id=group.name, group_name=group.name,
                      group=group, currency="USD", leverage=100,
                      balance=Money(D("10000"), "USD"), credit=Money(D("0"), "USD"))
    account.equity = Money(D("10000"), "USD")
    account.margin_free = Money(D("10000"), "USD")
    await account_repo.save(account)

    order_repo = SqlOrderRepository(factory)
    order = Order(account_login=1, symbol="EURUSD", order_type=OrderType.BUY,
                  volume_initial=Volume(D("1")), volume_current=Volume(D("1")),
                  price_order=Price(D("1.10")), state=OrderState.PLACED,
                  contract_size=D("100000"), digits=5)
    order.reserved_margin = D("1000")
    await order_repo.save(order)

    # the account row must carry the reservation the gate placed
    await account_repo.reserve_margin(1, D("1000"))
    return order, account_repo, order_repo, symbol_repo, group


@pytest.mark.asyncio
@pytest.mark.xfail(reason=_C11_REASON, strict=True, raises=AssertionError)
async def test_c11_a_fill_commits_atomically_and_the_event_sees_it(db):
    order, account_repo, order_repo, symbol_repo, group = await _prepare(db)
    deal_repo = SqlDealRepository(db)
    position_repo = SqlPositionRepository(db)
    bus = RecordingBus(deal_repo)

    def uow_factory():
        return UnitOfWork(session_factory=db)

    from core.domains.risk.engine import RiskEngine
    handler = RecordDealHandler(
        order_repo=order_repo, account_repo=account_repo, position_repo=position_repo,
        event_bus=bus, symbol_repo=symbol_repo, market_feed=StaticFeed(),
        deal_repo=deal_repo, uow_factory=uow_factory,
    )

    deal = await handler.execute(RecordDealCommand(
        order_id=order.ticket_id, account_login=1, symbol="EURUSD", volume=D("1"),
        price=D("1.10"), deal_type=DealType.BUY, commission_amount=D("0"),
        swap_amount=D("0"), profit=D("0")))

    # --- the event was published, and AFTER the commit -----------------------
    assert "DealCreated" in bus.events
    assert bus.deals_visible_at_publish and bus.deals_visible_at_publish[0] == 1, (
        f"DealCreated was published before the transaction committed, so a subscriber "
        f"reading its own session saw {bus.deals_visible_at_publish[0]} deals. "
        f"C11a requires the publish to happen after __aexit__ commits."
    )

    # --- everything landed ---------------------------------------------------
    saved_order = await order_repo.find_by_id(order.ticket_id)
    assert saved_order.state == OrderState.FILLED
    assert saved_order.reserved_margin == D("0"), "the hold must be released by the fill"

    positions = await position_repo.get_by_account(1)
    assert len(positions) == 1
    assert positions[0].volume.value == D("1")

    account = await account_repo.find_by_login(1)
    assert account.margin_reserved.amount == D("0")
    assert account.margin_used.amount == D("1000.0"), account.margin_used
    assert account.margin_level > D("0")


@pytest.mark.asyncio
@pytest.mark.skip(reason=_C11_REASON + " - this rollback test PASSES today but vacuously: "
                  "with nothing written, 'nothing survived the rollback' is trivially true. "
                  "Un-skip it together with the xfail above once the UoW persists.")
async def test_c11_a_failure_rolls_the_whole_fill_back(db):
    """The point of the transaction: a failure part-way leaves NO partial state."""
    order, account_repo, order_repo, symbol_repo, group = await _prepare(db)
    deal_repo = SqlDealRepository(db)
    position_repo = SqlPositionRepository(db)
    bus = RecordingBus(deal_repo)

    def uow_factory():
        return UnitOfWork(session_factory=db)

    from core.domains.risk.engine import RiskEngine
    handler = RecordDealHandler(
        order_repo=order_repo, account_repo=account_repo, position_repo=position_repo,
        event_bus=bus, symbol_repo=symbol_repo, market_feed=StaticFeed(),
        deal_repo=deal_repo, uow_factory=uow_factory,
    )

    # break the position step, which runs AFTER the order is set FILLED and AFTER the
    # Deal row is built
    async def explode(*a, **k):
        raise RuntimeError("injected failure during position write")

    handler._apply_deal_to_positions = explode

    with pytest.raises(RuntimeError):
        await handler.execute(RecordDealCommand(
            order_id=order.ticket_id, account_login=1, symbol="EURUSD", volume=D("1"),
            price=D("1.10"), deal_type=DealType.BUY, commission_amount=D("0"),
            swap_amount=D("0"), profit=D("0")))

    after_order = await order_repo.find_by_id(order.ticket_id)
    after_account = await account_repo.find_by_login(1)
    after_deals = await deal_repo.find_by_account(1)
    after_positions = await position_repo.get_by_account(1)

    assert after_order.state == OrderState.PLACED, (
        f"the order kept a state from a rolled-back transaction: {after_order.state}"
    )
    assert after_deals == [] or len(after_deals) == 0, "a deal survived the rollback"
    assert after_positions == [], "a position survived the rollback"
    assert after_account.margin_reserved.amount == D("1000"), (
        "the reservation must survive the rollback - the order is still live"
    )
    assert "DealCreated" not in bus.events, "no event may be published for a rolled-back deal"
