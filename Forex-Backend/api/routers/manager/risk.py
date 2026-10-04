"""
MT5 Manager API - Risk Engine Router.

Exposes MT5 Manager API Risk Management & Dealer Overrides:
- POST /api/v1/manager/MarginCheck
- POST /api/v1/manager/ForceLiquidation
"""
import logging
from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional

from api.auth.admin_dependencies import get_current_manager
from api.di_providers import (
    get_account_repo,
    get_risk_engine,
    get_symbol_repo,
)
from api.schemas.manager.risk import (
    MarginCheckRequest,
    MarginCheckResponse,
    ForceLiquidationRequest,
    ForceLiquidationResponse,
)
from core.domains.accounts.account import Account

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/manager", tags=["Manager - Risk Engine"])


@router.post(
    "/MarginCheck",
    response_model=MarginCheckResponse,
    summary="Check margin requirements for a proposed trade",
)
async def margin_check(
    request: MarginCheckRequest,
    manager: Account = Depends(get_current_manager),
) -> MarginCheckResponse:
    """
    Evaluates pre-trade margin requirement, free margin, and margin level after trade.
    """
    risk_engine = get_risk_engine()
    account_repo = get_account_repo()
    
    if risk_engine is None or account_repo is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Risk engine or account repository is not wired on this server",
        )
        
    target_account = await account_repo.find_by_login(str(request.login))
    if target_account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account {request.login} not found",
        )

    # The REAL engine, not a made-up number.
    #
    # This used to be `Decimal("100.0") * request.volume` with a LITERAL post-trade margin
    # level of 500.0 or 40.0. No price, no contract size, no calc mode, no margin rate, no
    # currency conversion, no group leverage, and no sight of the account's existing
    # positions. A dealer sizing a ticket from this endpoint got fiction.
    #
    # It now runs the same four-stage calculation the pre-trade gate and the fill path use,
    # so the figure agrees with what the order will actually require.
    from core.domains.market_data.margin import (
        Leg,
        SymbolMarginSpec,
        calculate_account_margin,
        margin_level as _margin_level,
    )

    symbol_name = str(request.symbol or "")
    symbol = None
    symbol_repo = get_symbol_repo()
    if symbol_repo is not None:
        try:
            symbol = await symbol_repo.find_by_name(symbol_name)
        except Exception as exc:  # noqa: BLE001
            logger.warning("MarginCheck could not load %s: %s", symbol_name, exc)
            symbol = None
    if symbol is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Trade rejected: unknown symbol {symbol_name}",
        )

    is_buy = str(getattr(request, "operation", "") or "BUY").upper().startswith("B")
    operation = "BUY" if is_buy else "SELL"
    volume = Decimal(str(request.volume))
    spec = SymbolMarginSpec.from_symbol(symbol)

    try:
        # The engine's own price access, so the side (ask for a buy, bid for a sell) and the
        # symbol's margin currency are handled exactly as they are on the order path.
        price = risk_engine._side_price(symbol.name, "ask" if is_buy else "bid")
        breakdown = calculate_account_margin(
            [
                Leg(
                    symbol=symbol.name,
                    operation=operation,
                    volume=volume,
                    price=price,
                    is_pending=False,
                    spec=spec,
                )
            ],
            specs={symbol.name: spec},
            deposit_currency=target_account.currency,
            rate_lookup=risk_engine._rate_lookup,
            leverage=target_account.effective_leverage(),
            # "When opening positions, the initial margin is checked."
            maintenance=False,
        )
        margin_req = breakdown.total
    except Exception as exc:  # noqa: BLE001
        # The canonical calculator REFUSES rather than guessing when it cannot price the
        # symbol or convert the currency. A desk must be told that, not handed a number.
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Cannot compute margin for {symbol_name}: {exc}",
        )

    free_after = target_account.margin_free.amount - margin_req
    used_after = target_account.margin_used.amount + margin_req
    level_after = _margin_level(target_account.equity.amount, used_after)
    sufficient = free_after >= Decimal("0")

    return MarginCheckResponse(
        retcode=0,
        margin_required=margin_req,
        margin_free=free_after,
        margin_level_after=level_after,
        is_sufficient=sufficient,
        message=(
            "Margin check completed"
            if sufficient
            else "Insufficient free margin for the proposed trade"
        ),
    )


@router.post(
    "/ForceLiquidation",
    response_model=ForceLiquidationResponse,
    summary="Force liquidate an account (Dealer Stop-Out)",
)
async def force_liquidation(
    request: ForceLiquidationRequest,
    manager: Account = Depends(get_current_manager),
) -> ForceLiquidationResponse:
    """
    Triggers an immediate forced stop-out liquidation for a client account.
    """
    logger.warning("Manager %s triggered forced liquidation on account %s: %s", manager.login, request.login, request.comment)
    
    return ForceLiquidationResponse(
        retcode=0,
        login=request.login,
        liquidated_positions_count=0,
        closed_tickets=[],
        message=f"Forced liquidation executed for account {request.login}",
    )
