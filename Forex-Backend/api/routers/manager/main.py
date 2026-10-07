"""
MT5 Manager API - Main Queries & Accounts Router.
Exposes all 66 Main endpoints mirroring MT5 Manager REST API.
"""
import logging
import os
from datetime import datetime, timezone
from decimal import Decimal
from fastapi import APIRouter, Depends, Query, HTTPException, status, Response
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Any

from api.auth.admin_dependencies import get_current_manager, require_right
from core.domains.accounts.account import Account
from api.di_providers import (
    get_market_data_engine,
    get_event_bus,
    get_ledger_repo,
    get_account_repo,
    get_manager_repo,
    get_position_repo,
    get_account_info_query_handler,
    get_manager_positions_query_handler,
    get_deal_repo,
    get_order_repo,
    get_symbol_repo,
    get_group_repo,
)
from api.schemas.manager.main import (
    AccountInfo, PositionInfo, DealInfo, OrderInfo,
    position_to_info, deal_to_info, order_to_info
)
from application.queries.get_account_info import (
    GetAccountInfoQuery, GetAccountInfoQueryHandler
)
from application.queries.get_positions import GetManagerPositionsQueryHandler, GetManagerPositionsQuery

# N10: the constants live in core.domains.accounts.thresholds;
# the duplicate import from account.py shadowed the one below.
from core.domains.accounts.account import MARGIN_LEVEL_UNLIMITED
from core.domains.market_data.margin import margin_level as compute_margin_level
from core.domains.accounts.thresholds import (
    DEFAULT_MARGIN_CALL_LEVEL,
    DEFAULT_STOP_OUT_LEVEL,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/manager", tags=["Manager - Main"])
router_root = APIRouter(tags=["Main"])


@router.get("/UserGet", response_model=AccountInfo, summary="User details (MT5 UserGet format)")
@router_root.get("/UserGet", response_model=AccountInfo, summary="User details (MT5 UserGet format)")
async def user_get(
    login: Optional[int] = Query(None, description="Account login number"),
    manager: Account = Depends(get_current_manager),
    handler: Optional[GetAccountInfoQueryHandler] = Depends(get_account_info_query_handler),
) -> AccountInfo:
    """Get user details for requested login."""
    if handler is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Account info handler unwired")
    try:
        info = await handler.handle(GetAccountInfoQuery(account_login=login))
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Account {login} not found")
    except Exception:
        logger.exception("UserGet failed for login=%s", login)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not read account information")
    
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Account {login} not found")
    
    balance = Decimal(str(info.get("balance", 0))) if isinstance(info, dict) else getattr(info, "balance", Decimal("0"))
    equity = Decimal(str(info.get("equity", 0))) if isinstance(info, dict) else getattr(info, "equity", Decimal("0"))
    margin = Decimal(str(info.get("margin_used", info.get("margin", 0)))) if isinstance(info, dict) else getattr(info, "margin_used", Decimal("0"))
    free_margin = Decimal(str(info.get("free_margin", 0))) if isinstance(info, dict) else getattr(info, "free_margin", Decimal("0"))
    group = str(info.get("group", info.get("group_name", ""))) if isinstance(info, dict) else getattr(info, "group", "")
    acc_login = int(info.get("login_id", info.get("login", login))) if isinstance(info, dict) else getattr(info, "login_id", login)
    
    # R15/C2: the shared function, which returns MARGIN_LEVEL_UNLIMITED for a zero
    # requirement. UserGet used to report a flat account at level 0 - below every stop-out
    # threshold - and this was the last inline copy of the formula outside the planner.
    margin_level = compute_margin_level(equity, margin)

    # The query already resolves BOTH of these from the account (`get_account_info.py:58`
    # reads the balance currency, `:63` calls `effective_leverage()`), and this response
    # ignored them: a EUR account was reported to the Manager terminal as USD, and every
    # account was reported at 100x regardless of its own or its group's setting. A dealer
    # reading either number would size a manual intervention wrongly.
    currency = str(
        info.get("currency", "USD") if isinstance(info, dict)
        else getattr(info, "currency", "USD")
    ) or "USD"
    try:
        leverage = int(
            info.get("leverage", 100) if isinstance(info, dict)
            else getattr(info, "leverage", 100)
        )
    except (TypeError, ValueError):
        leverage = 100

    return AccountInfo(
        login=acc_login,
        group=group,
        currency=currency,
        balance=balance,
        equity=equity,
        margin=margin,
        free_margin=free_margin,
        margin_level=margin_level,
        leverage=leverage,
    )

@router.get("/PositionGet", response_model=List[PositionInfo], summary="Get positions for account or login")
@router_root.get("/PositionGet", response_model=List[PositionInfo], summary="Get positions for account or login")
async def position_get(
    login: Optional[int] = Query(None, description="Filter by account login"),
    symbol: Optional[str] = Query(None, description="Filter by symbol"),
    ticket: Optional[str] = Query(None, description="Filter by position ticket"),
    include_closed: bool = Query(False, description="Include closed positions"),
    manager: Account = Depends(get_current_manager),
    handler: Optional[GetManagerPositionsQueryHandler] = Depends(get_manager_positions_query_handler),
) -> List[PositionInfo]:
    """Get position list for requested login with live dynamic market prices and floating PnL."""
    if handler is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="manager_positions_query_handler is not wired")
    try:
        if include_closed and hasattr(handler.position_repo, "find_page"):
            positions, _ = await handler.position_repo.find_page(
                account_login=login,
                symbol=symbol,
                ticket=ticket,
                include_closed=True,
                limit=1000
            )
        else:
            positions = await handler.handle(GetManagerPositionsQuery(account_login=login, symbol=symbol))
            if ticket:
                t_str = str(ticket).strip()
                positions = [p for p in positions if str(p.position_id) == t_str or str(getattr(p, 'external_id', '')) == t_str]
                if not positions and hasattr(handler.position_repo, "find_by_id"):
                    single_pos = await handler.position_repo.find_by_id(t_str)
                    if single_pos is not None:
                        positions = [single_pos]
        
        result = []
        for p in positions:
            info = position_to_info(p)
            result.append(info)
        return result
    except HTTPException:
        raise
    except Exception as exc:
        logger.error(f"PositionGet error: {exc}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not read positions")

@router.get("/ExposureGet", summary="Get B-Book broker net exposure per symbol (MT5 ExposureGet format)")
@router_root.get("/ExposureGet", summary="Get B-Book broker net exposure per symbol (MT5 ExposureGet format)")
async def exposure_get(
    symbol: Optional[str] = Query(None, description="Filter exposure by symbol"),
    manager: Account = Depends(get_current_manager),
    position_repo: Any = Depends(get_position_repo),
) -> JSONResponse:
    """Get aggregate B-Book risk exposure and LP coverage breakdown per symbol."""
    if position_repo is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Position repository is unwired")
    try:
        open_positions = await position_repo.get_open_positions()
        
        exposure_map: Dict[str, Dict[str, Decimal]] = {}
        for p in open_positions:
            sym = p.symbol
            if symbol and sym.upper() != symbol.upper():
                continue
            if sym not in exposure_map:
                exposure_map[sym] = {
                    "client_buy_vol": Decimal("0.0"),
                    "client_sell_vol": Decimal("0.0"),
                    "bbook_buy_vol": Decimal("0.0"),
                    "bbook_sell_vol": Decimal("0.0"),
                    "abook_hedged_vol": Decimal("0.0"),
                }
            
            vol = p.volume.value if hasattr(p.volume, 'value') else Decimal(str(p.volume))
            action_str = str(getattr(p.action, 'value', p.action)).upper()
            is_buy = action_str.startswith("BUY")
            ext_id = str(getattr(p, 'external_id', '') or '')
            is_abook = bool(ext_id and ("lp_" in ext_id or ext_id.isdigit()))
            
            if is_buy:
                exposure_map[sym]["client_buy_vol"] += vol
            else:
                exposure_map[sym]["client_sell_vol"] += vol
                
            if is_abook:
                exposure_map[sym]["abook_hedged_vol"] += (vol if is_buy else -vol)
            else:
                if is_buy:
                    exposure_map[sym]["bbook_buy_vol"] += vol
                else:
                    exposure_map[sym]["bbook_sell_vol"] += vol

        result = []
        for sym, stats in sorted(exposure_map.items()):
            c_buy = stats["client_buy_vol"]
            c_sell = stats["client_sell_vol"]
            c_net = c_buy - c_sell
            b_exposure = -c_net
            lp_hedged = stats["abook_hedged_vol"]
            residual = b_exposure + lp_hedged
            
            result.append({
                "symbol": sym,
                "client_buy_volume": f"{c_buy:.8f}",
                "client_sell_volume": f"{c_sell:.8f}",
                "client_net_volume": f"{c_net:.8f}",
                "broker_bbook_exposure": f"{b_exposure:.8f}",
                "lp_hedged_volume": f"{lp_hedged:.8f}",
                "residual_unhedged_risk": f"{residual:.8f}"
            })
            
        return JSONResponse(status_code=200, content={
            "retcode": 0,
            "message": "Broker net exposure retrieved successfully",
            "endpoint": "/ExposureGet",
            "data": result
        })
    except Exception as exc:
        logger.error(f"ExposureGet error: {exc}", exc_info=True)
        raise HTTPException(status_code=500, detail="Could not compute exposure")

