"""R20: the manager desk must not roll back balance writes it did not read.

The defect: `api/routers/manager/trading.py` persisted accounts with full-row
`save()` on snapshots it had loaded earlier.

  * OrderClose booked PnL as read-modify-write - `find_by_login`,
    `Money(balance + pnl)`, `save()` - so a fill, deposit or second manager
    action that committed between the read and the write was rolled back to
    the stale snapshot. On a real ledger, money simply disappears.
  * `recalculate_account_trading_state` saved the whole row after recomputing
    profit / equity / margin, overwriting balance and credit with whatever
    its initial `find_by_login` had seen.

This is D8b (tick pipeline vs fill, margin_used) transplanted to the manager
desk, and it gets the same cure: disjoint write sets, enforced in SQL.

  * `adjust_balance()` books a delta in ONE `balance = balance + :delta`
    UPDATE - the database serialises concurrent writers, no snapshot to lose.
  * `_persist_recalculated_valuation()` writes the valuation through
    `update_valuation(include_margin=True)`, which by construction cannot
    touch balance / credit / margin_reserved.

Like the D8b tests, these interleave the two writers by hand instead of
hoping to hit a timing window.
"""
from decimal import Decimal

import pytest

from core.domains.common.value_objects import Money
from infrastructure.persistence.database import DatabaseManager
from infrastructure.persistence.repositories.account_repository import (
    SqlAccountRepository,
)

import infrastructure.persistence.account_models  # noqa: F401  registers tables
import infrastructure.persistence.db_models       # noqa: F401


@pytest.fixture
async def sql_repo(tmp_path):
    """Real Sql* repositories over SQLite, with one group seeded (as in D8b)."""
    from infrastructure.persistence.di_setup import setup_persistence_di
    from infrastructure.config import seeder
    from infrastructure.security.password_hasher import Argon2PasswordHasher

    manager = DatabaseManager(f"sqlite+aiosqlite:///{tmp_path / 'r20.db'}")
    await manager.create_tables()
    providers = setup_persistence_di(manager)
    await seeder.seed_all(
        group_repo=providers["group_repo"], symbol_repo=providers["symbol_repo"],
        manager_repo=providers["manager_repo"], account_repo=providers["account_repo"],
        coverage_repo=providers["coverage_repo"], config_root="config",
        password_hasher=Argon2PasswordHasher(),
    )
    repo = providers["account_repo"]
    global SEEDED_GROUP
    groups = await providers["group_repo"].get_all()
    SEEDED_GROUP = next((g for g in groups if g.name == GROUP), groups[0])
    yield repo
    await manager.close()


GROUP = "demo\\Standard"
#: set by the fixture; account_to_db needs a real Group, not just the name
SEEDED_GROUP = None


def _account(login=880101, **over):
    from core.domains.accounts.account import Account

    a = Account(login=login, client_id="R20", group=SEEDED_GROUP, group_id=GROUP, currency="USD",
                balance=Money(Decimal("100000"), "USD"), credit=Money(Decimal("0"), "USD"),
                equity=Money(Decimal("100000"), "USD"),
                margin_used=Money(Decimal("0"), "USD"),
                margin_free=Money(Decimal("100000"), "USD"))
    for k, v in over.items():
        setattr(a, k, v)
    return a


