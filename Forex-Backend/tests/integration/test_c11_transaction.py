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
# C11 is FIXED: a fill is ONE transaction, and its event lands after the commit.
#
# Both tests below used to be locked (xfail/skip) because enabling the unit of work
# broke fills: the order stayed PLACED, no deal row and no position row was written,
# while the account row WAS updated and DealCreated still published - a silent tear.
#
# Root cause: repositories bound to a unit of work receive a shared-session factory,
# and any repo method falling back to `async with self.session_factory() as sess:`
# received the shared AsyncSession ITSELF - whose context-manager exit CLOSES it,
# rolling the half-written transaction back. SqlAccountRepository.find_by_login reaches
# SqlGroupRepository.find_by_name exactly that way, mid-fill, on every single deal.
#
# The fix, in three layers:
#   * _SharedSessionFactory now hands out a scope that never closes the session and
#     downgrades a repository's own commit() to flush() - the one real commit stays
#     with UnitOfWork.__aexit__ (infrastructure/persistence/unit_of_work.py);
#   * the nested group lookup (find_by_login -> find_by_name) and the fill's symbol
#     reads thread the UoW session explicitly, so they join the one transaction
#     instead of opening a second session on the shared connection;
#   * api/main.py passes uow_factory to build_trading_stack, so production fills
#     actually run through this path (the degraded case logs loudly).
#
# The third test pins the factory contract itself, so a future "simplification" back
# to the raw session fails HERE instead of silently tearing fills in production.
#
# C11a (post-commit publish) was already fixed and is asserted by the first test and
# by tests/unit/domains/risk/test_rms_open_items.py.
# ---------------------------------------------------------------------------------------


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


@pytest.mark.asyncio
async def test_c11_the_shared_session_scope_never_closes_or_commits_early(db):
    """The factory contract the fill path depends on, pinned directly.

    Repositories do `async with self.session_factory() as sess:` and some call
    `sess.commit()` inside the block. Within a unit of work the factory must hand out a
    scope that (a) does NOT close the shared session on exit, and (b) turns commit()
    into flush() - so everything stays inside the ONE transaction until
    UnitOfWork.__aexit__, and a rollback still undoes all of it.
    """
    from sqlalchemy import text

    from infrastructure.persistence.mappers import group_to_db

    group, _symbol = _seed()

    # (a)+(b): scope exit / scope commit() / scope close() must not end the UoW
    # transaction, and the rollback below must still undo the UoW's own write.
    with pytest.raises(RuntimeError):
        async with UnitOfWork(session_factory=db) as uow:
            shared = uow.accounts.session_factory
            await uow.session.merge(group_to_db(group))
            async with shared() as sess:
                await sess.execute(text("SELECT 1"))
                await sess.commit()      # must flush, NOT commit
                await sess.close()       # must be a no-op
            assert uow.session.in_transaction(), (
                "a repository block on the shared factory ended the unit of work's "
                "transaction - the C11 close/commit landmine is back"
            )
            raise RuntimeError("boom")

    async with db() as check:
        count = (await check.execute(text("SELECT count(*) FROM groups"))).scalar()
    assert count == 0, (
        "the scope's commit() committed for real: a rolled-back unit of work left "
        "persisted rows behind"
    )

    # The same scope usage inside a unit of work that COMMITS: the write made before
    # the scope block must land with the single UoW commit.
    async with UnitOfWork(session_factory=db) as uow:
        shared = uow.accounts.session_factory
        await uow.session.merge(group_to_db(group))
        async with shared() as sess:
            await sess.execute(text("SELECT 1"))
            await sess.commit()

    async with db() as check:
        count = (await check.execute(text("SELECT count(*) FROM groups"))).scalar()
    assert count == 1, (
        "the UoW's single commit must persist writes made before a repository scope "
        "block ran on the shared factory"
    )