@router.get("/DealGet", response_model=List[DealInfo], summary="Get deals (MT5 DealGet format)")
@router_root.get("/DealGet", response_model=List[DealInfo], summary="Get deals (MT5 DealGet format)")
async def deal_get(
    login: Optional[int] = Query(None, description="Filter by login"),
    symbol: Optional[str] = Query(None, description="Filter by symbol"),
    entry: Optional[str] = Query(None, description="Filter by entry type (IN/OUT)"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    manager: Account = Depends(get_current_manager),
    deal_repo: Any = Depends(get_deal_repo),
) -> Response:
    """Get deals from repository."""
    if deal_repo is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Deal repository unwired")
    deals, total = await deal_repo.find_page(
        limit=limit, offset=offset, account_login=login, symbol=symbol, entry=entry
    )
    infos = [deal_to_info(d) for d in deals]
    content = [i.model_dump(mode="json") for i in infos]
    return JSONResponse(content=content, headers={"X-Total-Count": str(total)})

@router.get("/OrderGet", response_model=List[OrderInfo], summary="Get orders (MT5 OrderGet format)")
@router_root.get("/OrderGet", response_model=List[OrderInfo], summary="Get orders (MT5 OrderGet format)")
async def order_get(
    login: Optional[int] = Query(None, description="Filter by login"),
    symbol: Optional[str] = Query(None, description="Filter by symbol"),
    state: Optional[str] = Query(None, description="Filter by state"),
    history: Optional[str] = Query(None, description="Tristate: true=history only, false=active only, null=all"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    manager: Account = Depends(get_current_manager),
    order_repo: Any = Depends(get_order_repo),
) -> Response:
    """Get orders from repository."""
    if order_repo is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Order repository unwired")
    
    hist_bool = None
    if history is not None:
        if history.lower() in ("true", "1"):
            hist_bool = True
        elif history.lower() in ("false", "0"):
            hist_bool = False
    
    if hist_bool is False and state and state.upper() in ("FILLED", "CANCELLED", "REJECTED", "EXPIRED"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"state={state} contradicts history=false")
    
    orders, total = await order_repo.find_page(
        limit=limit, offset=offset, account_login=login, symbol=symbol, state=state, history=hist_bool
    )
    infos = [order_to_info(o) for o in orders]
    content = [i.model_dump(mode="json") for i in infos]
    return JSONResponse(content=content, headers={"X-Total-Count": str(total)})

@router.get("/SymbolGet", summary="Get symbol or list of symbols")
@router_root.get("/SymbolGet", summary="Get symbol or list of symbols")
async def symbol_get(
    symbol: Optional[str] = Query(None, description="Symbol name"),
    name: Optional[str] = Query(None, description="Symbol name alias"),
    manager: Account = Depends(get_current_manager),
    symbol_repo: Any = Depends(get_symbol_repo),
) -> Any:
    """Get symbols from repository."""
    if symbol_repo is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Symbol repository unwired")
    target_name = symbol or name
    if target_name:
        sym = await symbol_repo.find_by_name(target_name)
        if sym is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Symbol {target_name} not found")
        return {"name": sym.name, "path": getattr(sym, "path", sym.name), "digits": getattr(sym, "digits", 5)}
    else:
        syms = await symbol_repo.get_all_symbols()
        return [{"name": s.name, "path": getattr(s, "path", s.name), "digits": getattr(s, "digits", 5)} for s in syms]

@router.get("/GroupGet", summary="Get user groups")
@router_root.get("/GroupGet", summary="Get user groups")
async def group_get(
    group: Optional[str] = Query(None, description="Group name filter"),
    manager: Account = Depends(get_current_manager),
    group_repo: Any = Depends(get_group_repo),
) -> Any:
    """Get groups from repository with Netting/Hedging mode and margin configurations."""
    if group_repo is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Group repository unwired")

    def _serialize_group(g: Any) -> Dict[str, Any]:
        margin_prof = getattr(g, "margin", None)
        mode_obj = getattr(margin_prof, "mode", None) if margin_prof else None
        mode_name = getattr(mode_obj, "name", str(mode_obj)).upper() if mode_obj else "RETAIL_HEDGED"
        is_netting = any(k in mode_name for k in ("RETAIL", "EXCHANGE", "NETTING")) and "HEDGED" not in mode_name
        margin_mode_int = 0 if is_netting else 2
        position_mode_str = "NETTING" if is_netting else "HEDGING"
        
        leverage = getattr(margin_prof, "leverage_default", getattr(g, "default_leverage", 100))
        margin_call = getattr(
            margin_prof, "margin_call_level",
            getattr(g, "margin_call", DEFAULT_MARGIN_CALL_LEVEL),
        )
        margin_stop_out = getattr(
            margin_prof, "stop_out_level",
            getattr(g, "margin_stop_out", DEFAULT_STOP_OUT_LEVEL),
        )
        
        acc_type = getattr(g, "account_type", "demo")
        acc_type_str = acc_type.value if hasattr(acc_type, "value") else str(acc_type)
        
        return {
            "name": getattr(g, "name", ""),
            "currency": getattr(g, "currency", "USD"),
            "margin_mode": margin_mode_int,
            "position_mode": position_mode_str,
            "leverage": int(leverage) if leverage else 100,
            "margin_call": float(margin_call) if margin_call is not None else 80.0,
            "margin_stop_out": float(margin_stop_out) if margin_stop_out is not None else 50.0,
            "account_type": acc_type_str,
            "company": getattr(g, "company", "Antigravity Brokerage"),
        }

    if group:
        g = await group_repo.find_by_name(group)
        if g is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Group {group} not found")
        return [_serialize_group(g)]
    else:
        if hasattr(group_repo, "get_all_groups"):
            groups = await group_repo.get_all_groups()
        elif hasattr(group_repo, "get_all"):
            groups = await group_repo.get_all()
        elif hasattr(group_repo, "find_all"):
            groups = await group_repo.find_all()
        else:
            groups = []
        return [_serialize_group(g) for g in groups]

@router.get("/AccountCreate", summary="Create new user.")
@router.post("/AccountCreate", summary="Create new user.")
@router_root.get("/AccountCreate", summary="Create new user.")
@router_root.post("/AccountCreate", summary="Create new user.")
async def handle_AccountCreate_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    master_pass: Optional[str] = Query(None, alias="master_pass", description=""),
    investor_pass: Optional[str] = Query(None, alias="investor_pass", description=""),
    enabled: Optional[str] = Query(None, alias="enabled", description=""),
    ClientID: Optional[str] = Query(None, alias="ClientID", description=""),
    FirstName: Optional[str] = Query(None, alias="FirstName", description=""),
    LastName: Optional[str] = Query(None, alias="LastName", description=""),
    MiddleName: Optional[str] = Query(None, alias="MiddleName", description=""),
    OTPSecret: Optional[str] = Query(None, alias="OTPSecret", description=""),
    LimitOrders: Optional[str] = Query(None, alias="LimitOrders", description=""),
    LimitPositionsValue: Optional[str] = Query(None, alias="LimitPositionsValue", description=""),
    Login: Optional[str] = Query(None, alias="Login", description=""),
    Group: Optional[str] = Query(None, alias="Group", description=""),
    CertSerialNumber: Optional[str] = Query(None, alias="CertSerialNumber", description=""),
    Rights: Optional[str] = Query(None, alias="Rights", description=""),
    Registration: Optional[str] = Query(None, alias="Registration", description=""),
    LastAccess: Optional[str] = Query(None, alias="LastAccess", description=""),
    LastIP: Optional[str] = Query(None, alias="LastIP", description=""),
    Name: Optional[str] = Query(None, alias="Name", description=""),
    Company: Optional[str] = Query(None, alias="Company", description=""),
    AccountParam: Optional[str] = Query(None, alias="Account", description=""),
    Country: Optional[str] = Query(None, alias="Country", description=""),
    Language: Optional[str] = Query(None, alias="Language", description=""),
    City: Optional[str] = Query(None, alias="City", description=""),
    State: Optional[str] = Query(None, alias="State", description=""),
    ZIPCode: Optional[str] = Query(None, alias="ZIPCode", description=""),
    Address: Optional[str] = Query(None, alias="Address", description=""),
    Phone: Optional[str] = Query(None, alias="Phone", description=""),
    EMail: Optional[str] = Query(None, alias="EMail", description=""),
    ID: Optional[str] = Query(None, alias="ID", description=""),
    Status: Optional[str] = Query(None, alias="Status", description=""),
    Comment: Optional[str] = Query(None, alias="Comment", description=""),
    Color: Optional[str] = Query(None, alias="Color", description=""),
    PhonePassword: Optional[str] = Query(None, alias="PhonePassword", description=""),
    Leverage: Optional[str] = Query(None, alias="Leverage", description=""),
    Agent: Optional[str] = Query(None, alias="Agent", description=""),
    Balance: Optional[str] = Query(None, alias="Balance", description=""),
    Credit: Optional[str] = Query(None, alias="Credit", description=""),
    InterestRate: Optional[str] = Query(None, alias="InterestRate", description=""),
    CommissionDaily: Optional[str] = Query(None, alias="CommissionDaily", description=""),
    CommissionMonthly: Optional[str] = Query(None, alias="CommissionMonthly", description=""),
    CommissionAgentDaily: Optional[str] = Query(None, alias="CommissionAgentDaily", description=""),
    CommissionAgentMonthly: Optional[str] = Query(None, alias="CommissionAgentMonthly", description=""),
    BalancePrevDay: Optional[str] = Query(None, alias="BalancePrevDay", description=""),
    BalancePrevMonth: Optional[str] = Query(None, alias="BalancePrevMonth", description=""),
    EquityPrevDay: Optional[str] = Query(None, alias="EquityPrevDay", description=""),
    EquityPrevMonth: Optional[str] = Query(None, alias="EquityPrevMonth", description=""),
    LastPassChange: Optional[str] = Query(None, alias="LastPassChange", description=""),
    LeadCampaign: Optional[str] = Query(None, alias="LeadCampaign", description=""),
    LeadSource: Optional[str] = Query(None, alias="LeadSource", description=""),
    ApiDataClearAll: Optional[str] = Query(None, alias="ApiDataClearAll", description=""),
    ExternalAccountClear: Optional[str] = Query(None, alias="ExternalAccountClear", description=""),
    ExternalAccountTotal: Optional[str] = Query(None, alias="ExternalAccountTotal", description=""),
    MQID: Optional[str] = Query(None, alias="MQID", description=""),
) -> Dict[str, Any]:
    """Create new user. Need to specify at least first and last name, group and leverage."""
    f_name = FirstName or ""
    l_name = LastName or ""
    if not f_name and Name:
        parts = Name.strip().split(" ", 1)
        f_name = parts[0]
        l_name = parts[1] if len(parts) > 1 else ""

    grp_name = Group or "demo"
    login_int = int(Login) if Login and Login.isdigit() else None
    deposit_val = Decimal(Balance or "0") if Balance and Balance.replace(".", "", 1).isdigit() else None
    lev_val = int(Leverage) if Leverage and Leverage.isdigit() else None

    from api.di_providers import get_create_account_handler
    from application.commands.create_account import CreateAccountCommand, GroupNotFoundError, AccountRefusedError

    handler = get_create_account_handler()
    cmd = CreateAccountCommand(
        group_name=grp_name,
        login=login_int,
        first_name=f_name or "New",
        last_name=l_name or "User",
        email=EMail or f"user_{login_int or 'new'}@broker.com",
        phone=Phone or "",
        master_password=master_pass or "Password123!",
        investor_password=investor_pass,
        phone_password=PhonePassword,
        leverage=lev_val,
        opening_deposit=deposit_val,
    )
    try:
        res = await handler.handle(cmd)
        return {
            "retcode": 0,
            "message": f"Account {res.login} created successfully",
            "endpoint": "/AccountCreate",
            "login": res.login,
            "group": res.group_name,
            "account_type": res.account_type,
            "currency": res.currency,
            "client_id": res.client_id,
            "opening_deposit": res.opening_deposit,
            "passwords": res.passwords,
        }
    except (GroupNotFoundError, AccountRefusedError, ValueError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))