@pytest.mark.asyncio
async def test_adjust_balance_serialises_concurrent_writers(sql_repo):
    """A manager PnL booking and a concurrent fill both land - the R20 race.

    Hand-interleaved the way the defect happened live:

        T0  manager OrderClose loads the account     balance = 100000
        T1  a fill books +500 PnL                    balance = 100500
        T2  the manager books its own -200 PnL       balance = 100300

    The old read-modify-write committed the T0 snapshot at T2 and the fill's
    +500 vanished. With one atomic `balance = balance + delta` per writer,
    the database serialises them and both movements survive.
    """
    await sql_repo.save(_account())

    # T0: the manager handler reads the account (this is all it should need
    # the read for - currency, existence - never for the balance arithmetic).
    stale = await sql_repo.find_by_login(880101)
    assert stale.balance.amount == Decimal("100000")

    # T1: a fill books profit on the same account while the manager is
    # between its read and its write.
    after_fill = await sql_repo.adjust_balance(880101, Decimal("500"))
    assert after_fill == Decimal("100500")

    # T2: the manager books the close PnL as a delta, not as a snapshot.
    after_close = await sql_repo.adjust_balance(880101, Decimal("-200"))
    assert after_close == Decimal("100300")

    fresh = await sql_repo.find_by_login(880101)
    assert fresh.balance.amount == Decimal("100300"), (
        "a concurrent balance write was lost - the manager desk rolled the "
        "ledger back to its stale snapshot"
    )


@pytest.mark.asyncio
async def test_adjust_balance_returns_none_for_missing_account(sql_repo):
    """A vanished account must report None, never raise or invent a row."""
    assert await sql_repo.adjust_balance(999999, Decimal("10")) is None


@pytest.mark.asyncio
async def test_stale_valuation_write_cannot_clobber_balance(sql_repo):
    """The recalculation's write set is disjoint from the ledger's.

    `recalculate_account_trading_state` persists through
    `_persist_recalculated_valuation` -> `update_valuation(include_margin=True)`.
    A balance movement that commits while the recalculation is mid-flight must
    survive the valuation write, and the valuation columns (including the
    margin repair) must still land.
    """
    from api.routers.manager.trading import _persist_recalculated_valuation

    await sql_repo.save(_account(login=880102))

    # The recalculation loads the account and starts deriving numbers...
    stale = await sql_repo.find_by_login(880102)

    # ...meanwhile a fill books +750 PnL onto the balance.
    assert await sql_repo.adjust_balance(880102, Decimal("750")) == Decimal("100750")

    # The recalculation finishes and writes ITS columns from the stale snapshot.
    stale.profit = Money(Decimal("-12.34"), "USD")
    stale.equity = Money(Decimal("99987.66"), "USD")
    stale.margin_used = Money(Decimal("55.50"), "USD")
    stale.margin_free = Money(Decimal("99932.16"), "USD")
    await _persist_recalculated_valuation(sql_repo, stale)

    after = await sql_repo.find_by_login(880102)
    # The fill's balance movement SURVIVED - that is the whole point.
    assert after.balance.amount == Decimal("100750"), (
        "the valuation write rolled back a committed balance movement"
    )
    # ...and the recalculation's own columns landed, margin_used included
    # (include_margin=True is what lets a sweep repair an under-margined row).
    assert after.profit.amount == Decimal("-12.34")
    assert after.margin_used.amount == Decimal("55.50")


@pytest.mark.asyncio
async def test_valuation_helper_falls_back_to_save_without_the_setter():
    """In-memory doubles without update_valuation keep working (via save)."""
    from api.routers.manager.trading import _persist_recalculated_valuation

    class _NoValuationRepo:
        def __init__(self):
            self.saved = []

        async def save(self, account, session=None):
            self.saved.append(account)
            return account

    repo = _NoValuationRepo()
    acc = object()
    await _persist_recalculated_valuation(repo, acc)
    assert repo.saved == [acc]


@pytest.mark.asyncio
async def test_valuation_helper_supports_setters_without_include_margin():
    """A double with the old update_valuation(account) signature still gets
    the disjoint-column write - just without the margin repair."""
    from api.routers.manager.trading import _persist_recalculated_valuation

    class _LegacyValuationRepo:
        def __init__(self):
            self.valued = []
            self.saved = []

        async def update_valuation(self, account, session=None):
            self.valued.append(account)
            return 1

        async def save(self, account, session=None):
            self.saved.append(account)
            return account

    repo = _LegacyValuationRepo()
    acc = object()
    await _persist_recalculated_valuation(repo, acc)
    assert repo.valued == [acc]
    assert repo.saved == [], "must not fall through to a full-row save"
