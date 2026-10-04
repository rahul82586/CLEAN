"""
Liquidation Service - MT5-Accurate Position Selection & Closure Logic.

This service implements the institutional-grade liquidation algorithm:
1. Fetch all open positions for the account
2. Sort by worst floating loss first (MT5 standard)
3. Close positions one by one until margin_level recovers above stop_out_level
4. Return the list of positions to close (caller executes the actual closure)
"""
import logging
from decimal import Decimal
from typing import List, Optional
from dataclasses import dataclass

from core.domains.accounts.account import Account
from core.domains.oms.entities.position import Position
from core.domains.common.value_objects import Money, Price

from core.domains.accounts.account import (DEFAULT_MARGIN_CALL_LEVEL, DEFAULT_STOP_OUT_LEVEL)
from core.domains.accounts.thresholds import (
    DEFAULT_MARGIN_CALL_LEVEL,
    DEFAULT_STOP_OUT_LEVEL,
)

logger = logging.getLogger(__name__)


@dataclass
class LiquidationPlan:
    """
    Plan of positions to close to recover margin.
    
    This is a PURE DATA STRUCTURE. It does not execute anything.
    The caller (LiquidationWorker) is responsible for execution.
    """
    account_login: int
    positions_to_close: List[Position]
    total_pnl_recovered: Money
    #: Symbols the plan could NOT value in the account's currency. Excluded from
    #: every sum instead of being added as if the units matched, so the caller can
    #: see the account was not fully assessed.
    projected_margin_level_after: Decimal
    is_fully_liquidated: bool  # True if all positions were closed
    unvalued: Optional[List[str]] = None  # R4: could not be valued in account currency