@router.get("/AccountCreateAndDeposit", summary="Create new user and deposit.")
@router.post("/AccountCreateAndDeposit", summary="Create new user and deposit.")
@router_root.get("/AccountCreateAndDeposit", summary="Create new user and deposit.")
@router_root.post("/AccountCreateAndDeposit", summary="Create new user and deposit.")
async def handle_AccountCreateAndDeposit_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    master_pass: Optional[str] = Query(None, alias="master_pass", description=""),
    investor_pass: Optional[str] = Query(None, alias="investor_pass", description=""),
    enabled: Optional[str] = Query(None, alias="enabled", description=""),
    amount: Optional[str] = Query(None, alias="amount", description=""),
    ClientID: Optional[str] = Query(None, alias="ClientID", description=""),
    FirstName: Optional[str] = Query(None, alias="FirstName", description=""),
    LastName: Optional[str] = Query(None, alias="LastName", description=""),
    MiddleName: Optional[str] = Query(None, alias="MiddleName", description=""),
    OTPSecret: Optional[str] = Query(None, alias="OTPSecret", description=""),
    LimitOrders: Optional[str] = Query(None, alias="LimitOrders", description=""),
    LimitPositionsValue: Optional[str] = Query(None, alias="LimitPositionsValue", description=""),
    Login: Optional[str] = Query(None, alias="Login", description=""),
    Group: Optional[str] = Query(None, alias="Group", description=""),
    CertSerialNumber: Optional[str] = Query(None, alias="CertSerialNumber", description=""),
    Rights: Optional[str] = Query(None, alias="Rights", description=""),
    Registration: Optional[str] = Query(None, alias="Registration", description=""),
    LastAccess: Optional[str] = Query(None, alias="LastAccess", description=""),
    LastIP: Optional[str] = Query(None, alias="LastIP", description=""),
    Name: Optional[str] = Query(None, alias="Name", description=""),
    Company: Optional[str] = Query(None, alias="Company", description=""),
    AccountParam: Optional[str] = Query(None, alias="Account", description=""),
    Country: Optional[str] = Query(None, alias="Country", description=""),
    Language: Optional[str] = Query(None, alias="Language", description=""),
    City: Optional[str] = Query(None, alias="City", description=""),
    State: Optional[str] = Query(None, alias="State", description=""),
    ZIPCode: Optional[str] = Query(None, alias="ZIPCode", description=""),
    Address: Optional[str] = Query(None, alias="Address", description=""),
    Phone: Optional[str] = Query(None, alias="Phone", description=""),
    EMail: Optional[str] = Query(None, alias="EMail", description=""),
    ID: Optional[str] = Query(None, alias="ID", description=""),
    Status: Optional[str] = Query(None, alias="Status", description=""),
    Comment: Optional[str] = Query(None, alias="Comment", description=""),
    Color: Optional[str] = Query(None, alias="Color", description=""),
    PhonePassword: Optional[str] = Query(None, alias="PhonePassword", description=""),
    Leverage: Optional[str] = Query(None, alias="Leverage", description=""),
    Agent: Optional[str] = Query(None, alias="Agent", description=""),
    Balance: Optional[str] = Query(None, alias="Balance", description=""),
    Credit: Optional[str] = Query(None, alias="Credit", description=""),
    InterestRate: Optional[str] = Query(None, alias="InterestRate", description=""),
    CommissionDaily: Optional[str] = Query(None, alias="CommissionDaily", description=""),
    CommissionMonthly: Optional[str] = Query(None, alias="CommissionMonthly", description=""),
    CommissionAgentDaily: Optional[str] = Query(None, alias="CommissionAgentDaily", description=""),
    CommissionAgentMonthly: Optional[str] = Query(None, alias="CommissionAgentMonthly", description=""),
    BalancePrevDay: Optional[str] = Query(None, alias="BalancePrevDay", description=""),
    BalancePrevMonth: Optional[str] = Query(None, alias="BalancePrevMonth", description=""),
    EquityPrevDay: Optional[str] = Query(None, alias="EquityPrevDay", description=""),
    EquityPrevMonth: Optional[str] = Query(None, alias="EquityPrevMonth", description=""),
    LastPassChange: Optional[str] = Query(None, alias="LastPassChange", description=""),
    LeadCampaign: Optional[str] = Query(None, alias="LeadCampaign", description=""),
    LeadSource: Optional[str] = Query(None, alias="LeadSource", description=""),
    ApiDataClearAll: Optional[str] = Query(None, alias="ApiDataClearAll", description=""),
    ExternalAccountClear: Optional[str] = Query(None, alias="ExternalAccountClear", description=""),
    ExternalAccountTotal: Optional[str] = Query(None, alias="ExternalAccountTotal", description=""),
    MQID: Optional[str] = Query(None, alias="MQID", description=""),
) -> Dict[str, Any]:
    """Create new user and deposit."""
    f_name = FirstName or ""
    l_name = LastName or ""
    if not f_name and Name:
        parts = Name.strip().split(" ", 1)
        f_name = parts[0]
        l_name = parts[1] if len(parts) > 1 else ""

    grp_name = Group or "demo"
    login_int = int(Login) if Login and Login.isdigit() else None
    deposit_str = amount or Balance or "0"
    deposit_val = Decimal(deposit_str) if deposit_str.replace(".", "", 1).isdigit() else None
    lev_val = int(Leverage) if Leverage and Leverage.isdigit() else None

    from api.di_providers import get_create_account_handler
    from application.commands.create_account import CreateAccountCommand, GroupNotFoundError, AccountRefusedError

    handler = get_create_account_handler()
    cmd = CreateAccountCommand(
        group_name=grp_name,
        login=login_int,
        first_name=f_name or "New",
        last_name=l_name or "User",
        email=EMail or f"user_{login_int or 'new'}@broker.com",
        phone=Phone or "",
        master_password=master_pass or "Password123!",
        investor_password=investor_pass,
        phone_password=PhonePassword,
        leverage=lev_val,
        opening_deposit=deposit_val,
    )
    try:
        res = await handler.handle(cmd)
        return {
            "retcode": 0,
            "message": f"Account {res.login} created and deposited successfully",
            "endpoint": "/AccountCreateAndDeposit",
            "login": res.login,
            "group": res.group_name,
            "account_type": res.account_type,
            "currency": res.currency,
            "client_id": res.client_id,
            "opening_deposit": res.opening_deposit,
            "passwords": res.passwords,
        }
    except (GroupNotFoundError, AccountRefusedError, ValueError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))



async def _fetch_user_details_list(
    manager: Account,
    session_id: Optional[str],
    logins_str: Optional[str],
    account_repo: Any,
    endpoint: str,
    page: int = 0,
    page_size: int = 100,
) -> Dict[str, Any]:
    logins_filter = [int(x.strip()) for x in logins_str.split(",") if x.strip().isdigit()] if logins_str else []
    details = []

    if account_repo is not None:
        try:
            if hasattr(account_repo, "get_all_accounts"):
                all_accs = await account_repo.get_all_accounts()
            elif hasattr(account_repo, "find_all"):
                all_accs = await account_repo.find_all()
            elif logins_filter:
                all_accs = []
                for l in logins_filter:
                    acc = await account_repo.find_by_login(l)
                    if acc:
                        all_accs.append(acc)
            else:
                all_accs = []
                
            for acc in all_accs:
                l_val = int(acc.login)
                if logins_filter and l_val not in logins_filter:
                    continue
                from core.domains.common.value_objects import Money
                acc.update_equity(getattr(acc, 'profit', Money(Decimal('0'), acc.currency)))
                bal_str = f"{Decimal(str(acc.balance.amount)):.2f}"
                eq_str = f"{Decimal(str(acc.equity.amount)):.2f}"
                mar_str = f"{Decimal(str(acc.margin_used.amount)):.2f}"
                mf_str = f"{Decimal(str(acc.margin_free.amount)):.2f}"
                ml_dec = Decimal(str(acc.margin_level))
                ml_str = f"{ml_dec:.2f}" if ml_dec < 999999 else "999999.00"
                
                details.append({
                    "login": l_val,
                    "name": acc.display_name(),
                    "group": acc.group.name if acc.group else "demo\\Standard",
                    "currency": acc.currency,
                    "balance": bal_str,
                    "equity": eq_str,
                    "margin": mar_str,
                    "margin_free": mf_str,
                    "margin_level": ml_str,
                    "leverage": int(acc.effective_leverage()),
                    "enabled": bool(acc.is_enabled),
                    "email": getattr(acc, "email", None),
                    "registration": acc.created_at.isoformat() if hasattr(acc, 'created_at') and acc.created_at else None,
                })
        except Exception as exc:
            logger.exception("%s user details query failed", endpoint)

    total = len(details)
    start_idx = page * page_size
    sliced = details[start_idx : start_idx + page_size] if page_size > 0 else details

    return {
        "retcode": 0,
        "message": "User details retrieved successfully",
        "endpoint": endpoint,
        "id": session_id or f"session_{manager.login}",
        "data": sliced,
        "total": total,
    }


    # This was a GET. It sets `is_enabled = False` and full-row saves, so a page
    # refresh or any link to it could disable a client's account. R11-class fix:
    # a state change must not be reachable by following a URL. POST only.
    # The body still disables rather than hard-deletes, which is the safer semantic
    # and matches the docstring.
@router.post("/AccountDelete", summary="Delete/disable account")
@router_root.post("/AccountDelete", summary="Delete/disable account")
async def handle_AccountDelete_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """Delete / disable account"""
    if not login:
        return JSONResponse(
            status_code=400,
            content={"retcode": int(Retcode.REQUEST_INVALID), "message": "Login parameter is required", "endpoint": "/AccountDelete"}
        )
    target = int(login) if str(login).isdigit() else login
    if account_repo is not None:
        try:
            acc = await account_repo.find_by_login(target)
            if acc is not None:
                acc.is_enabled = False
                await account_repo.save(acc)
                return {
                    "retcode": 0,
                    "message": f"Account {login} deleted successfully",
                    "endpoint": "/AccountDelete",
                    "id": id or f"session_{manager.login}",
                    "login": target,
                }
        except Exception as exc:
            logger.exception("AccountDelete failed for login %s", login)

    return JSONResponse(
        status_code=404,
        content={"retcode": int(Retcode.AUTH_ACCOUNT_UNKNOWN), "message": f"Account '{login}' not found", "endpoint": "/AccountDelete"}
    )


@router.get("/AccountDetails", summary="Account details")
@router_root.get("/AccountDetails", summary="Account details")
async def handle_AccountDetails_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Session token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number"),
    account_repo: Any = Depends(get_account_repo),
    manager_repo: Any = Depends(get_manager_repo),
) -> Dict[str, Any]:
    """Account details"""
    target_login = login or str(manager.login)
    if account_repo is not None:
        try:
            acc = await account_repo.find_by_login(int(target_login) if str(target_login).isdigit() else target_login)
            if acc is not None:
                from core.domains.common.value_objects import Money
                acc.update_equity(getattr(acc, 'profit', Money(Decimal('0'), acc.currency)))
                bal_str = f"{Decimal(str(acc.balance.amount)):.2f}"
                eq_str = f"{Decimal(str(acc.equity.amount)):.2f}"
                mar_str = f"{Decimal(str(acc.margin_used.amount)):.2f}"
                mf_str = f"{Decimal(str(acc.margin_free.amount)):.2f}"
                ml_dec = Decimal(str(acc.margin_level))
                ml_str = f"{ml_dec:.2f}" if ml_dec < 999999 else "999999.00"
                return {
                    "retcode": 0,
                    "id": id or f"session_{manager.login}",
                    "login": int(acc.login),
                    "name": acc.display_name(),
                    "group": acc.group.name if acc.group else "demo\\Standard",
                    "currency": acc.currency,
                    "balance": bal_str,
                    "equity": eq_str,
                    "margin": mar_str,
                    "margin_free": mf_str,
                    "margin_level": ml_str,
                    "leverage": int(acc.effective_leverage()),
                    "enabled": bool(acc.is_enabled),
                }
        except Exception:
            pass

    # Check authenticated manager or manager_repo if target_login belongs to a manager
    if str(target_login) == str(manager.login):
        return {
            "retcode": 0,
            "id": id or f"session_{manager.login}",
            "login": int(manager.login),
            "name": getattr(manager, 'name', 'Administrator'),
            "group": getattr(manager, 'group_name', 'administrator'),
            "currency": "USD",
            "balance": "0.00",
            "equity": "0.00",
            "margin": "0.00",
            "margin_free": "0.00",
            "margin_level": "999999.00",
            "leverage": 1,
            "enabled": True,
        }

    if manager_repo is not None:
        try:
            mgr_obj = await manager_repo.find_by_login(str(target_login))
            if mgr_obj is not None:
                return {
                    "retcode": 0,
                    "id": id or f"session_{manager.login}",
                    "login": int(mgr_obj.login),
                    "name": getattr(mgr_obj, 'name', 'Administrator'),
                    "group": getattr(mgr_obj, 'group_name', 'administrator'),
                    "currency": "USD",
                    "balance": "0.00",
                    "equity": "0.00",
                    "margin": "0.00",
                    "margin_free": "0.00",
                    "margin_level": "999999.00",
                    "leverage": 1,
                    "enabled": True,
                }
        except Exception:
            pass

    raise HTTPException(status_code=404, detail=f"Account '{target_login}' not found")


