"""
Tick & Margin Pipeline - The Heartbeat of the Broker.

Orchestrates the critical path:
Tick -> Position PnL Update -> Account Equity Recalculation -> Margin State Evaluation.

Mirrors MT5's IMTTickSink -> IMTAccountSink flow.

Phase 1 Optimization:
1. Reads positions from in-memory PositionIndex (O(1)) instead of querying PostgreSQL per tick.
2. Trailing-edge coalescing per symbol (coalesce_seconds) to bundle bursts into batches.
"""
from __future__ import annotations

import asyncio
import logging
import os
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict, List, Optional, Set

from application.monitoring.tick_counters import TICK_COUNTERS
from core.domains.accounts.account import Account
from core.domains.common.value_objects import Money, Price, Volume
from core.domains.market_data.models import Tick
from core.domains.oms.entities.position import Position
from core.domains.oms.enums import PositionAction
from core.domains.oms.position_index import GLOBAL_POSITION_INDEX, PositionIndex
from core.domains.risk.engine import CurrencyConversionError, RiskEngine
from core.events.domain_events import (
    MarginCallEntered,
    MarginCallExited,
    StopOutEntered,
    StopOutExited,
)
from core.ports.interfaces import (
    IAccountRepository,
    IEventBus,
    IMarketDataFeed,
    IPositionRepository,
    ISymbolRepository,
)

logger = logging.getLogger(__name__)


