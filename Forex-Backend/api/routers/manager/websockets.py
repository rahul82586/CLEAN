"""
MT5 Manager API - WebSockets Router.
Honest handlers for MT5 Manager API WebSockets streaming endpoints.
"""
import logging
from typing import Optional, Dict, Any
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from api.auth.admin_dependencies import get_current_manager
from core.domains.accounts.account import Account
from core.domains.oms.retcodes import Retcode

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/manager", tags=["Manager - WebSockets"])
router_root = APIRouter(tags=["WebSockets"])

def _not_implemented_ws(endpoint_name: str) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content={
            "retcode": int(Retcode.REQUEST_ERROR),
            "message": f"Websocket stream '{endpoint_name}' is not supported over HTTP GET. Connect via ws:// protocol.",
            "endpoint": endpoint_name,
        }
    )

@router.get("/OnAccountUpdate", summary="Websocket stream for account updates.")
@router_root.get("/OnAccountUpdate", summary="Websocket stream for account updates.")
async def handle_OnAccountUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnAccountUpdate")

@router.get("/OnConnectDisconnect", summary="Websocket stream for connect/disconnect events.")
@router_root.get("/OnConnectDisconnect", summary="Websocket stream for connect/disconnect events.")
async def handle_OnConnectDisconnect(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnConnectDisconnect")

@router.get("/OnDealUpdate", summary="Websocket stream for deal updates.")
@router_root.get("/OnDealUpdate", summary="Websocket stream for deal updates.")
async def handle_OnDealUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnDealUpdate")

@router.get("/OnGroupUpdate", summary="Websocket stream for group updates.")
@router_root.get("/OnGroupUpdate", summary="Websocket stream for group updates.")
async def handle_OnGroupUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnGroupUpdate")

@router.get("/OnMarketWatch", summary="Websocket stream for market watch.")
@router_root.get("/OnMarketWatch", summary="Websocket stream for market watch.")
async def handle_OnMarketWatch(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnMarketWatch")

@router.get("/OnOrderProfit", summary="Websocket stream for order profit.")
@router_root.get("/OnOrderProfit", summary="Websocket stream for order profit.")
async def handle_OnOrderProfit(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnOrderProfit")

@router.get("/OnOrderProfitInterval", summary="Websocket stream for order profit interval.")
@router_root.get("/OnOrderProfitInterval", summary="Websocket stream for order profit interval.")
async def handle_OnOrderProfitInterval(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnOrderProfitInterval")

@router.get("/OnOrderProfitIntervalEx", summary="Websocket stream for order profit interval ex.")
@router_root.get("/OnOrderProfitIntervalEx", summary="Websocket stream for order profit interval ex.")
async def handle_OnOrderProfitIntervalEx(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnOrderProfitIntervalEx")

@router.get("/OnOrderUpdate", summary="Websocket stream for order updates.")
@router_root.get("/OnOrderUpdate", summary="Websocket stream for order updates.")
async def handle_OnOrderUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnOrderUpdate")

@router.get("/OnPositionUpdate", summary="Websocket stream for position updates.")
@router_root.get("/OnPositionUpdate", summary="Websocket stream for position updates.")
async def handle_OnPositionUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnPositionUpdate")

@router.get("/OnPositionUpdateMT4Format", summary="Websocket stream for position updates MT4 format.")
@router_root.get("/OnPositionUpdateMT4Format", summary="Websocket stream for position updates MT4 format.")
async def handle_OnPositionUpdateMT4Format(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnPositionUpdateMT4Format")

@router.get("/OnQuote", summary="Websocket stream for quotes.")
@router_root.get("/OnQuote", summary="Websocket stream for quotes.")
async def handle_OnQuote(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnQuote")

@router.get("/OnRequesUpdate", summary="Websocket stream for request updates.")
@router_root.get("/OnRequesUpdate", summary="Websocket stream for request updates.")
async def handle_OnRequesUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnRequesUpdate")

@router.get("/OnSymbolUpdate", summary="Websocket stream for symbol updates.")
@router_root.get("/OnSymbolUpdate", summary="Websocket stream for symbol updates.")
async def handle_OnSymbolUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnSymbolUpdate")

@router.get("/OnTick", summary="Websocket stream for ticks.")
@router_root.get("/OnTick", summary="Websocket stream for ticks.")
async def handle_OnTick(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnTick")

@router.get("/OnTickStat", summary="Websocket stream for tick stat.")
@router_root.get("/OnTickStat", summary="Websocket stream for tick stat.")
async def handle_OnTickStat(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnTickStat")

@router.get("/OnTradeDelete", summary="Websocket stream for trade deletion.")
@router_root.get("/OnTradeDelete", summary="Websocket stream for trade deletion.")
async def handle_OnTradeDelete(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnTradeDelete")

@router.get("/OnUserUpdate", summary="Websocket stream for user updates.")
@router_root.get("/OnUserUpdate", summary="Websocket stream for user updates.")
async def handle_OnUserUpdate(id: Optional[str] = Query(None), manager: Account = Depends(get_current_manager)) -> JSONResponse:
    return _not_implemented_ws("OnUserUpdate")