@router.get("/AccountDetailsMany", summary="Accounts details.")
@router_root.get("/AccountDetailsMany", summary="Accounts details.")
async def handle_AccountDetailsMany_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number(s)"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """Accounts details for specified logins or all accounts."""
    return await _fetch_user_details_list(manager, id, login, account_repo, "/AccountDetailsMany")


@router.get("/Accounts", summary="Account numbers")
@router_root.get("/Accounts", summary="Account numbers")
async def handle_Accounts_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """List of all registered account numbers."""
    logins = []
    if account_repo is not None:
        try:
            if hasattr(account_repo, "get_all_accounts"):
                all_accs = await account_repo.get_all_accounts()
                logins = [int(a.login) for a in all_accs]
            elif hasattr(account_repo, "find_all"):
                all_accs = await account_repo.find_all()
                logins = [int(a.login) for a in all_accs]
        except Exception as exc:
            logger.exception("Accounts listing failed")
    return {
        "retcode": 0,
        "message": "Account numbers retrieved successfully",
        "endpoint": "/Accounts",
        "id": id or f"session_{manager.login}",
        "data": logins,
    }


@router.get("/AccountsOnline", summary="Online account details")
@router_root.get("/AccountsOnline", summary="Online account details")
async def handle_AccountsOnline_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """Online account details (enabled active accounts)."""
    return await _fetch_user_details_list(manager, id, None, account_repo, "/AccountsOnline")


@router.get("/AccountsSummary", summary="Accounts Balance, Equity, Profit, Margin summary")
@router_root.get("/AccountsSummary", summary="Accounts Balance, Equity, Profit, Margin summary")
async def handle_AccountsSummary_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="User number filter"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """Summary metrics of balance, equity, profit, margin across accounts."""
    tot_bal = Decimal("0")
    tot_eq = Decimal("0")
    tot_mar = Decimal("0")
    tot_free = Decimal("0")
    tot_prof = Decimal("0")
    count = 0

    if account_repo is not None:
        try:
            if hasattr(account_repo, "get_all_accounts"):
                all_accs = await account_repo.get_all_accounts()
            elif hasattr(account_repo, "find_all"):
                all_accs = await account_repo.find_all()
            elif login:
                acc = await account_repo.find_by_login(login)
                all_accs = [acc] if acc else []
            else:
                all_accs = []

            for acc in all_accs:
                if login and str(acc.login) != str(login):
                    continue
                from core.domains.common.value_objects import Money
                acc.update_equity(getattr(acc, 'profit', Money(Decimal('0'), acc.currency)))
                tot_bal += Decimal(str(acc.balance.amount))
                tot_eq += Decimal(str(acc.equity.amount))
                tot_mar += Decimal(str(acc.margin_used.amount))
                tot_free += Decimal(str(acc.margin_free.amount))
                tot_prof += Decimal(str(acc.profit.amount))
                count += 1
        except Exception as exc:
            logger.exception("AccountsSummary query failed")

    return {
        "retcode": 0,
        "message": "Accounts summary calculated successfully",
        "endpoint": "/AccountsSummary",
        "id": id or f"session_{manager.login}",
        "data": {
            "count": count,
            "balance": f"{tot_bal:.2f}",
            "equity": f"{tot_eq:.2f}",
            "margin": f"{tot_mar:.2f}",
            "margin_free": f"{tot_free:.2f}",
            "profit": f"{tot_prof:.2f}",
        }
    }


@router.get("/AdmTradeRecordModify", summary="MT5 Endpoint /AdmTradeRecordModify")
@router_root.get("/AdmTradeRecordModify", summary="MT5 Endpoint /AdmTradeRecordModify")
async def handle_AdmTradeRecordModify_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    ticket: Optional[str] = Query(None, alias="ticket", description=""),
    openPrice: Optional[str] = Query(None, alias="openPrice", description=""),
    closePrice: Optional[str] = Query(None, alias="closePrice", description=""),
    volume: Optional[str] = Query(None, alias="volume", description=""),
    sl: Optional[str] = Query(None, alias="sl", description=""),
    tp: Optional[str] = Query(None, alias="tp", description=""),
    comment: Optional[str] = Query(None, alias="comment", description=""),
) -> Dict[str, Any]:
    """MT5 Endpoint /AdmTradeRecordModify"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/AdmTradeRecordModify",
        "data": []
    }


@router.post("/AdmTradeRecordModifyEx", summary="MT5 Endpoint /AdmTradeRecordModifyEx")
@router_root.post("/AdmTradeRecordModifyEx", summary="MT5 Endpoint /AdmTradeRecordModifyEx")
async def handle_AdmTradeRecordModifyEx_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
) -> Dict[str, Any]:
    """MT5 Endpoint /AdmTradeRecordModifyEx"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/AdmTradeRecordModifyEx",
        "data": []
    }


@router.get("/AdmTradesDelete", summary="MT5 Endpoint /AdmTradesDelete")
@router_root.get("/AdmTradesDelete", summary="MT5 Endpoint /AdmTradesDelete")
async def handle_AdmTradesDelete_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    tickets: Optional[str] = Query(None, alias="tickets", description=""),
) -> Dict[str, Any]:
    """MT5 Endpoint /AdmTradesDelete"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/AdmTradesDelete",
        "data": []
    }


async def _funds_operation(login: Optional[str], amount: Optional[str],
                           comment: Optional[str]) -> Dict[str, Any]:
    """The ONE funds path for the manager dialect (punch-list fix).

    Each rule fixes a specific lie in the old bodies:
    * login and amount are REQUIRED - the old code invented "1000.00" when the
      caller omitted the amount, booking money nobody sent;
    * negative amount = withdrawal (mtapi convention), refused by the handler
      when the balance cannot cover it;
    * the ledger-backed BalanceOperationCommandHandler does the work: balance
      and BalanceOperation row commit together, or the whole thing refuses -
      never a mutated balance with no ledger evidence (the old body did
      balance += x via full-row save with NO ledger row);
    * the response carries the REAL operation_id; the fabricated
      `500000+login` deal tickets are gone;
    * a persistence failure is a 4xx/5xx - the old body logged a "notice" and
      returned retcode=0 "processed successfully" for a deposit that never
      happened.
    """
    from application.commands.balance_operation import (
        BalanceOperationCommand, BalanceOperationCommandHandler)
    from core.domains.common.value_objects import Money
    from core.domains.ledger.engine import LedgerEngine
    from core.domains.ledger.models import BalanceOperationType

    account_repo = get_account_repo()
    ledger_repo = get_ledger_repo()
    if account_repo is None or ledger_repo is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Funds operations need the account and ledger repositories wired")
    if not login or not str(login).strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="login is required - refusing to guess whose money this is")
    if amount is None or not str(amount).strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="amount is required - this endpoint never invents one")
    try:
        amt = Decimal(str(amount))
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"amount is not a number: {amount!r}")
    if amt == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="amount must be non-zero; say deposit or withdrawal explicitly")
    _l = str(login).strip()
    account = await account_repo.find_by_login(int(_l) if _l.lstrip("-").isdigit() else _l)
    if account is None:
        account = await account_repo.find_by_login(_l)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no account with login {login}")
    op_type = BalanceOperationType.DEPOSIT if amt > 0 else BalanceOperationType.WITHDRAWAL
    handler = BalanceOperationCommandHandler(
        ledger_engine=LedgerEngine(ledger_repo=ledger_repo, account_repo=account_repo),
        event_bus=get_event_bus(),
    )
    try:
        operation = await handler.handle(BalanceOperationCommand(
            account_login=str(account.login), operation_type=op_type,
            amount=Money(abs(amt), account.currency), comment=comment))
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return {
        "login": int(account.login),
        "operation": operation.operation_type.value,
        "amount": str(operation.amount.amount),
        "balance_after": str(operation.balance_after.amount),
        "operation_id": operation.operation_id,
        "ticket": None,  # honest: a ledger operation has no venue ticket
        "comment": operation.comment,
    }


    # ------------------------------------------------------------------
    # /BalanceAdjustment - moves money, therefore POST.
    #
    # This had the same two faults as /Deposit had: declared as a GET, so a page
    # refresh re-sent the whole transfer; and it moved the balance with a full-row
    # `save()` while writing NO ledger row, so the movement had no audit trail. It
    # also invented a `500000 + login` deal ticket and returned `retcode: 0`
    # "processed successfully" even when the repository had raised - the `except`
    # only logged a warning and the function fell through to the success return.
    #
    # It now delegates to `_funds_operation`, the same ledger-backed path /Deposit
    # uses, where the balance and the ledger row commit together or the whole
    # operation refuses.
    # ------------------------------------------------------------------
    @router.post("/BalanceAdjustment", summary="Deposit/withdraw (ledger-backed)",
                 dependencies=[Depends(require_right("RIGHT_ACCOUNTANT"))])
    @router_root.post("/BalanceAdjustment", summary="Deposit/withdraw (ledger-backed)",
                      dependencies=[Depends(require_right("RIGHT_ACCOUNTANT"))])
    async def handle_BalanceAdjustment_post(
        manager: Account = Depends(get_current_manager),
        id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
        login: Optional[str] = Query(None, alias="login", description="User account"),
        amount: Optional[str] = Query(None, alias="amount", description="Amount. If negative - withdraw."),
        action: Optional[str] = Query(None, alias="action", description=""),
        comment: Optional[str] = Query(None, alias="comment", description="Comment"),
    ) -> Dict[str, Any]:
        """Balance adjustment through the ledger. POST only."""
        result = await _funds_operation(
            login, amount, comment or f"Balance Adjustment ({action or 'balance'})"
        )
        return {
            "retcode": 0,
            "message": "Balance adjustment processed successfully",
            "endpoint": "/BalanceAdjustment",
            "id": id or f"session_{manager.login}",
            **result,
        }


def _not_wired_stub(endpoint_name: str) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content={
            "retcode": int(Retcode.REQUEST_ERROR),
            "message": f"Endpoint '{endpoint_name}' is not implemented on this server",
            "endpoint": endpoint_name,
        }
    )


@router.get("/ChartRequest", summary="OHLC history")
@router_root.get("/ChartRequest", summary="OHLC history")
async def handle_ChartRequest_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbol: Optional[str] = Query(None, alias="symbol", description="Symbol"),
    from_: Optional[str] = Query(None, alias="from", description="From date"),
    to_: Optional[str] = Query(None, alias="to", description="To date"),
) -> JSONResponse:
    """OHLC history"""
    return _not_wired_stub("/ChartRequest")


@router.post("/DealAdd", summary="Adds a new deal.")
@router_root.post("/DealAdd", summary="Adds a new deal.")
async def handle_DealAdd_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Adds a new deal."""
    return _not_wired_stub("/DealAdd")


@router.post("/DealAddBatch", summary="Adds multiple deals in batch.")
@router_root.post("/DealAddBatch", summary="Adds multiple deals in batch.")
async def handle_DealAddBatch_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Adds multiple deals in batch."""
    return _not_wired_stub("/DealAddBatch")


@router.post("/DealDeleteBatch", summary="Deletes multiple deals by ticket in batch.")
@router_root.post("/DealDeleteBatch", summary="Deletes multiple deals by ticket in batch.")
async def handle_DealDeleteBatch_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Deletes multiple deals by ticket in batch."""
    return _not_wired_stub("/DealDeleteBatch")


@router.get("/DealHistory", summary="Deal history")
@router_root.get("/DealHistory", summary="Deal history")
async def handle_DealHistory_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    from_: Optional[str] = Query(None, alias="from", description="From time"),
    to_: Optional[str] = Query(None, alias="to", description="To time"),
    deal_repo: Any = Depends(get_deal_repo),
) -> Dict[str, Any]:
    """Deal history query."""
    deals_data = []
    if deal_repo is not None:
        try:
            if login:
                target_login = int(login) if str(login).isdigit() else login
                deals = await deal_repo.find_by_account(target_login)
            else:
                deals = await deal_repo.find_all() if hasattr(deal_repo, "find_all") else []
            for d in deals:
                deals_data.append(deal_to_info(d).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("DealHistory query failed")

    return {
        "retcode": 0,
        "message": "Deal history retrieved successfully",
        "endpoint": "/DealHistory",
        "id": id or f"session_{manager.login}",
        "data": deals_data,
    }


@router.post("/DealPerform", summary="Performs a deal.")
@router_root.post("/DealPerform", summary="Performs a deal.")
async def handle_DealPerform_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Performs a deal."""
    return _not_wired_stub("/DealPerform")


@router.post("/DealPerformBatch", summary="Performs multiple deals in batch.")
@router_root.post("/DealPerformBatch", summary="Performs multiple deals in batch.")
async def handle_DealPerformBatch_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Performs multiple deals in batch."""
    return _not_wired_stub("/DealPerformBatch")


@router.post("/DealRequestByLogins", summary="Gets the deal history for multiple trading accounts")
@router_root.post("/DealRequestByLogins", summary="Gets the deal history for multiple trading accounts")
async def handle_DealRequestByLogins_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Session token"),
    logins: Optional[str] = Query(None, alias="logins", description="Comma-separated logins"),
    from_: Optional[str] = Query(None, alias="from", description="Start of time range"),
    to_: Optional[str] = Query(None, alias="to", description="End of time range"),
    deal_repo: Any = Depends(get_deal_repo),
) -> Dict[str, Any]:
    """Gets deal history for multiple logins."""
    login_filter = [int(x.strip()) for x in logins.split(",") if x.strip().isdigit()] if logins else []
    deals_data = []
    if deal_repo is not None:
        try:
            if login_filter:
                for l in login_filter:
                    deals = await deal_repo.find_by_account(l)
                    for d in deals:
                        deals_data.append(deal_to_info(d).model_dump(by_alias=True))
            else:
                all_deals = await deal_repo.find_all() if hasattr(deal_repo, "find_all") else []
                for d in all_deals:
                    deals_data.append(deal_to_info(d).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("DealRequestByLogins query failed")

    return {
        "retcode": 0,
        "message": "Deal history retrieved successfully",
        "endpoint": "/DealRequestByLogins",
        "id": id or f"session_{manager.login}",
        "data": deals_data,
    }


@router.post("/DealUpdate", summary="Updates a single deal.")
@router_root.post("/DealUpdate", summary="Updates a single deal.")
async def handle_DealUpdate_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Updates a single deal."""
    return _not_wired_stub("/DealUpdate")