class TickMarginPipeline:
    """Calculates position PnL, account equity, and evaluates margin state."""

    def __init__(
        self,
        position_repo: IPositionRepository,
        account_repo: IAccountRepository,
        symbol_repo: ISymbolRepository,
        risk_engine: RiskEngine,
        event_bus: IEventBus,
        coalesce_seconds: Optional[float] = None,
        position_index: Optional[PositionIndex] = None,
    ):
        self.position_repo = position_repo
        self.account_repo = account_repo
        self.symbol_repo = symbol_repo
        self.risk_engine = risk_engine
        self.event_bus = event_bus
        self.position_index = position_index

        if coalesce_seconds is None:
            coalesce_seconds = float(os.environ.get("TICK_MARGIN_COALESCE_SECONDS", "0.0") or 0.0)
        self.coalesce_seconds = max(0.0, float(coalesce_seconds))

        self._pending: Dict[str, Any] = {}
        self._flush_tasks: Dict[str, Any] = {}
        self.account_read_cache_seconds = max(
            0.0, float(os.environ.get("ACCOUNT_READ_CACHE_SECONDS", "0") or 0)
        )
        self._account_positions_cache: Dict[str, Any] = {}
        self._account_positions_cached_at: Dict[str, float] = {}
        self._warned_full_row_save = False

    async def process_tick(self, tick: Tick) -> None:
        """Entry point for a new Tick. Coalesces when a window is configured."""
        if self.coalesce_seconds <= 0:
            await self._process_tick_now(tick)
            return

        symbol_name = tick.symbol
        if symbol_name in self._pending:
            TICK_COUNTERS.inc_margin_coalesced_dropped(symbol_name)
        self._pending[symbol_name] = tick
        task = self._flush_tasks.get(symbol_name)
        if task is None or task.done():
            self._flush_tasks[symbol_name] = asyncio.create_task(
                self._flush_later(symbol_name)
            )

    async def _flush_later(self, symbol_name: str) -> None:
        """Apply the newest tick for a symbol once the coalescing window closes."""
        try:
            await asyncio.sleep(self.coalesce_seconds)
            tick = self._pending.pop(symbol_name, None)
            if tick is not None:
                await self._process_tick_now(tick)
        except asyncio.CancelledError:
            pass
        except Exception:  # noqa: BLE001
            logger.exception("coalesced flush failed for %s", symbol_name)

    async def flush(self) -> int:
        """Apply every pending tick now, and return how many were applied."""
        applied = 0
        for symbol_name, tick in list(self._pending.items()):
            self._pending.pop(symbol_name, None)
            task = self._flush_tasks.pop(symbol_name, None)
            if task is not None and not task.done():
                task.cancel()
            try:
                await self._process_tick_now(tick)
                applied += 1
            except Exception:  # noqa: BLE001
                logger.exception("could not flush %s", symbol_name)
        return applied

    async def _process_tick_now(self, tick: Tick) -> None:
        """Evaluates PnL and updates margin for affected open positions."""
        TICK_COUNTERS.inc_margin_pipeline(tick.symbol)
        symbol_name = tick.symbol

        # 1. Fetch all open positions for this symbol (from memory index if ready)
        if self.position_index and self.position_index.is_ready:
            positions = self.position_index.get_by_symbol(symbol_name)
        else:
            positions = await self.position_repo.get_by_symbol(symbol_name)

        if not positions:
            return  # No open positions, skip processing

        # 2. Fetch symbol info for currency conversion
        symbol = await self.symbol_repo.find_by_name(symbol_name)
        if not symbol:
            logger.error("Symbol %s not found for tick processing", symbol_name)
            return

        # 3. Fetch all affected accounts
        account_logins = list(set(p.account_login for p in positions))
        accounts: Dict[int, Account] = {}
        for login in account_logins:
            acc = await self.account_repo.find_by_login(login)
            if acc:
                accounts[login] = acc

        # 4. Update PnL for each position
        repriced: Dict[str, Position] = {}
        legacy_write = False
        for position in positions:
            account = accounts.get(position.account_login)
            if not account:
                continue

            try:
                conversion_rate = self.risk_engine.get_conversion_rate(
                    symbol.quote_currency,
                    account.currency,
                    market_feed=self.risk_engine.market_data_engine,
                )
            except CurrencyConversionError as e:
                logger.error("Cannot calculate PnL for position %s: %s", position.position_id, e)
                continue

            # MT5 PnL Valuation Rule:
            # BUY positions are valued at BID; SELL positions at ASK
            act_str = position.action.value if hasattr(position.action, "value") else str(position.action)
            is_buy = "BUY" in str(act_str).upper()
            current_price_decimal = tick.bid if is_buy else tick.ask
            price_obj = Price(current_price_decimal)

            _update_valuation = getattr(self.position_repo, "update_valuation", None)
            if _update_valuation is not None:
                try:
                    written = await _update_valuation(
                        position.position_id, act_str, current_price_decimal
                    )
                except Exception as exc:  # noqa: BLE001
                    logger.error(
                        "could not revalue position %s: %s - keeping the stored figures "
                        "rather than writing a guess", position.position_id, exc,
                    )
                    continue
                if written is None:
                    logger.debug(
                        "position %s was closed while a tick was revaluing it; skipped",
                        position.position_id,
                    )
                    continue
                position.volume = Volume(written["volume"])
                position.profit = Money(written["profit"], position.profit.currency)
                position.price_current = price_obj
                repriced[position.position_id] = position
                continue

            position.update_unrealized_pnl(price_obj, conversion_rate)
            repriced[position.position_id] = position
            legacy_write = True

        # 5. Update Account Equity and Evaluate Margin State
        for login, account in accounts.items():
            if self.position_index and self.position_index.is_ready:
                fetched = self.position_index.get_by_account(login)
            else:
                _now = asyncio.get_event_loop().time()
                _cached_at = self._account_positions_cached_at.get(login)
                fetched = self._account_positions_cache.get(login)
                if (
                    fetched is None
                    or _cached_at is None
                    or (_now - _cached_at) >= self.account_read_cache_seconds
                ):
                    fetched = await self.position_repo.get_by_account(login)
                    self._account_positions_cache[login] = fetched
                    self._account_positions_cached_at[login] = _now

            seen = {x.position_id for x in fetched}
            all_positions = [repriced.get(x.position_id, x) for x in fetched]
            all_positions.extend(
                p for pid, p in repriced.items()
                if p.account_login == login and pid not in seen and p.time_done is None
            )

            total_pnl_amount = sum(p.profit.amount for p in all_positions)
            total_pnl_money = Money(total_pnl_amount, account.currency)

            account.update_equity(total_pnl_money)
            state_events = account.evaluate_margin_state()

            # Persist valuation updates
            _update_valuation = getattr(self.account_repo, "update_valuation", None)
            _rows = await _update_valuation(account) if _update_valuation is not None else None
            if _rows is None:
                logger.warning(
                    "account_repo %s has no update_valuation(); falling back to full-row save",
                    type(self.account_repo).__name__,
                )
                await self.account_repo.save(account)

            if legacy_write:
                if not self._warned_full_row_save:
                    self._warned_full_row_save = True
                    logger.warning(
                        "position_repo %s has no update_valuation(); falling back to full-row save",
                        type(self.position_repo).__name__,
                    )
                for p in all_positions:
                    await self.position_repo.save(p)

            # Emit domain events for UI/Notifications/Risk Workers
            for evt_dict in state_events:
                await self._emit_margin_event(evt_dict, account)

    async def _emit_margin_event(self, evt_dict: dict, account: Account) -> None:
        """Converts state machine dict to Domain Event and publishes."""
        event_type = evt_dict.get("event_type")
        event_map = {
            "MarginCallEntered": MarginCallEntered,
            "MarginCallExited": MarginCallExited,
            "StopOutEntered": StopOutEntered,
            "StopOutExited": StopOutExited,
        }
        event_class = event_map.get(event_type)
        if event_class:
            event = event_class(aggregate_id=str(account.login), payload=evt_dict)
            await self.event_bus.publish(event)
            logger.warning(
                "Margin State Change: %s for Account %s | Level: %s",
                event_type, account.login, evt_dict.get("margin_level"),
            )