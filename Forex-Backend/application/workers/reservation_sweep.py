"""Recover margin reservations stranded on orders that reached a terminal state.

`application/services/margin_reservation.py` documents this sweep as "the M7+ answer" to a
node crash between approval and terminal state. It did not exist, and three other paths
(cancel, expiry, stop-out) leaked reservations without any crash at all.

This worker is the recovery net for the ones that still get through. It is deliberately
CONSERVATIVE:

* it only acts on orders in a TERMINAL state (`FILLED`, `CANCELLED`, `REJECTED`, `EXPIRED`)
  that still hold margin;
* it never touches a working order. Freeing a live pending's hold would hand the client
  margin it has not actually regained - turning a leak into an overdraft;
* it releases through `release_margin`, which prefers the repository's atomic conditional
  UPDATE, so two concurrent sweeps cannot both succeed;
* it clears `order.reserved_margin` as it releases, so it is idempotent.

Every release is logged with the order id and the amount, because a recovery path that acts
silently is indistinguishable from one that leaks.
"""
import asyncio
import logging
from decimal import Decimal, InvalidOperation
from typing import Any, Optional

from application.services.margin_reservation import release_margin

logger = logging.getLogger(__name__)

#: Terminal states, matching the list `find_pending_orders` EXCLUDES. Taken from the
#: codebase rather than invented, so the two cannot disagree about what "finished" means.
TERMINAL_STATES = ("FILLED", "CANCELLED", "REJECTED", "EXPIRED")


def _dec(value: Any) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        return Decimal("0")


class ReservationSweep:
    """Release margin held by orders that are already finished."""

    def __init__(
        self,
        order_repo: Any,
        account_repo: Any = None,
        sweep_seconds: int = 900,
        batch_limit: int = 500,
    ) -> None:
        self.order_repo = order_repo
        self.account_repo = account_repo
        self.sweep_seconds = max(1, int(sweep_seconds))
        self.batch_limit = max(1, int(batch_limit))
        self._running = False

    async def start(self) -> None:
        self._running = True
        logger.info(
            "reservation sweep started (every %ss)", self.sweep_seconds
        )
        while self._running:
            try:
                released = await self.sweep_once()
                if released:
                    logger.info("reservation sweep released %s stale hold(s)", released)
            except Exception:  # noqa: BLE001 - the loop must survive a bad sweep
                logger.exception("reservation sweep failed")
            await asyncio.sleep(self.sweep_seconds)

    async def stop(self) -> None:
        self._running = False

    async def sweep_once(self) -> int:
        """One pass. Returns how many holds were released. Public for tests and ops."""
        finder = getattr(self.order_repo, "find_by_state_in", None)
        candidates = []

        if callable(finder):
            try:
                candidates = await finder(list(TERMINAL_STATES)) or []
            except Exception as exc:  # noqa: BLE001
                logger.warning("reservation sweep could not list terminal orders: %s", exc)
                return 0
        else:
            # No bulk accessor: page through and filter. Bounded, so a large book cannot
            # make this sweep unbounded work.
            pager = getattr(self.order_repo, "find_page", None)
            if not callable(pager):
                logger.warning(
                    "order repository exposes neither find_by_state_in nor find_page; "
                    "stale reservations cannot be swept"
                )
                return 0
            try:
                rows, _total = await pager(limit=self.batch_limit, offset=0)
                candidates = rows or []
            except Exception as exc:  # noqa: BLE001
                logger.warning("reservation sweep could not page orders: %s", exc)
                return 0

        released = 0
        for order in candidates:
            try:
                state = getattr(order, "state", None)
                name = str(getattr(state, "value", state) or "").upper()
                if name not in TERMINAL_STATES:
                    continue

                hold = _dec(getattr(order, "reserved_margin", 0))
                if hold <= 0:
                    continue

                login = getattr(order, "account_login", None)
                if login is None:
                    logger.warning(
                        "order %s holds %s but has no account_login; not released",
                        getattr(order, "ticket_id", "?"), hold,
                    )
                    continue

                await release_margin(self.account_repo, login, hold)
                # Clear the hold as it is released, so a second pass is a no-op.
                order.reserved_margin = Decimal("0")
                saver = getattr(self.order_repo, "save", None)
                if callable(saver):
                    await saver(order)

                released += 1
                logger.info(
                    "reservation sweep released %s stranded on order %s (account %s, %s)",
                    hold, getattr(order, "ticket_id", "?"), login, name,
                )
            except Exception:  # noqa: BLE001 - one bad order must not stop the sweep
                logger.exception(
                    "reservation sweep could not process order %s",
                    getattr(order, "ticket_id", "?"),
                )

        return released