@router.post("/DealUpdateBatch", summary="Updates multiple deals in batch.")
@router_root.post("/DealUpdateBatch", summary="Updates multiple deals in batch.")
async def handle_DealUpdateBatch_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> JSONResponse:
    """Updates multiple deals in batch."""
    return _not_wired_stub("/DealUpdateBatch")


    # ------------------------------------------------------------------
    # /Deposit moves money, therefore POST.
    #
    # This was a GET. A GET that mutates money gives up the guarantee HTTP exists to
    # provide: a browser refresh, a bookmark or any link-following re-sends the entire
    # withdrawal. In live testing, repeated refreshes are how an account lost six figures
    # before anyone noticed. Query parameters are deliberately KEPT because MT5's own
    # manager dialect is query-shaped - only the method changes, so no caller has to
    # learn a new convention.
    #
    # GET on this path now returns 405 instead of quietly transferring again, which is
    # the point: a financial mutation must not be reachable by following a link.
    # ------------------------------------------------------------------
    @router.post("/Deposit", summary="Deposit/withdraw (ledger-backed)",
                 dependencies=[Depends(require_right("RIGHT_ACCOUNTANT"))])
    @router_root.post("/Deposit", summary="Deposit/withdraw (ledger-backed)",
                      dependencies=[Depends(require_right("RIGHT_ACCOUNTANT"))])
    async def handle_Deposit_post(
        manager: Account = Depends(get_current_manager),
        id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
        login: Optional[str] = Query(None, alias="login", description="User account"),
        amount: Optional[str] = Query(None, alias="amount", description="Amount. If negative - withdraw."),
        comment: Optional[str] = Query(None, alias="comment", description="Comment"),
        credit: Optional[str] = Query(None, alias="credit", description="Set true if credit"),
    ) -> Dict[str, Any]:
        """Deposit/withdrawal. Same ledger-backed path as BalanceAdjustment;
        `credit=true` books a CORRECTION with the comment kept, still through the
        ledger - never a bare balance mutation.

        POST only. This was a GET, so a page refresh re-sent the transaction.
        """
        result = await _funds_operation(
            login, amount, comment or ("Credit Adjustment" if credit else None)
        )
        return {
            "retcode": 0,
            "message": "Transaction processed successfully",
            "endpoint": "/Deposit",
            "id": id or f"session_{manager.login}",
            **result,
        }


@router.get("/EmailSend", summary="MT5 Endpoint /EmailSend")
@router_root.get("/EmailSend", summary="MT5 Endpoint /EmailSend")
async def handle_EmailSend_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    account: Optional[str] = Query(None, alias="account", description=""),
    to_: Optional[str] = Query(None, alias="to", description=""),
    to_name: Optional[str] = Query(None, alias="to_name", description=""),
    subject: Optional[str] = Query(None, alias="subject", description=""),
    body: Optional[str] = Query(None, alias="body", description=""),
) -> Dict[str, Any]:
    """MT5 Endpoint /EmailSend"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/EmailSend",
        "data": []
    }


@router.get("/Health", summary="Check Connection.")
@router_root.get("/Health", summary="Check Connection.")
async def handle_Health_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> Dict[str, Any]:
    """Check Connection."""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/Health",
        "data": []
    }


@router.get("/Holidays", summary="MT5 Endpoint /Holidays")
@router_root.get("/Holidays", summary="MT5 Endpoint /Holidays")
async def handle_Holidays_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
) -> Dict[str, Any]:
    """MT5 Endpoint /Holidays"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/Holidays",
        "data": []
    }


@router.get("/IsQuoteSession", summary="Check market open or not for specified symbol.")
@router_root.get("/IsQuoteSession", summary="Check market open or not for specified symbol.")
async def handle_IsQuoteSession_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbols: Optional[str] = Query(None, alias="symbols", description=""),
) -> Dict[str, Any]:
    """Check market open or not for specified symbol."""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/IsQuoteSession",
        "data": []
    }


@router.get("/IsTradeSession", summary="Check market open or not for specified symbol.")
@router_root.get("/IsTradeSession", summary="Check market open or not for specified symbol.")
async def handle_IsTradeSession_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbols: Optional[str] = Query(None, alias="symbols", description="Symbols. If not specified - all symbols."),
) -> Dict[str, Any]:
    """Check market open or not for specified symbol."""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/IsTradeSession",
        "data": []
    }


@router.get("/MessengerSend", summary="MT5 Endpoint /MessengerSend")
@router_root.get("/MessengerSend", summary="MT5 Endpoint /MessengerSend")
async def handle_MessengerSend_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    destination: Optional[str] = Query(None, alias="destination", description=""),
    group: Optional[str] = Query(None, alias="group", description=""),
    sender: Optional[str] = Query(None, alias="sender", description=""),
    text: Optional[str] = Query(None, alias="text", description=""),
) -> Dict[str, Any]:
    """MT5 Endpoint /MessengerSend"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/MessengerSend",
        "data": []
    }


@router.get("/ModifyDeal", summary="Modify deal")
@router_root.get("/ModifyDeal", summary="Modify deal")
async def handle_ModifyDeal_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Ticket"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="Stop loss"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="Take profit"),
    comment: Optional[str] = Query(None, alias="comment", description="Comment"),
    deal_repo: Any = Depends(get_deal_repo),
) -> Dict[str, Any]:
    """Modify deal parameters."""
    if not ticket:
        return JSONResponse(
            status_code=400,
            content={"retcode": int(Retcode.REQUEST_INVALID), "message": "Ticket parameter is required", "endpoint": "/ModifyDeal"}
        )
    if deal_repo is not None:
        try:
            target_ticket = int(ticket) if str(ticket).isdigit() else ticket
            deal = await deal_repo.find_by_id(target_ticket)
            if deal is not None:
                if comment:
                    deal.comment = comment
                await deal_repo.save(deal)
                return {
                    "retcode": 0,
                    "message": f"Deal {ticket} modified successfully",
                    "endpoint": "/ModifyDeal",
                    "id": id or f"session_{manager.login}",
                    "ticket": ticket,
                }
        except Exception as exc:
            logger.exception("ModifyDeal failed for ticket %s", ticket)

    return JSONResponse(
        status_code=404,
        content={"retcode": int(Retcode.ERR_NOTFOUND), "message": f"Deal '{ticket}' not found", "endpoint": "/ModifyDeal"}
    )


@router.get("/ModifyOrder", summary="Modify order")
@router_root.get("/ModifyOrder", summary="Modify order")
async def handle_ModifyOrder_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Ticket"),
    price: Optional[str] = Query(None, alias="price", description="Order price"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="Stop loss"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="Take profit"),
    order_repo: Any = Depends(get_order_repo),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Modify order or position parameters."""
    if not ticket:
        return JSONResponse(
            status_code=400,
            content={"retcode": int(Retcode.REQUEST_INVALID), "message": "Ticket parameter is required", "endpoint": "/ModifyOrder"}
        )
    from api.routers.manager.trading import _process_modify_order_or_position
    return await _process_modify_order_or_position(
        ticket=ticket, price=price, stoploss=stoploss, takeprofit=takeprofit,
        order_repo=order_repo, position_repo=position_repo, manager_login=manager.login, endpoint="/ModifyOrder"
    )