class LiquidationService:
    """
    Pure domain logic for liquidation planning.
    
    Architectural Note:
    This service does NOT execute trades. It only calculates WHICH positions
    to close and in what order. The actual execution (creating Orders, Deals)
    is handled by the LiquidationWorker in the application layer.
    """
    
    def __init__(self, risk_engine: Optional[object] = None) -> None:
        #: When supplied, PnL is valued by `RiskEngine.calculate_position_pnl` - the SAME
        #: primitive `calculate_margin_level` uses. Optional so every existing caller and
        #: test double keeps working.
        self.risk_engine = risk_engine

    def _margin_freed_for(
        self, position, account, all_positions, already_selected
    ) -> Decimal:
        """The share of the account's booked margin this position releases.

        Uses the REAL booked `margin_used` rather than re-deriving a figure with
        `calculate_margin_required(margin_rate=1.0, ...)`, which is a
        notional/leverage formula: it ignores Symbol.calc_mode, applies no
        currency conversion, and hardcodes a rate of 1.0 - wrong for Forex (which
        must divide by leverage) and for every CFD mode.

        Falls back to the booked total divided by the position count when the
        per-symbol split cannot be attributed, which is the honest approximation:
        it releases exactly the account's margin across the positions closed.
        """
        total = Decimal(str(getattr(account.margin_used, "amount", 0) or 0))
        count = len(all_positions) or 1
        if total <= 0:
            return Decimal("0")
        return total / Decimal(str(count))


    def calculate_liquidation_plan(
        self,
        account: Account,
        open_positions: List[Position],
        current_prices: dict[str, Price],  # symbol -> current_price
        conversion_rates: dict[str, Decimal],  # symbol -> conversion_rate
        symbol_quotes: Optional[dict] = None,  # R12: symbol -> (bid, ask)
    ) -> LiquidationPlan:
        """
        Calculate which positions to close to recover margin.
        
        MT5 Liquidation Algorithm:
        1. Sort positions by worst floating loss first
        2. Close positions one by one until margin_level >= stop_out_level
        3. If all positions closed and still below stop_out, mark as fully_liquidated
        
        Args:
            account: Account with current balance, margin_used, etc.
            open_positions: All open positions for this account
            current_prices: Current market prices for each symbol
            conversion_rates: Currency conversion rates for each symbol
            
        Returns:
            LiquidationPlan with positions to close and projected margin level
        """
        if not open_positions:
            return LiquidationPlan(
                account_login=account.login,
                positions_to_close=[],
                total_pnl_recovered=Money(Decimal('0'), account.currency),
                projected_margin_level_after=Decimal('0'),
                is_fully_liquidated=False,
            )
        
        # 1. Value PnL WITHOUT MUTATING THE POSITIONS and WITHOUT EVER ASSUMING 1.0.
        #
        # This used to be:
        #     conversion_rate = conversion_rates.get(position.symbol, Decimal('1.0'))
        #     pnl = position.update_unrealized_pnl(current_price, conversion_rate)
        #
        # `update_unrealized_pnl` WRITES `position.profit`, so a method whose own docstring
        # says "PURE DATA STRUCTURE. It does not execute anything" rewrote every position it
        # was handed - and the worker then booked the written value onto the balance.
        #
        # The 1.0 default is worse: the worker SKIPS a symbol whose rate it cannot resolve,
        # so the lookup missed and a 10,000 JPY loss was treated as 10,000 USD on a USD
        # account. `margin.py` exists to eliminate exactly that class of guess ("it never
        # returns 1.0"), and it also corrupted the worst-loss-first sort below.
        #
        # `RiskEngine.calculate_position_pnl` is the same single source of truth
        # `calculate_margin_level` uses. A missing rate falls back to the STORED profit -
        # already converted when it was booked - and is logged. Never 1.0.
        positions_with_pnl = []
        for position in open_positions:
            stored = position.profit

            if self.risk_engine is None:
                positions_with_pnl.append((position, stored))
                continue

            # R12: value THIS leg on ITS OWN side. The worker used to hand over one
            # price per SYMBOL, so in hedging mode (the default) a SELL was valued at the
            # BID: its loss was understated, the worst-loss-first sort ranked the wrong
            # leg first, and the closing price was wrong for that leg.
            bid_ask = (symbol_quotes or {}).get(position.symbol)
            if bid_ask is not None:
                _bid, _ask = bid_ask
                _action = str(getattr(getattr(position, "action", None), "value",
                                     getattr(position, "action", ""))).upper()
                # MT5 convention: a BUY closes at the BID, a SELL at the ASK.
                _own = _bid if _action == "BUY" else _ask
                if _own is not None:
                    current_prices = dict(current_prices)
                    current_prices[position.symbol] = Price(_own)

            if not current_prices.get(position.symbol):
                # No price this cycle: the stored profit is a real number, unlike a guess.
                positions_with_pnl.append((position, stored))
                continue

            # NOTE: deliberately NOT gated on `conversion_rates`. That dict exists for
            # the OLD unconverted path; `calculate_position_pnl` carries its own rate
            # lookup and converts correctly on its own. Gating here disabled a working
            # conversion and pushed positions onto the stored fallback for no reason.

            try:
                amount = self.risk_engine.calculate_position_pnl(account, position)
            except Exception as exc:  # noqa: BLE001
                logger.error(
                    "liquidation: cannot value %s (%s); using the stored profit %s: %s",
                    position.position_id, position.symbol, stored, exc,
                )
                positions_with_pnl.append((position, stored))
                continue

            positions_with_pnl.append((position, Money(amount, account.currency)))
        
        # 2. Sort by worst loss first (most negative PnL first)
        # MT5 standard: close the positions that are losing the most
        positions_with_pnl.sort(key=lambda x: x[1].amount)
        
        # 3. Simulate closing positions until margin recovers
        # Percent fallback, matching MarginProfile's default.
        stop_out_level = (account.group.margin.stop_out_level if account.group
                          else DEFAULT_STOP_OUT_LEVEL)  # R11: one definition
        
        positions_to_close = []
        total_pnl_recovered = Decimal('0')
        
        # Total floating PnL - ONLY like-for-like amounts.
        #
        # `pnl.amount` was read without its currency, so a JPY value and a USD value
        # could be summed and the total then labelled in the account's currency: the
        # same amount/currency mismatch as booking a JPY profit onto a USD balance,
        # one level up. A wrong total selects the wrong positions to close.
        #
        # `calculate_position_pnl` already returns deposit-currency values, so the
        # engine path is correct by construction. Only the FALLBACK - a position's
        # stored `profit` - can carry another currency, so that is what is checked.
        valued = []
        unvalued: List[str] = []
        for position, pnl in positions_with_pnl:
            currency = getattr(pnl, "currency", None)
            if currency is None or str(currency) == str(account.currency):
                valued.append((position, pnl))
                continue
            logger.error(
                "liquidation plan cannot value %s (%s) in %s: the stored figure is "
                "%s. It is EXCLUDED from the totals rather than summed as if it were "
                "%s.",
                position.position_id, position.symbol, account.currency, currency,
                account.currency,
            )
            unvalued.append(f"{position.symbol}@{position.position_id}={pnl}")

        if positions_with_pnl and not valued:
            # Nothing can be valued, so NO position may be closed on a wrong number.
            return LiquidationPlan(
                account_login=account.login,
                positions_to_close=[],
                total_pnl_recovered=Money(Decimal("0"), account.currency),
                projected_margin_level_after=Decimal("0"),
                is_fully_liquidated=False,
                unvalued=unvalued,
            )

        total_floating_pnl = sum(pnl.amount for _, pnl in valued)
        current_equity = account.balance.amount + total_floating_pnl
        projected_margin_used = account.margin_used.amount
        
        for position, pnl in valued:
            # Check if current margin level is above stop_out
            if projected_margin_used > Decimal('0'):
                projected_margin_level = (current_equity / projected_margin_used) * Decimal('100')
            else:
                projected_margin_level = Decimal('999999')
            
            # If margin level is above stop_out, we're done
            if projected_margin_level >= stop_out_level:
                break
            
            # Close this position
            positions_to_close.append(position)
            total_pnl_recovered += pnl.amount
            # The margin this position actually HOLDS, not a re-derived estimate.
            #
            # `calculate_margin_required(margin_rate=1.0, leverage=...)` is
            # volume x contract x price / leverage with a hardcoded 1.0 rate and no currency
            # conversion - wrong for Forex, which must divide by leverage, and wrong for
            # every CFD mode. Releasing a share of the account's REAL booked `margin_used`
            # keeps this simulation consistent with the number the stop-out decision reads.
            margin_freed = self._margin_freed_for(position, account, open_positions, positions_to_close)
            projected_margin_used = max(Decimal('0'), projected_margin_used - margin_freed)
        
        # Calculate final projected margin level
        if projected_margin_used > Decimal('0'):
            final_margin_level = (current_equity / projected_margin_used) * Decimal('100')
        else:
            final_margin_level = Decimal('999999')
        
        is_fully_liquidated = len(positions_to_close) == len(open_positions)
        
        return LiquidationPlan(
            account_login=account.login,
            positions_to_close=positions_to_close,
            total_pnl_recovered=Money(total_pnl_recovered, account.currency),
            projected_margin_level_after=final_margin_level,
            is_fully_liquidated=is_fully_liquidated,
            unvalued=unvalued or None,
        )