class OrphanedReservationSweep:
    """Release reservations that NO order accounts for, under an explicit policy.

    Separate from `ReservationSweep`, and deliberately narrower. That one frees holds
    attributable to a terminal order; this one handles the residue no order claims, which the
    first sweep correctly refuses to guess at.

    Safe by construction - it acts only when ALL of these hold:

    * the account holds a positive `margin_reserved`;
    * NO order for the account holds any reservation at all;
    * the account has NO orders in a non-terminal state.

    If any order holds something, or a working order exists, the account is SKIPPED: the
    residue might belong to it, and freeing it could over-extend the account.

    `dry_run=True` by DEFAULT. Applying is a separate, explicit call - the account's money
    should not move because a module was imported.
    """

    #: Terminal states, matching `ReservationSweep` and `find_pending_orders`.
    TERMINAL_STATES = ("FILLED", "CANCELLED", "REJECTED", "EXPIRED")

    def __init__(self, order_repo: Any, account_repo: Any = None) -> None:
        self.order_repo = order_repo
        self.account_repo = account_repo

    async def _orders_for(self, login: Any) -> list:
        repo = self.order_repo
        for name in ("find_by_account", "get_by_account", "find_pending_orders"):
            getter = getattr(repo, name, None)
            if getter is None:
                continue
            try:
                # `orders.account_login` is VARCHAR and `accounts.login` is BIGINT, so the
                # value must be passed as a STRING. Passing the int raised
                # `operator does not exist: character varying = bigint`, the error was
                # logged, and `[]` came back - which the safety check would have read as
                # "no orders", i.e. the opposite of "51 orders, none holding". A silent
                # empty list here disables the whole guard, so the failure is raised
                # rather than swallowed.
                result = getter(int(login))
                if hasattr(result, "__await__"):
                    result = await result
                return list(result or [])
            except Exception as exc:  # noqa: BLE001
                # NOT `return []`: an empty list means "this account has no orders", which
                # SATISFIES the safety check. Failing to read the orders must not be
                # indistinguishable from there being none, so the account is refused
                # instead - signalled by a None return.
                logger.error(
                    "orphan sweep could not list orders for %s: %s; REFUSING to treat this "
                    "as 'no orders', because that would satisfy the safety check",
                    login, exc,
                )
                return None
        return []

    async def scan(self, logins: Any = None) -> list:
        """Accounts carrying a hold that no order accounts for. Read-only."""
        if self.account_repo is None:
            return []
        finder = getattr(self.account_repo, "find_all", None)
        if not callable(finder):
            logger.error(
                "orphan sweep needs account_repo.find_all to enumerate candidates"
            )
            return []
        try:
            accounts = await finder()
        except Exception as exc:  # noqa: BLE001
            logger.error("orphan sweep could not list accounts: %s", exc)
            return []

        out = []
        for account in (accounts or []):
            login = getattr(account, "login", None)
            if login is None:
                continue
            if logins is not None and str(login) not in {str(x) for x in logins}:
                continue
            held = _dec(getattr(getattr(account, "margin_reserved", None), "amount", 0))
            if held <= 0:
                continue

            orders = await self._orders_for(login)
            if orders is None:
                # The order list could not be read, so attribution is UNKNOWN. Skipped,
                # because an unreadable list must never look like an empty one.
                continue
            attributable = sum(
                max(Decimal("0"), _dec(getattr(o, "reserved_margin", 0))) for o in orders
            )
            working = [
                o for o in orders
                if str(getattr(getattr(o, "state", None), "value",
                           getattr(o, "state", "")) or "").upper()
                not in self.TERMINAL_STATES
            ]

            if attributable > 0:
                logger.info(
                    "account %s holds %.8f but orders already account for %.8f; left alone",
                    login, held, attributable,
                )
                continue
            if working:
                logger.info(
                    "account %s holds %.8f with %d working order(s); left alone",
                    login, held, len(working),
                )
                continue

            out.append({"login": login, "held": held, "orders": len(orders)})
        return out

    async def sweep_once(self, *, dry_run: bool = True, logins: Any = None) -> dict:
        """Release unattributable holds, or report what WOULD be released.

        Returns a report either way, so the caller can log exactly what happened and a broker
        can reconcile it. Every release is reversible by re-reserving.
        """
        candidates = await self.scan(logins=logins)
        report = {
            "dry_run": dry_run,
            "candidates": [dict(c) for c in candidates],
            "released": 0,
            "released_total": Decimal("0"),
        }
        if dry_run:
            for c in candidates:
                logger.warning(
                    "DRY RUN: account %s holds %.8f in margin_reserved that NO order accounts "
                    "for (%d order(s), none holding). Release it with dry_run=False.",
                    c["login"], c["held"], c["orders"],
                )
            return report

        for c in candidates:
            login, held = c["login"], c["held"]
            try:
                await release_margin(self.account_repo, login, held)
                report["released"] += 1
                report["released_total"] += held
                logger.warning(
                    "ORPHANED RESERVATION RELEASED: account %s, %.8f. No order accounted for "
                    "it (%d order(s), all terminal, none holding). Re-reserve if this was "
                    "wrong.",
                    login, held, c["orders"],
                )
            except Exception as exc:  # noqa: BLE001
                logger.error("could not release the orphaned hold on %s: %s", login, exc)
        return report