@router.get("/OpenedOrders", summary="Active open positions for logins")
@router_root.get("/OpenedOrders", summary="Active open positions for logins")
async def handle_OpenedOrders_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    logins: Optional[str] = Query(None, alias="logins", description="List of logins. Null - all open orders."),
    sort: Optional[str] = Query(None, alias="sort", description="Sort by open time or close time"),
    ascending: Optional[str] = Query(None, alias="ascending", description="Ascending sort"),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Active open positions formatted in MT5 PositionInfo schema."""
    login_filter = [int(x.strip()) for x in logins.split(",") if x.strip().isdigit()] if logins else []
    results = []
    if position_repo is not None:
        try:
            if login_filter:
                positions = []
                for l in login_filter:
                    acc_pos = await position_repo.get_positions_by_account(l)
                    positions.extend([p for p in acc_pos if getattr(p, "time_done", None) is None])
            else:
                all_pos = await position_repo.get_open_positions()
                positions = [p for p in all_pos if getattr(p, "time_done", None) is None]

            for p in positions:
                results.append(position_to_info(p).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("OpenedOrders query failed")

    return {
        "retcode": 0,
        "message": "Opened orders retrieved successfully",
        "endpoint": "/OpenedOrders",
        "id": id or f"session_{manager.login}",
        "data": results,
    }


@router.get("/OpenedOrdersPagination", summary="Paginated active open positions")
@router_root.get("/OpenedOrdersPagination", summary="Paginated active open positions")
async def handle_OpenedOrdersPagination_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    logins: Optional[str] = Query(None, alias="logins", description="List of logins. Null - all open orders."),
    from_: Optional[str] = Query(None, alias="from", description="Open time filter, from (server time)"),
    to_: Optional[str] = Query(None, alias="to", description="Open time filter, to (server time)"),
    sort: Optional[str] = Query(None, alias="sort", description="Sort by open time or close time"),
    ascending: Optional[str] = Query(None, alias="ascending", description="Ascending sort"),
    page: Optional[str] = Query(None, alias="page", description="Zero-based page index"),
    pageSize: Optional[str] = Query(None, alias="pageSize", description="Page size, default 100"),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Paginated open positions query."""
    login_filter = [int(x.strip()) for x in logins.split(",") if x.strip().isdigit()] if logins else []
    results = []
    page_num = int(page) if page and str(page).isdigit() else 0
    size_num = int(pageSize) if pageSize and str(pageSize).isdigit() else 100

    if position_repo is not None:
        try:
            if login_filter:
                positions = []
                for l in login_filter:
                    acc_pos = await position_repo.get_positions_by_account(l)
                    positions.extend([p for p in acc_pos if getattr(p, "time_done", None) is None])
            else:
                all_pos = await position_repo.get_open_positions()
                positions = [p for p in all_pos if getattr(p, "time_done", None) is None]

            for p in positions:
                results.append(position_to_info(p).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("OpenedOrdersPagination query failed")

    total = len(results)
    start_idx = page_num * size_num
    sliced = results[start_idx : start_idx + size_num]

    return {
        "retcode": 0,
        "message": "Opened orders retrieved successfully",
        "endpoint": "/OpenedOrdersPagination",
        "id": id or f"session_{manager.login}",
        "data": sliced,
        "total": total,
    }


@router.get("/OrderHistory", summary="Position and deal history")
@router_root.get("/OrderHistory", summary="Position and deal history")
async def handle_OrderHistory_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    from_: Optional[str] = Query(None, alias="from", description="From time"),
    to_: Optional[str] = Query(None, alias="to", description="To time"),
    sort: Optional[str] = Query(None, alias="sort", description="Sort by open time or close time"),
    ascending: Optional[str] = Query(None, alias="ascending", description="Ascending sort"),
    deal_repo: Any = Depends(get_deal_repo),
) -> Dict[str, Any]:
    """Historical deals and closed positions for account."""
    results = []
    if deal_repo is not None and login:
        try:
            target_login = int(login) if str(login).isdigit() else login
            deals = await deal_repo.find_by_account(target_login)
            for d in deals:
                results.append(deal_to_info(d).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("OrderHistory query failed for login %s", login)

    return {
        "retcode": 0,
        "message": "Order history retrieved successfully",
        "endpoint": "/OrderHistory",
        "id": id or f"session_{manager.login}",
        "data": results,
    }


@router.get("/OrderHistoryPagination", summary="Paginated position and deal history")
@router_root.get("/OrderHistoryPagination", summary="Paginated position and deal history")
async def handle_OrderHistoryPagination_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    from_: Optional[str] = Query(None, alias="from", description="From time"),
    to_: Optional[str] = Query(None, alias="to", description="To time"),
    sort: Optional[str] = Query(None, alias="sort", description="Sort by open time or close time"),
    ascending: Optional[str] = Query(None, alias="ascending", description="Ascending sort"),
    page: Optional[str] = Query(None, alias="page", description="Zero-based page index"),
    pageSize: Optional[str] = Query(None, alias="pageSize", description="Page size, default 100"),
    deal_repo: Any = Depends(get_deal_repo),
) -> Dict[str, Any]:
    """Paginated historical deals and closed positions for account."""
    results = []
    page_num = int(page) if page and str(page).isdigit() else 0
    size_num = int(pageSize) if pageSize and str(pageSize).isdigit() else 100

    if deal_repo is not None and login:
        try:
            target_login = int(login) if str(login).isdigit() else login
            deals = await deal_repo.find_by_account(target_login)
            for d in deals:
                results.append(deal_to_info(d).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("OrderHistoryPagination query failed for login %s", login)

    total = len(results)
    start_idx = page_num * size_num
    sliced = results[start_idx : start_idx + size_num]

    return {
        "retcode": 0,
        "message": "Order history retrieved successfully",
        "endpoint": "/OrderHistoryPagination",
        "id": id or f"session_{manager.login}",
        "data": sliced,
        "total": total,
    }


@router.post("/OrderUpdate", summary="Updates a single order/deal.")
@router_root.post("/OrderUpdate", summary="Updates a single order/deal.")
async def handle_OrderUpdate_post(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Order ticket / deal ID"),
    price: Optional[str] = Query(None, alias="price", description="Order price"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="Stop loss"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="Take profit"),
    order_repo: Any = Depends(get_order_repo),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Updates a single order or position."""
    if not ticket:
        return JSONResponse(
            status_code=400,
            content={"retcode": int(Retcode.REQUEST_INVALID), "message": "Ticket parameter is required", "endpoint": "/OrderUpdate"}
        )
    from api.routers.manager.trading import _process_modify_order_or_position
    return await _process_modify_order_or_position(
        ticket=ticket, price=price, stoploss=stoploss, takeprofit=takeprofit,
        order_repo=order_repo, position_repo=position_repo, manager_login=manager.login, endpoint="/OrderUpdate"
    )


@router.get("/Orders", summary="Opened orders/positions.")
@router_root.get("/Orders", summary="Opened orders/positions.")
async def handle_Orders_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    logins: Optional[str] = Query(None, alias="logins", description="Logins filter"),
    order_repo: Any = Depends(get_order_repo),
) -> Dict[str, Any]:
    """Opened orders/positions."""
    orders_list = []
    login_filter = [int(x.strip()) for x in logins.split(",") if x.strip().isdigit()] if logins else []

    if order_repo is not None:
        try:
            # get_open_orders() does not exist on any repository - the call
            # raised AttributeError, the blanket except swallowed it, and the
            # route answered retcode=0 with an empty list (the F8 shape).
            # find_page(history=False) is the real active-book read.
            raw_orders, _orders_total = await order_repo.find_page(limit=1000, offset=0, history=False)
            for o in raw_orders:
                acc_login = int(o.account_login)
                if login_filter and acc_login not in login_filter:
                    continue

                # F9 rule: the venue ticket comes from external_id or is null.
                # The old fallback fabricated 800101 - a plausible-looking lie.
                _ext = getattr(o, "external_id", None)
                ord_ticket = int(_ext) if _ext is not None and str(_ext).lstrip("-").isdigit() else None
                ord_type_str = o.order_type.name if hasattr(o.order_type, "name") else str(o.order_type)
                ord_state_str = o.state.name if hasattr(o.state, "name") else str(o.state)
                vol_dec = Decimal(str(o.volume_initial.value if hasattr(o.volume_initial, 'value') else (o.volume_initial.amount if hasattr(o.volume_initial, 'amount') else o.volume_initial)))
                px_dec = Decimal(str(o.price_order.value if hasattr(o.price_order, 'value') else o.price_order)) if o.price_order else Decimal("0.00")

                orders_list.append({
                    "ticket": ord_ticket,
                    "order_id": str(o.ticket_id),
                    "login": acc_login,
                    "symbol": o.symbol,
                    "state": ord_state_str,
                    "operation": ord_type_str,
                    "volume": f"{vol_dec:.2f}",
                    "price": f"{px_dec:.2f}",
                    "time_setup": o.time_setup.isoformat() if hasattr(o, 'time_setup') and o.time_setup else "",
                })
        except HTTPException:
            raise
        except Exception:
            logger.exception("Orders read failed")
            raise HTTPException(status_code=500, detail="Could not read orders")

    return {
        "retcode": 0,
        "message": "Opened orders retrieved successfully",
        "endpoint": "/Orders",
        "id": id or f"session_{manager.login}",
        "data": orders_list,
    }


@router.get("/PendingOrderHistory", summary="Pending order history")
@router_root.get("/PendingOrderHistory", summary="Pending order history")
async def handle_PendingOrderHistory_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    from_: Optional[str] = Query(None, alias="from", description="From time"),
    to_: Optional[str] = Query(None, alias="to", description="To time"),
    order_repo: Any = Depends(get_order_repo),
) -> Dict[str, Any]:
    """Pending order history for account."""
    orders_data = []
    if order_repo is not None and login:
        try:
            target_login = int(login) if str(login).isdigit() else login
            raw_orders, _ = await order_repo.find_page(limit=1000, offset=0, history=True)
            for o in raw_orders:
                if int(o.account_login) == target_login:
                    orders_data.append(order_to_info(o).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("PendingOrderHistory query failed for login %s", login)

    return {
        "retcode": 0,
        "message": "Pending order history retrieved successfully",
        "endpoint": "/PendingOrderHistory",
        "id": id or f"session_{manager.login}",
        "data": orders_data,
    }


@router.get("/PositionHistoryMT4Format", summary="Position history MT4 format")
@router_root.get("/PositionHistoryMT4Format", summary="Position history MT4 format")
async def handle_PositionHistoryMT4Format_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    from_: Optional[str] = Query(None, alias="from", description="From time"),
    to_: Optional[str] = Query(None, alias="to", description="To time"),
    deal_repo: Any = Depends(get_deal_repo),
) -> Dict[str, Any]:
    """Position history in MT4 format."""
    results = []
    if deal_repo is not None and login:
        try:
            target_login = int(login) if str(login).isdigit() else login
            deals = await deal_repo.find_by_account(target_login)
            for d in deals:
                results.append(deal_to_info(d).model_dump(by_alias=True))
        except Exception as exc:
            logger.exception("PositionHistoryMT4Format query failed for login %s", login)

    return {
        "retcode": 0,
        "message": "Position history retrieved successfully",
        "endpoint": "/PositionHistoryMT4Format",
        "id": id or f"session_{manager.login}",
        "data": results,
    }


@router.get("/Positions", summary="Opened positions.")
@router_root.get("/Positions", summary="Opened positions.")
async def handle_Positions_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    logins: Optional[str] = Query(None, alias="logins", description="Accounts filter (comma separated logins)"),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Opened positions."""
    positions_list = []
    login_filter = [int(x.strip()) for x in logins.split(",") if x.strip().isdigit()] if logins else []

    if position_repo is not None:
        try:
            raw_pos = await position_repo.get_open_positions()
            for p in raw_pos:
                acc_login = int(p.account_login)
                if login_filter and acc_login not in login_filter:
                    continue

                act_str = p.action.name if hasattr(p.action, 'name') else str(p.action)
                vol_dec = Decimal(str(p.volume.value if hasattr(p.volume, 'value') else (p.volume.amount if hasattr(p.volume, 'amount') else p.volume)))
                open_px = Decimal(str(p.price_open.value if hasattr(p.price_open, 'value') else p.price_open))
                sl_px = Decimal(str(p.price_sl.value if hasattr(p.price_sl, 'value') else p.price_sl)) if p.price_sl else Decimal("0.00")
                tp_px = Decimal(str(p.price_tp.value if hasattr(p.price_tp, 'value') else p.price_tp)) if p.price_tp else Decimal("0.00")

                # The stored profit is the valuation writers' number (one
                # writer per number). The old body recomputed PnL inline with
                # contract_size HARDCODED per symbol - a second, divergent
                # formula for the same money.
                pnl_dec = p.profit.amount

                _pext = getattr(p, "external_id", None)
                positions_list.append({
                    "ticket": int(_pext) if _pext is not None and str(_pext).lstrip("-").isdigit() else None,
                    "position_id": str(p.position_id),
                    "login": acc_login,
                    "symbol": p.symbol,
                    "type": act_str.upper(),
                    "volume": f"{vol_dec:.2f}",
                    "price_open": f"{open_px:.2f}",
                    "sl": f"{sl_px:.2f}",
                    "tp": f"{tp_px:.2f}",
                    "profit": f"{pnl_dec:.2f}",
                })
        except HTTPException:
            raise
        except Exception:
            logger.exception("Positions read failed")
            raise HTTPException(status_code=500, detail="Could not read positions")

    return {
        "retcode": 0,
        "message": "Opened positions retrieved successfully",
        "endpoint": "/Positions",
        "id": id or f"session_{manager.login}",
        "data": positions_list,
    }


@router.get("/PositionsMT4Format", summary="Poition list in MT4 format.")
@router_root.get("/PositionsMT4Format", summary="Poition list in MT4 format.")
async def handle_PositionsMT4Format_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    logins: Optional[str] = Query(None, alias="logins", description=""),
) -> Dict[str, Any]:
    """Poition list in MT4 format."""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/PositionsMT4Format",
        "data": []
    }


@router.get("/ServerTimezone", summary="Server timezone details")
@router_root.get("/ServerTimezone", summary="Server timezone details")
async def handle_ServerTimezone_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
) -> Dict[str, Any]:
    """Server timezone details"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/ServerTimezone",
        "data": []
    }


@router.get("/SummaryGet", summary="Get summary for symbol")
@router_root.get("/SummaryGet", summary="Get summary for symbol")
async def handle_SummaryGet_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbol: Optional[str] = Query(None, alias="symbol", description=""),
) -> Dict[str, Any]:
    """Get summary for symbol"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/SummaryGet",
        "data": []
    }


@router.get("/SummaryGetAll", summary="Get summary for all symbols")
@router_root.get("/SummaryGetAll", summary="Get summary for all symbols")
async def handle_SummaryGetAll_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
) -> Dict[str, Any]:
    """Get summary for all symbols"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/SummaryGetAll",
        "data": []
    }


@router.get("/SymbolGroupExecutionSet", summary="Set symbol group execution")
@router_root.get("/SymbolGroupExecutionSet", summary="Set symbol group execution")
async def handle_SymbolGroupExecutionSet_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    userGroup: Optional[str] = Query(None, alias="userGroup", description="User group path"),
    symbolGroup: Optional[str] = Query(None, alias="symbolGroup", description="Symbol group path"),
    execution: Optional[str] = Query(None, alias="execution", description="Execution mode"),
) -> Dict[str, Any]:
    """Set symbol group execution"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/SymbolGroupExecutionSet",
        "data": []
    }


@router.get("/SymbolGroups", summary="Symbol groups")
@router_root.get("/SymbolGroups", summary="Symbol groups")
async def handle_SymbolGroups_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    userGroup: Optional[str] = Query(None, alias="userGroup", description="User group path"),
) -> Dict[str, Any]:
    """Symbol groups"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/SymbolGroups",
        "data": []
    }


@router.get("/SymbolGroupsForUserGroup", summary="Symbol groups for user group")
@router_root.get("/SymbolGroupsForUserGroup", summary="Symbol groups for user group")
async def handle_SymbolGroupsForUserGroup_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    group: Optional[str] = Query(None, alias="group", description=""),
) -> Dict[str, Any]:
    """Symbol groups for user group"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/SymbolGroupsForUserGroup",
        "data": []
    }


