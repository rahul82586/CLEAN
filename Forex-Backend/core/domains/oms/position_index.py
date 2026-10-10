"""
In-Memory Position Index — Phase 1.

Keeps active open positions indexed in memory by:
1. Symbol -> open positions (O(1) lookup for TickMarginPipeline).
2. Account -> open positions (O(1) lookup for equity/margin revaluations).
3. Price-sorted SL/TP trigger structures organized per symbol:
   - BUY-stops (SL, triggers on Bid <= SL): sorted ascending by SL
   - BUY-tps   (TP, triggers on Bid >= TP): sorted ascending by TP
   - SELL-stops(SL, triggers on Ask >= SL): sorted ascending by SL
   - SELL-tps  (TP, triggers on Ask <= TP): sorted ascending by TP

A tick only inspects positions that crossed current Bid/Ask using bisect
binary search in O(log M + K) time, instead of scanning all positions in O(N).

Single-Writer Rule:
Only the fill/close/modify commit path mutates this index AFTER the
database transaction commits. Rebuilt from PostgreSQL on startup.

Fail-Closed Rule:
Periodic reconciliation compares in-memory positions against the DB.
If the index is not ready or fails reconciliation, consumers fall back
to the durable position_repo path with an ERROR log. It never silently evaluates nothing.
"""
from __future__ import annotations

import bisect
import logging
import threading
from decimal import Decimal
from typing import Dict, List, Optional, Set, Tuple

from core.domains.oms.entities.position import Position

logger = logging.getLogger(__name__)


def _extract_decimal(val) -> Optional[Decimal]:
    if val is None:
        return None
    if hasattr(val, "value"):
        return Decimal(str(val.value))
    return Decimal(str(val))