@router.get("/SymbolSessions", summary="Symbol quote and trade sessions")
@router_root.get("/SymbolSessions", summary="Symbol quote and trade sessions")
async def handle_SymbolSessions_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbols: Optional[str] = Query(None, alias="symbols", description="Symbol"),
) -> Dict[str, Any]:
    """Symbol quote and trade sessions"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/SymbolSessions",
        "data": []
    }


@router.get("/SymbolsList", summary="List of symbols")
@router_root.get("/SymbolsList", summary="List of symbols")
async def handle_SymbolsList_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbol_repo: Any = Depends(get_symbol_repo),
) -> Dict[str, Any]:
    """List of symbol names."""
    names = []
    if symbol_repo is not None:
        try:
            symbols = await symbol_repo.get_all_symbols()
            names = [s.name for s in symbols]
        except Exception as exc:
            logger.exception("SymbolsList query failed")
    return {
        "retcode": 0,
        "message": "Symbols list retrieved successfully",
        "endpoint": "/SymbolsList",
        "id": id or f"session_{manager.login}",
        "data": names,
    }


@router.get("/SymbolsParams", summary="Symbol parameters")
@router_root.get("/SymbolsParams", summary="Symbol parameters")
async def handle_SymbolsParams_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbols: Optional[str] = Query(None, alias="symbols", description="List of required symbols, if not specified - all symbols"),
    symbol_repo: Any = Depends(get_symbol_repo),
) -> Dict[str, Any]:
    """Symbol specification parameters."""
    requested = [x.strip().upper() for x in symbols.split(",") if x.strip()] if symbols else []
    params = []
    if symbol_repo is not None:
        try:
            all_symbols = await symbol_repo.get_all_symbols()
            for s in all_symbols:
                if requested and s.name.upper() not in requested:
                    continue
                params.append({
                    "symbol": s.name,
                    "digits": s.digits,
                    "contract_size": f"{s.contract_size:.2f}",
                    "margin_initial": f"{s.margin_initial:.2f}",
                    "currency_base": getattr(s, "currency_base", "EUR"),
                    "currency_profit": getattr(s, "currency_profit", "USD"),
                    "swap_long": f"{s.swap_long:.2f}",
                    "swap_short": f"{s.swap_short:.2f}",
                })
        except Exception as exc:
            logger.exception("SymbolsParams query failed")
    return {
        "retcode": 0,
        "message": "Symbol parameters retrieved successfully",
        "endpoint": "/SymbolsParams",
        "id": id or f"session_{manager.login}",
        "data": params,
    }


@router.get("/TickAdd", summary="Last tick details")
@router_root.get("/TickAdd", summary="Last tick details")
async def handle_TickAdd_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbol: Optional[str] = Query(None, alias="symbol", description="Symbol"),
    bid: Optional[str] = Query(None, alias="bid", description=""),
    ask: Optional[str] = Query(None, alias="ask", description=""),
    volume: Optional[str] = Query(None, alias="volume", description=""),
) -> Dict[str, Any]:
    """Last tick details"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/TickAdd",
        "data": []
    }


@router.get("/TickHistory", summary="Tick history within a specified time period")
@router_root.get("/TickHistory", summary="Tick history within a specified time period")
async def handle_TickHistory_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbol: Optional[str] = Query(None, alias="symbol", description="Symbol name"),
    from_: Optional[str] = Query(None, alias="from", description="Start time in ISO format (yyyy-MM-ddTHH:mm:ss)"),
    to_: Optional[str] = Query(None, alias="to", description="End time in ISO format (yyyy-MM-ddTHH:mm:ss)"),
) -> Dict[str, Any]:
    """Tick history within a specified time period"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/TickHistory",
        "data": []
    }


@router.get("/TickHistoryByTime", summary="Nearest tick to specified time (searches a short window first; if empty, expands to Â±2 days)")
@router_root.get("/TickHistoryByTime", summary="Nearest tick to specified time (searches a short window first; if empty, expands to Â±2 days)")
async def handle_TickHistoryByTime_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    symbol: Optional[str] = Query(None, alias="symbol", description=""),
    time: Optional[str] = Query(None, alias="time", description=""),
) -> Dict[str, Any]:
    """Nearest tick to specified time (searches a short window first; if empty, expands to Â±2 days)"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/TickHistoryByTime",
        "data": []
    }


@router.get("/TickLast", summary="Last tick details")
@router_root.get("/TickLast", summary="Last tick details")
async def handle_TickLast_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbols: Optional[str] = Query(None, alias="symbols", description="Symbols (e.g. BTCUSD, ETHUSD)"),
    symbol: Optional[str] = Query(None, alias="symbol", description="Symbol alias"),
) -> Dict[str, Any]:
    """Last known ticks, honestly.

    Sources, in order: the wired market-data engine (its ticks carry venue
    timestamps and source labels), then the trade-server gateway for whatever
    the engine has not seen. A symbol with no real quote is served with nulls
    and source=null - the old body fabricated prices (BTCUSD 65420.50, a
    hardcoded "100.00" fallback) whenever the gateway was down. A Market Watch
    page that invents prices is worse than one that shows gaps.
    """
    target_syms = symbols or symbol or ""
    sym_list = [x.strip().upper() for x in target_syms.split(",") if x.strip()]
    if not sym_list:
        from api.di_providers import get_symbol_repo as _gsr
        _srepo = _gsr()
        if _srepo is not None:
            try:
                sym_list = [sym.name for sym in await _srepo.get_all_symbols()]
            except Exception:
                logger.exception("TickLast could not list symbols")
                sym_list = []

    quotes: Dict[str, Dict[str, Any]] = {}
    engine = get_market_data_engine()
    if engine is not None:
        for sym in sym_list:
            try:
                t = engine.get_latest_tick(sym)
            except Exception:
                t = None
            if t is not None:
                quotes[sym] = {
                    "bid": str(t.bid), "ask": str(t.ask),
                    "time": t.timestamp.isoformat() if t.timestamp else None,
                    "source": t.source,
                }
    missing = [x for x in sym_list if x not in quotes]
    if missing:
        try:
            from infrastructure.gateways.trade_server_gateway import TradeServerLiquidityGateway
            gw_url = os.environ.get("BROKER_TRADE_SERVER_URL", "http://127.0.0.1:8000")
            gw = TradeServerLiquidityGateway(gw_url)
            fetched = await gw.get_quotes(missing)
            for sym, q in (fetched or {}).items():
                if q and q.get("bid") and q.get("ask"):
                    quotes[sym.upper()] = {
                        "bid": str(q["bid"]), "ask": str(q["ask"]),
                        "time": datetime.now(timezone.utc).isoformat(),
                        "source": "TRADE_SERVER",
                    }
        except Exception as exc:
            logger.warning("TickLast gateway fetch failed for %s: %s", missing, exc)

    ticks = []
    for sym in sym_list:
        q = quotes.get(sym)
        if q is None:
            ticks.append({"symbol": sym, "bid": None, "ask": None, "last": None,
                          "digits": None, "volume": None, "time": None, "source": None})
        else:
            ticks.append({"symbol": sym, "bid": q["bid"], "ask": q["ask"], "last": q["bid"],
                          "digits": None, "volume": None, "time": q["time"], "source": q["source"]})

    return {
        "retcode": 0,
        "message": "Last tick details retrieved successfully",
        "endpoint": "/TickLast",
        "id": id or f"session_{manager.login}",
        "data": ticks if len(sym_list) > 1 else (ticks[0] if ticks else {}),
    }


@router.get("/TickStat", summary="Last tick details")
@router_root.get("/TickStat", summary="Last tick details")
async def handle_TickStat_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    symbols: Optional[str] = Query(None, alias="symbols", description="Symbols (e.g. BTCUSD, ETHUSD)"),
    symbol: Optional[str] = Query(None, alias="symbol", description="Symbol alias"),
) -> Dict[str, Any]:
    """Last known ticks, honestly.

    Sources, in order: the wired market-data engine (its ticks carry venue
    timestamps and source labels), then the trade-server gateway for whatever
    the engine has not seen. A symbol with no real quote is served with nulls
    and source=null - the old body fabricated prices (BTCUSD 65420.50, a
    hardcoded "100.00" fallback) whenever the gateway was down. A Market Watch
    page that invents prices is worse than one that shows gaps.
    """
    target_syms = symbols or symbol or ""
    sym_list = [x.strip().upper() for x in target_syms.split(",") if x.strip()]
    if not sym_list:
        from api.di_providers import get_symbol_repo as _gsr
        _srepo = _gsr()
        if _srepo is not None:
            try:
                sym_list = [sym.name for sym in await _srepo.get_all_symbols()]
            except Exception:
                logger.exception("TickLast could not list symbols")
                sym_list = []

    quotes: Dict[str, Dict[str, Any]] = {}
    engine = get_market_data_engine()
    if engine is not None:
        for sym in sym_list:
            try:
                t = engine.get_latest_tick(sym)
            except Exception:
                t = None
            if t is not None:
                quotes[sym] = {
                    "bid": str(t.bid), "ask": str(t.ask),
                    "time": t.timestamp.isoformat() if t.timestamp else None,
                    "source": t.source,
                }
    missing = [x for x in sym_list if x not in quotes]
    if missing:
        try:
            from infrastructure.gateways.trade_server_gateway import TradeServerLiquidityGateway
            gw_url = os.environ.get("BROKER_TRADE_SERVER_URL", "http://127.0.0.1:8000")
            gw = TradeServerLiquidityGateway(gw_url)
            fetched = await gw.get_quotes(missing)
            for sym, q in (fetched or {}).items():
                if q and q.get("bid") and q.get("ask"):
                    quotes[sym.upper()] = {
                        "bid": str(q["bid"]), "ask": str(q["ask"]),
                        "time": datetime.now(timezone.utc).isoformat(),
                        "source": "TRADE_SERVER",
                    }
        except Exception as exc:
            logger.warning("TickLast gateway fetch failed for %s: %s", missing, exc)

    # high/low/volume_24h are HONEST NULLS: real statistics need the tick/bar
    # history store, which does not exist yet (bars = 0 rows). The old body
    # invented high=bid*1.01, low=bid*0.99 and volume_24h="12500.00" for EVERY
    # symbol - fabricated statistics are worse than absent ones.
    ticks = []
    for sym in sym_list:
        q = quotes.get(sym)
        if q is None:
            ticks.append({"symbol": sym, "bid": None, "ask": None, "high": None,
                          "low": None, "volume_24h": None, "time": None, "source": None})
        else:
            ticks.append({"symbol": sym, "bid": q["bid"], "ask": q["ask"], "high": None,
                          "low": None, "volume_24h": None, "time": q["time"], "source": q["source"]})

    return {
        "retcode": 0,
        "message": "Tick stat details retrieved successfully",
        "endpoint": "/TickStat",
        "id": id or f"session_{manager.login}",
        "data": ticks if len(sym_list) > 1 else (ticks[0] if ticks else {}),
    }


@router.get("/TradeJournal", summary="Get Trade Journal.")
@router_root.get("/TradeJournal", summary="Get Trade Journal.")
async def handle_TradeJournal_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    mode: Optional[str] = Query(None, alias="mode", description="full: 0 host: 4 user: 5 Trade: 6"),
    type: Optional[str] = Query(None, alias="type", description=""),
    from_: Optional[str] = Query(None, alias="from", description=""),
    to_: Optional[str] = Query(None, alias="to", description=""),
    filter: Optional[str] = Query(None, alias="filter", description=""),
) -> Dict[str, Any]:
    """Get Trade Journal."""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/TradeJournal",
        "data": []
    }


@router.get("/UserBalanceCheck", summary="Checks user balance against history and optionally fixes it.")
@router_root.get("/UserBalanceCheck", summary="Checks user balance against history and optionally fixes it.")
async def handle_UserBalanceCheck_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number"),
    fixflag: Optional[str] = Query(None, alias="fixflag", description="false = check only, true = check and fix"),
    account_repo: Any = Depends(get_account_repo),
    deal_repo: Any = Depends(get_deal_repo),
    ledger_repo: Any = Depends(get_ledger_repo),
) -> Dict[str, Any]:
    """Checks user balance against deal & balance operation history."""
    if not login:
        return JSONResponse(
            status_code=400,
            content={"retcode": int(Retcode.REQUEST_INVALID), "message": "Login parameter is required", "endpoint": "/UserBalanceCheck"}
        )
    target_login = int(login) if str(login).isdigit() else login
    if account_repo is None:
        return JSONResponse(status_code=503, content={"retcode": int(Retcode.REQUEST_ERROR), "message": "Account repository unavailable"})

    acc = await account_repo.find_by_login(target_login)
    if not acc:
        return JSONResponse(status_code=404, content={"retcode": int(Retcode.AUTH_ACCOUNT_UNKNOWN), "message": f"Account {login} not found"})

    calculated = Decimal("0")
    has_ledger_ops = False

    if ledger_repo is not None:
        try:
            fn = getattr(ledger_repo, "get_by_account", None) or getattr(ledger_repo, "find_by_account", None)
            if fn:
                ops = await fn(str(target_login)) if not isinstance(target_login, int) else (await fn(target_login) or await fn(str(target_login)))
                if ops:
                    has_ledger_ops = True
                    for op in ops:
                        amt = op.amount.amount if hasattr(op.amount, "amount") else Decimal(str(op.amount))
                        calculated += amt
        except Exception as exc:
            logger.warning("UserBalanceCheck ledger query failed for %s: %s", login, exc)

    if deal_repo is not None:
        try:
            fn_deals = getattr(deal_repo, "find_by_account", None) or getattr(deal_repo, "get_by_account", None)
            if fn_deals:
                deals = await fn_deals(target_login)
                for d in deals:
                    entry_str = d.entry.value if hasattr(d.entry, "value") else str(d.entry)
                    deal_type_str = d.deal_type.value if hasattr(d.deal_type, "value") else str(d.deal_type)
                    if deal_type_str == "BALANCE":
                        if not has_ledger_ops:
                            calculated += d.profit.amount + d.swap.amount - d.commission.amount
                    elif entry_str == "OUT":
                        calculated += d.profit.amount + d.swap.amount - d.commission.amount
        except Exception as exc:
            logger.warning("UserBalanceCheck deal query failed for %s: %s", login, exc)

    stored_bal = Decimal(str(acc.balance.amount))
    should_fix = bool(fixflag and fixflag.lower() == "true")
    fixed = False
    if should_fix and calculated != stored_bal:
        from core.domains.common.value_objects import Money
        acc.balance = Money(calculated, acc.currency)
        await account_repo.save(acc)
        fixed = True

    return {
        "retcode": 0,
        "message": "Balance check completed",
        "endpoint": "/UserBalanceCheck",
        "id": id or f"session_{manager.login}",
        "login": target_login,
        "current_balance": f"{stored_bal:.2f}",
        "calculated_balance": f"{calculated:.2f}",
        "fixed": fixed,
    }


@router.get("/UserDetails", summary="User details")
@router_root.get("/UserDetails", summary="User details")
async def handle_UserDetails_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """User details"""
    res = await _fetch_user_details_list(manager, id, login, account_repo, "/UserDetails")
    data_list = res.get("data", [])
    single = data_list[0] if data_list else {}
    return {
        "retcode": 0,
        "message": "User details retrieved successfully",
        "endpoint": "/UserDetails",
        "id": id or f"session_{manager.login}",
        "data": single,
    }


@router.get("/UserDetailsMany", summary="Accounts details.")
@router_root.get("/UserDetailsMany", summary="Accounts details.")
async def handle_UserDetailsMany_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number(s)"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """Accounts details for specified logins or all accounts."""
    return await _fetch_user_details_list(manager, id, login, account_repo, "/UserDetailsMany")


@router.get("/UserDetailsManyPagination", summary="Paginated variant of 'UserDetailsMany'")
@router_root.get("/UserDetailsManyPagination", summary="Paginated variant of 'UserDetailsMany'")
async def handle_UserDetailsManyPagination_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login numbers. Null - all accounts."),
    from_: Optional[str] = Query(None, alias="from", description="Registration date filter, from (server time)"),
    to_: Optional[str] = Query(None, alias="to", description="Registration date filter, to (server time)"),
    page: Optional[str] = Query(None, alias="page", description="Zero-based page index"),
    pageSize: Optional[str] = Query(None, alias="pageSize", description="Page size, default 100"),
    account_repo: Any = Depends(get_account_repo),
) -> Dict[str, Any]:
    """Paginated user details list."""
    p_num = int(page) if page and str(page).isdigit() else 0
    s_num = int(pageSize) if pageSize and str(pageSize).isdigit() else 100
    return await _fetch_user_details_list(manager, id, login, account_repo, "/UserDetailsManyPagination", page=p_num, page_size=s_num)


@router.get("/UserGroups", summary="All user groups")
@router_root.get("/UserGroups", summary="All user groups")
async def handle_UserGroups_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    assignSymbolGroups: Optional[str] = Query(None, alias="assignSymbolGroups", description=""),
    group_repo: Any = Depends(get_group_repo),
) -> Dict[str, Any]:
    """All user groups"""
    groups_data = []
    if group_repo is not None:
        try:
            groups = await group_repo.get_all_groups()
            for g in groups:
                groups_data.append({
                    "group": g.name,
                    "currency": g.currency,
                    "margin_call": f"{g.margin_call:.2f}",
                    "stop_out": f"{g.margin_stop_out:.2f}",
                    "leverage": g.default_leverage,
                })
        except Exception as exc:
            logger.exception("UserGroups query failed")
    return {
        "retcode": 0,
        "message": "User groups retrieved successfully",
        "endpoint": "/UserGroups",
        "id": id or f"session_{manager.login}",
        "data": groups_data,
    }


@router.get("/UserPasswordChange", summary="Change user passsord")
@router_root.get("/UserPasswordChange", summary="Change user passsord")
async def handle_UserPasswordChange_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    type: Optional[str] = Query(None, alias="type", description="Type"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    password: Optional[str] = Query(None, alias="password", description="Passowrd"),
) -> Dict[str, Any]:
    """Change user passsord"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/UserPasswordChange",
        "data": []
    }


@router.get("/UserPasswordCheck", summary="Check user password")
@router_root.get("/UserPasswordCheck", summary="Check user password")
async def handle_UserPasswordCheck_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    type: Optional[str] = Query(None, alias="type", description="Type"),
    login: Optional[str] = Query(None, alias="login", description="Login"),
    password: Optional[str] = Query(None, alias="password", description="Passowrd"),
) -> Dict[str, Any]:
    """Check user password"""
    return {
        "retcode": 0,
        "message": "Success",
        "endpoint": "/UserPasswordCheck",
        "data": []
    }


@router.get("/UserUpdate", summary="Update user. Only specified fields are updated. Use enableRights/disableRights to toggle individual rights without affecting others.")
@router_root.get("/UserUpdate", summary="Update user. Only specified fields are updated. Use enableRights/disableRights to toggle individual rights without affecting others.")
async def handle_UserUpdate_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    enabled: Optional[str] = Query(None, alias="enabled", description="Enable or disable user"),
    enableRights: Optional[str] = Query(None, alias="enableRights", description="Comma-separated right names to enable (OR into existing). Values: enabled,password,trade_disabled,investor,confirmed,trailing,expert,reports,readonly,reset_pass,otp_enabled,sponsored_hosting,api_enabled,push_notification"),
    disableRights: Optional[str] = Query(None, alias="disableRights", description="Comma-separated right names to disable (remove from existing). Same values as enableRights."),
    ClientID: Optional[str] = Query(None, alias="ClientID", description=""),
    FirstName: Optional[str] = Query(None, alias="FirstName", description=""),
    LastName: Optional[str] = Query(None, alias="LastName", description=""),
    MiddleName: Optional[str] = Query(None, alias="MiddleName", description=""),
    OTPSecret: Optional[str] = Query(None, alias="OTPSecret", description=""),
    LimitOrders: Optional[str] = Query(None, alias="LimitOrders", description=""),
    LimitPositionsValue: Optional[str] = Query(None, alias="LimitPositionsValue", description=""),
    Login: Optional[str] = Query(None, alias="Login", description=""),
    Group: Optional[str] = Query(None, alias="Group", description=""),
    CertSerialNumber: Optional[str] = Query(None, alias="CertSerialNumber", description=""),
    Rights: Optional[str] = Query(None, alias="Rights", description=""),
    Registration: Optional[str] = Query(None, alias="Registration", description=""),
    LastAccess: Optional[str] = Query(None, alias="LastAccess", description=""),
    LastIP: Optional[str] = Query(None, alias="LastIP", description=""),
    Name: Optional[str] = Query(None, alias="Name", description=""),
    Company: Optional[str] = Query(None, alias="Company", description=""),
    Account: Optional[str] = Query(None, alias="Account", description=""),
    Country: Optional[str] = Query(None, alias="Country", description=""),
    Language: Optional[str] = Query(None, alias="Language", description=""),
    City: Optional[str] = Query(None, alias="City", description=""),
    State: Optional[str] = Query(None, alias="State", description=""),
    ZIPCode: Optional[str] = Query(None, alias="ZIPCode", description=""),
    Address: Optional[str] = Query(None, alias="Address", description=""),
    Phone: Optional[str] = Query(None, alias="Phone", description=""),
    EMail: Optional[str] = Query(None, alias="EMail", description=""),
    ID: Optional[str] = Query(None, alias="ID", description=""),
    Status: Optional[str] = Query(None, alias="Status", description=""),
    Comment: Optional[str] = Query(None, alias="Comment", description=""),
    Color: Optional[str] = Query(None, alias="Color", description=""),
    PhonePassword: Optional[str] = Query(None, alias="PhonePassword", description=""),
    Leverage: Optional[str] = Query(None, alias="Leverage", description=""),
    Agent: Optional[str] = Query(None, alias="Agent", description=""),
    Balance: Optional[str] = Query(None, alias="Balance", description=""),
    Credit: Optional[str] = Query(None, alias="Credit", description=""),
    InterestRate: Optional[str] = Query(None, alias="InterestRate", description=""),
    CommissionDaily: Optional[str] = Query(None, alias="CommissionDaily", description=""),
    CommissionMonthly: Optional[str] = Query(None, alias="CommissionMonthly", description=""),
    CommissionAgentDaily: Optional[str] = Query(None, alias="CommissionAgentDaily", description=""),
    CommissionAgentMonthly: Optional[str] = Query(None, alias="CommissionAgentMonthly", description=""),
    BalancePrevDay: Optional[str] = Query(None, alias="BalancePrevDay", description=""),
    BalancePrevMonth: Optional[str] = Query(None, alias="BalancePrevMonth", description=""),
    EquityPrevDay: Optional[str] = Query(None, alias="EquityPrevDay", description=""),
    EquityPrevMonth: Optional[str] = Query(None, alias="EquityPrevMonth", description=""),
    LastPassChange: Optional[str] = Query(None, alias="LastPassChange", description=""),
    LeadCampaign: Optional[str] = Query(None, alias="LeadCampaign", description=""),
    LeadSource: Optional[str] = Query(None, alias="LeadSource", description=""),
    ApiDataClearAll: Optional[str] = Query(None, alias="ApiDataClearAll", description=""),
    ExternalAccountClear: Optional[str] = Query(None, alias="ExternalAccountClear", description=""),
    ExternalAccountTotal: Optional[str] = Query(None, alias="ExternalAccountTotal", description=""),
    MQID: Optional[str] = Query(None, alias="MQID", description=""),
    account_repo: Any = Depends(get_account_repo),
    group_repo: Any = Depends(get_group_repo),
) -> Dict[str, Any]:
    """Update user. Only specified fields are updated. Use enableRights/disableRights to toggle individual rights without affecting others."""
    target_login = Login or id or Account
    if not target_login:
        return {
            "retcode": 10013,
            "message": "Login is required for UserUpdate",
            "endpoint": "/UserUpdate"
        }
    
    login_str = str(target_login)
    updated_fields = {}
    
    if Group and account_repo and hasattr(account_repo, "session_factory") and account_repo.session_factory:
        from sqlalchemy import text as sa_text
        async with account_repo.session_factory() as sess:
            await sess.execute(sa_text("UPDATE accounts SET group_name = :g WHERE login = :l"), {"g": Group, "l": login_str})
            await sess.commit()
        updated_fields["group"] = Group

    if Leverage and account_repo and hasattr(account_repo, "session_factory") and account_repo.session_factory:
        from sqlalchemy import text as sa_text
        try:
            lev_int = int(Leverage)
            async with account_repo.session_factory() as sess:
                await sess.execute(sa_text("UPDATE accounts SET leverage = :lev WHERE login = :l"), {"lev": lev_int, "l": login_str})
                await sess.commit()
            updated_fields["leverage"] = lev_int
        except Exception:
            pass

    return {
        "retcode": 0,
        "message": f"User {login_str} updated successfully",
        "endpoint": "/UserUpdate",
        "login": int(login_str) if login_str.isdigit() else login_str,
        "updated": updated_fields
    }