class PositionIndex:
    """Thread-safe in-memory index for active open positions."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._ready: bool = False
        self._last_reconciliation_ok: bool = False

        # Primary storage: position_id -> Position
        self._positions: Dict[str, Position] = {}

        # Secondary indexes
        self._by_symbol: Dict[str, Set[str]] = {}
        self._by_account: Dict[int, Set[str]] = {}

        # Trigger search lists per symbol: symbol -> List[Tuple[Decimal, str]]
        # (price, position_id)
        self._buy_sl: Dict[str, List[Tuple[Decimal, str]]] = {}
        self._buy_tp: Dict[str, List[Tuple[Decimal, str]]] = {}
        self._sell_sl: Dict[str, List[Tuple[Decimal, str]]] = {}
        self._sell_tp: Dict[str, List[Tuple[Decimal, str]]] = {}

    @property
    def is_ready(self) -> bool:
        with self._lock:
            return self._ready

    def set_ready(self, ready: bool) -> None:
        with self._lock:
            self._ready = ready

    # ── Single-Writer Mutations (called AFTER DB commit) ─────────────────────

    def upsert(self, position: Position) -> None:
        """Add or update an open position. If time_done is set, removes it."""
        with self._lock:
            if getattr(position, "time_done", None) is not None:
                self._remove_locked(position.position_id)
                return

            # If existing, clean up previous indexes first
            if position.position_id in self._positions:
                self._remove_locked(position.position_id)

            pid = str(position.position_id)
            sym = str(position.symbol)
            acct = int(position.account_login)

            self._positions[pid] = position

            self._by_symbol.setdefault(sym, set()).add(pid)
            self._by_account.setdefault(acct, set()).add(pid)

            # Insert into price-sorted trigger structures
            act_str = str(getattr(position, "action", "")).upper()
            is_buy = "BUY" in act_str

            sl = _extract_decimal(getattr(position, "price_sl", None))
            tp = _extract_decimal(getattr(position, "price_tp", None))

            if is_buy:
                if sl is not None and sl > Decimal("0"):
                    lst = self._buy_sl.setdefault(sym, [])
                    bisect.insort(lst, (sl, pid))
                if tp is not None and tp > Decimal("0"):
                    lst = self._buy_tp.setdefault(sym, [])
                    bisect.insort(lst, (tp, pid))
            else:
                if sl is not None and sl > Decimal("0"):
                    lst = self._sell_sl.setdefault(sym, [])
                    bisect.insort(lst, (sl, pid))
                if tp is not None and tp > Decimal("0"):
                    lst = self._sell_tp.setdefault(sym, [])
                    bisect.insort(lst, (tp, pid))

    def remove(self, position_id: str) -> Optional[Position]:
        """Remove a closed position from all in-memory indexes."""
        with self._lock:
            return self._remove_locked(position_id)

    def _remove_locked(self, position_id: str) -> Optional[Position]:
        pid = str(position_id)
        pos = self._positions.pop(pid, None)
        if pos is None:
            return None

        sym = str(pos.symbol)
        acct = int(pos.account_login)

        if sym in self._by_symbol:
            self._by_symbol[sym].discard(pid)
            if not self._by_symbol[sym]:
                del self._by_symbol[sym]

        if acct in self._by_account:
            self._by_account[acct].discard(pid)
            if not self._by_account[acct]:
                del self._by_account[acct]

        # Remove from trigger lists
        if sym in self._buy_sl:
            self._buy_sl[sym] = [x for x in self._buy_sl[sym] if x[1] != pid]
        if self._buy_tp.get(sym):
            self._buy_tp[sym] = [x for x in self._buy_tp[sym] if x[1] != pid]
        if self._sell_sl.get(sym):
            self._sell_sl[sym] = [x for x in self._sell_sl[sym] if x[1] != pid]
        if self._sell_tp.get(sym):
            self._sell_tp[sym] = [x for x in self._sell_tp[sym] if x[1] != pid]

        return pos

    def rebuild(self, positions: List[Position]) -> None:
        """Clear and rebuild entire in-memory index from a database snapshot."""
        with self._lock:
            self._positions.clear()
            self._by_symbol.clear()
            self._by_account.clear()
            self._buy_sl.clear()
            self._buy_tp.clear()
            self._sell_sl.clear()
            self._sell_tp.clear()

            for p in positions:
                if getattr(p, "time_done", None) is None:
                    # Inline upsert logic without lock re-entry
                    pid = str(p.position_id)
                    sym = str(p.symbol)
                    acct = int(p.account_login)

                    self._positions[pid] = p
                    self._by_symbol.setdefault(sym, set()).add(pid)
                    self._by_account.setdefault(acct, set()).add(pid)

                    act_str = str(getattr(p, "action", "")).upper()
                    is_buy = "BUY" in act_str

                    sl = _extract_decimal(getattr(p, "price_sl", None))
                    tp = _extract_decimal(getattr(p, "price_tp", None))

                    if is_buy:
                        if sl is not None and sl > Decimal("0"):
                            bisect.insort(self._buy_sl.setdefault(sym, []), (sl, pid))
                        if tp is not None and tp > Decimal("0"):
                            bisect.insort(self._buy_tp.setdefault(sym, []), (tp, pid))
                    else:
                        if sl is not None and sl > Decimal("0"):
                            bisect.insort(self._sell_sl.setdefault(sym, []), (sl, pid))
                        if tp is not None and tp > Decimal("0"):
                            bisect.insort(self._sell_tp.setdefault(sym, []), (tp, pid))

            self._ready = True
            self._last_reconciliation_ok = True
            logger.info("PositionIndex rebuilt: %d open positions indexed", len(self._positions))

    # ── Fast In-Memory Queries (Hot Tick Path) ───────────────────────────────

    def get_by_symbol(self, symbol: str) -> List[Position]:
        """All open positions for a symbol. O(1) index lookup."""
        with self._lock:
            pids = self._by_symbol.get(str(symbol), set())
            return [self._positions[pid] for pid in pids if pid in self._positions]

    def get_by_account(self, login: int) -> List[Position]:
        """All open positions for an account. O(1) index lookup."""
        with self._lock:
            pids = self._by_account.get(int(login), set())
            return [self._positions[pid] for pid in pids if pid in self._positions]

    def get_position(self, position_id: str) -> Optional[Position]:
        """Lookup by ID."""
        with self._lock:
            return self._positions.get(str(position_id))

    def count(self) -> int:
        with self._lock:
            return len(self._positions)

    def find_triggered(
        self, symbol: str, bid: Decimal, ask: Decimal
    ) -> List[Tuple[Position, str, Decimal]]:
        """Find triggered positions using binary search on sorted price arrays.

        Returns list of (Position, reason ('SL'|'TP'), trigger_price).
        Amortized O(log M + K), where K = triggered positions count.
        """
        with self._lock:
            sym = str(symbol)
            triggered: List[Tuple[Position, str, Decimal]] = []
            seen_pids: Set[str] = set()

            # 1. Buy SL: triggers on Bid <= SL  -->  SL >= Bid
            if sym in self._buy_sl and self._buy_sl[sym]:
                lst = self._buy_sl[sym]
                # Elements with sl >= bid start from idx to end
                idx = bisect.bisect_left(lst, (bid, ""))
                for _, pid in lst[idx:]:
                    if pid not in seen_pids and pid in self._positions:
                        triggered.append((self._positions[pid], "SL", bid))
                        seen_pids.add(pid)

            # 2. Buy TP: triggers on Bid >= TP  -->  TP <= Bid
            if sym in self._buy_tp and self._buy_tp[sym]:
                lst = self._buy_tp[sym]
                # Elements with tp <= bid are from 0 to idx
                idx = bisect.bisect_right(lst, (bid, "\U0010ffff"))
                for _, pid in lst[:idx]:
                    if pid not in seen_pids and pid in self._positions:
                        triggered.append((self._positions[pid], "TP", bid))
                        seen_pids.add(pid)

            # 3. Sell SL: triggers on Ask >= SL  -->  SL <= Ask
            if sym in self._sell_sl and self._sell_sl[sym]:
                lst = self._sell_sl[sym]
                # Elements with sl <= ask are from 0 to idx
                idx = bisect.bisect_right(lst, (ask, "\U0010ffff"))
                for _, pid in lst[:idx]:
                    if pid not in seen_pids and pid in self._positions:
                        triggered.append((self._positions[pid], "SL", ask))
                        seen_pids.add(pid)

            # 4. Sell TP: triggers on Ask <= TP  -->  TP >= Ask
            if sym in self._sell_tp and self._sell_tp[sym]:
                lst = self._sell_tp[sym]
                # Elements with tp >= ask start from idx to end
                idx = bisect.bisect_left(lst, (ask, ""))
                for _, pid in lst[idx:]:
                    if pid not in seen_pids and pid in self._positions:
                        triggered.append((self._positions[pid], "TP", ask))
                        seen_pids.add(pid)

            return triggered

    # ── Reconciliation (Safety / Audit) ──────────────────────────────────────

    def reconcile_with_db(self, db_positions: List[Position]) -> bool:
        """Compare in-memory positions against DB snapshot. Logs differences loudly."""
        with self._lock:
            db_pids = {str(p.position_id) for p in db_positions if getattr(p, "time_done", None) is None}
            mem_pids = set(self._positions.keys())

            missing_in_mem = db_pids - mem_pids
            stale_in_mem = mem_pids - db_pids

            if missing_in_mem or stale_in_mem:
                logger.error(
                    "POSITION INDEX RECONCILIATION MISMATCH: in_memory=%d db=%d "
                    "missing_in_mem=%s stale_in_mem=%s",
                    len(mem_pids), len(db_pids), missing_in_mem, stale_in_mem,
                )
                self._last_reconciliation_ok = False
                return False

            self._last_reconciliation_ok = True
            return True


# Global shared singleton instance for the process
GLOBAL_POSITION_INDEX: PositionIndex = PositionIndex()
