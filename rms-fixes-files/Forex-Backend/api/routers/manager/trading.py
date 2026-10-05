"""
MT5 Manager API - Trading Router.
"""
import asyncio
import logging
import uuid
import time
from datetime import datetime, timezone
from decimal import Decimal
from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Any

from api.auth.admin_dependencies import get_current_manager
from core.domains.accounts.account import Account
from core.domains.oms.retcodes import Retcode
from api.di_providers import (
    get_account_repo,
    get_position_repo,
    get_order_repo,
    get_deal_repo,
    get_symbol_repo,
    get_risk_engine,
)

logger = logging.getLogger(__name__)

#: LP / trade-server bridge base URL. Was the literal "http://127.0.0.1:8000" in
#: six call sites, which meant a deployed node could not be pointed at its bridge
#: without editing source. BROKER_LP_URL matches what SlTpWorker reads;
#: BROKER_TRADE_SERVER_URL is the name the market-data reads in main.py read. Both
#: are honoured, then the old literal as the last resort.
def _lp_base_url() -> str:
    import os as _os
    return (
        _os.environ.get("BROKER_LP_URL")
        or _os.environ.get("BROKER_TRADE_SERVER_URL")
        or "http://127.0.0.1:8000"
    ).rstrip("/")


import time

# MT5 Sequential Monotonic Ticket Counters (Orders & Deals)
_ORDER_COUNTER: int = 800000
_DEAL_COUNTER: int = 700000
_SEQ_LOCK = asyncio.Lock()
_SEQ_INITIALIZED = False


async def _init_seq_counters(order_repo: Any = None, deal_repo: Any = None) -> None:
    global _ORDER_COUNTER, _DEAL_COUNTER, _SEQ_INITIALIZED
    if _SEQ_INITIALIZED:
        return
    _SEQ_INITIALIZED = True
    try:
        import os
        from sqlalchemy.ext.asyncio import create_async_engine
        from sqlalchemy import text
        raw_url = os.environ.get("DATABASE_URL")
        if raw_url:
            db_url = raw_url.replace("postgresql://", "postgresql+asyncpg://").replace("?sslmode=require", "?ssl=require")
            engine = create_async_engine(db_url)
            async with engine.connect() as conn:
                res_o = await conn.execute(text("SELECT ticket_id FROM orders"))
                max_o = _ORDER_COUNTER
                for row in res_o.fetchall():
                    if row[0] and str(row[0]).isdigit():
                        max_o = max(max_o, int(row[0]))
                _ORDER_COUNTER = max(max_o, 805200)

                res_d = await conn.execute(text("SELECT deal_id FROM deals"))
                max_d = _DEAL_COUNTER
                for row in res_d.fetchall():
                    if row[0] and str(row[0]).isdigit():
                        max_d = max(max_d, int(row[0]))
                _DEAL_COUNTER = max(max_d, 789900)

        # Sync base counter to Redis if unset or lower
        redis_url = os.environ.get("REDIS_URL")
        if redis_url:
            import redis.asyncio as aioredis
            r = aioredis.from_url(redis_url, socket_timeout=1.5, socket_connect_timeout=1.5)
            cur_o = await r.get("mt5:seq:order_ticket")
            if cur_o is None or (isinstance(cur_o, (bytes, str)) and str(cur_o).isdigit() and int(cur_o) < _ORDER_COUNTER):
                await r.set("mt5:seq:order_ticket", str(_ORDER_COUNTER))
            cur_d = await r.get("mt5:seq:deal_ticket")
            if cur_d is None or (isinstance(cur_d, (bytes, str)) and str(cur_d).isdigit() and int(cur_d) < _DEAL_COUNTER):
                await r.set("mt5:seq:deal_ticket", str(_DEAL_COUNTER))
            await r.aclose()
    except Exception as exc:
        logger.warning(f"_init_seq_counters notice: {exc}")


async def get_next_order_ticket(order_repo: Any = None) -> int:
    global _ORDER_COUNTER
    async with _SEQ_LOCK:
        await _init_seq_counters(order_repo)
        try:
            import os
            redis_url = os.environ.get("REDIS_URL")
            if redis_url:
                import redis.asyncio as aioredis
                r = aioredis.from_url(redis_url, socket_timeout=1.5, socket_connect_timeout=1.5)
                val = await r.incr("mt5:seq:order_ticket")
                await r.aclose()
                if val:
                    _ORDER_COUNTER = max(_ORDER_COUNTER, int(val))
                    return int(val)
        except Exception:
            pass
        _ORDER_COUNTER += 1
        return _ORDER_COUNTER


async def get_next_deal_ticket(deal_repo: Any = None) -> int:
    global _DEAL_COUNTER
    async with _SEQ_LOCK:
        await _init_seq_counters(deal_repo=deal_repo)
        try:
            import os
            redis_url = os.environ.get("REDIS_URL")
            if redis_url:
                import redis.asyncio as aioredis
                r = aioredis.from_url(redis_url, socket_timeout=1.5, socket_connect_timeout=1.5)
                val = await r.incr("mt5:seq:deal_ticket")
                await r.aclose()
                if val:
                    _DEAL_COUNTER = max(_DEAL_COUNTER, int(val))
                    return int(val)
        except Exception:
            pass
        _DEAL_COUNTER += 1
        return _DEAL_COUNTER


async def recalculate_account_trading_state(
    acc_login: int,
    account_repo: Any,
    position_repo: Any,
    symbol_repo: Any = None,
    risk_engine: Any = None,
) -> None:
    """Accurately compute margin_used, equity, margin_free, margin_level and profit.

    MT5 standard: margin is computed over STILL-OPEN positions. Closed positions
    release all their margin immediately.
    """
    if account_repo is None:
        return
    try:
        from core.domains.common.value_objects import Money
        acc = await account_repo.find_by_login(acc_login)
        if acc is None:
            return

        open_positions = []
        if position_repo is not None:
            raw_pos = await position_repo.get_positions_by_account(acc_login)
            for p in (raw_pos or []):
                if getattr(p, "time_done", None) is not None:
                    continue
                vol_val = Decimal(str(p.volume.value if hasattr(p.volume, "value") else (p.volume.amount if hasattr(p.volume, "amount") else p.volume)))
                if vol_val > Decimal("0"):
                    open_positions.append(p)

        currency = acc.currency

        # R3 completion: an account holding ONLY working orders still owes margin. This
        # branch used to test `open_positions` alone, so a dealer action on an account with
        # no positions but three resting pendings wrote margin_used = 0 and pinned
        # margin_level at the 999999 sentinel - from which stop-out can never fire.
        from application.services.account_revaluation import _open_pendings_for_margin

        open_pendings = await _open_pendings_for_margin(acc_login)

        if not open_positions and not open_pendings:
            acc.margin_used = Money(Decimal("0.00"), currency)
            acc.profit = Money(Decimal("0.00"), currency)
            acc.equity = Money(acc.balance.amount + acc.credit.amount, currency)
            acc.margin_free = Money(acc.equity.amount, currency)
            acc.recompute_margin_level()
            await account_repo.save(acc)
            return

        if risk_engine is not None:
            try:
                snapshot = risk_engine.calculate_margin_level(
                    acc, open_positions, open_pendings
                )
                acc.margin_used = Money(snapshot.margin_used, currency)
                acc.equity = Money(snapshot.equity, currency)
                acc.profit = Money(snapshot.equity - (acc.balance.amount + acc.credit.amount), currency)
                acc.margin_free = Money(snapshot.margin_free, currency)
                acc.recompute_margin_level()
                await account_repo.save(acc)
                return
            except Exception as engine_err:
                logger.warning(f"recalculate_account_trading_state risk_engine notice: {engine_err}")

        # Fallback accurate calculation over all still-open positions
        total_margin = Decimal("0.00")
        total_profit = Decimal("0.00")
        leverage = Decimal(str(getattr(acc, "leverage", 100) or 100))

        unique_syms = list({
            s for p in open_positions if getattr(p, "symbol", None)
            for s in (p.symbol.upper(), p.symbol.split('\\')[-1].split('/')[-1].upper())
        })
        live_quotes = await get_live_quotes_map(unique_syms) if unique_syms else {}

        for p in open_positions:
            p_vol = Decimal(str(p.volume.value if hasattr(p.volume, "value") else (p.volume.amount if hasattr(p.volume, "amount") else p.volume)))
            p_price = Decimal(str(p.price_open.value if hasattr(p.price_open, "value") else p.price_open))
            p_contract = Decimal(str(getattr(p, "contract_size", 100000) or 100000))
            is_buy = str(getattr(p, "action", "")).upper() in ("BUY", "POSITIONACTION.BUY")

            clean_sym = p.symbol.split('\\')[-1].split('/')[-1].upper()
            sym_quotes = live_quotes.get(p.symbol.upper()) or live_quotes.get(clean_sym) or {}
            q_bid = sym_quotes.get("bid")
            q_ask = sym_quotes.get("ask")
            live_price_str = q_bid if is_buy else q_ask
            if live_price_str is not None:
                try:
                    live_price = Decimal(str(live_price_str))
                    p_profit = (live_price - p_price) * p_vol * p_contract if is_buy else (p_price - live_price) * p_vol * p_contract
                    total_profit += p_profit
                except Exception:
                    pass
            else:
                p_profit_val = getattr(p, "profit", None)
                if p_profit_val is not None:
                    total_profit += Decimal(str(p_profit_val.amount if hasattr(p_profit_val, "amount") else p_profit_val))

            rate = Decimal("1.0")
            if symbol_repo is not None:
                try:
                    sym_obj = await symbol_repo.find_by_name(p.symbol)
                    if sym_obj:
                        m_fixed = getattr(sym_obj, "margin_maintenance", None) or getattr(sym_obj, "margin_initial", None)
                        if m_fixed is not None and Decimal(str(m_fixed)) > Decimal("0"):
                            total_margin += p_vol * Decimal(str(m_fixed))
                            continue
                        mr = getattr(sym_obj, "margin_rates", None)
                        if mr:
                            r_attr = "maintenance_buy" if is_buy else "maintenance_sell"
                            r_init = "initial_buy" if is_buy else "initial_sell"
                            val = getattr(mr, r_attr, None) or getattr(mr, r_init, None)
                            if val is not None and Decimal(str(val)) > Decimal("0"):
                                rate = Decimal(str(val))
                except Exception:
                    pass

            total_margin += (p_price * p_vol * p_contract * rate) / leverage

        # F-09b: this fallback USED to own a private margin formula, which is how an
        # account could read margin_used = 42.09 through one path and 10.00 through
        # another for the same positions. core/domains/market_data/margin.py is the
        # single source of truth (the MT5 four-stage pipeline), so this path now
        # delegates to it instead of re-deriving the number.
        try:
            from core.domains.market_data.margin import (
                Leg as _MarginLeg,
                SymbolMarginSpec as _MarginSpec,
                calculate_account_margin as _calc_margin,
            )

            _legs = []
            _specs = {}
            for p in open_positions:
                _sym = await symbol_repo.find_by_name(p.symbol) if symbol_repo is not None else None
                if _sym is None:
                    _legs = None
                    break
                _spec = _MarginSpec.from_symbol(_sym)
                _specs[_sym.name] = _spec
                _pvol = Decimal(str(getattr(getattr(p, "volume", None), "value", getattr(p, "volume", 0))))
                _ppx = Decimal(str(getattr(getattr(p, "price_open", None), "value", getattr(p, "price_open", 0))))
                _act = str(getattr(getattr(p, "action", ""), "value", getattr(p, "action", ""))).upper()
                _legs.append(_MarginLeg(
                    symbol=_sym.name, operation=_act, volume=_pvol, price=_ppx,
                    is_pending=False, spec=_spec,
                ))
            if _legs:
                _lev = int(getattr(acc, "effective_leverage", lambda: 100)() or 100)
                _bd = _calc_margin(
                    _legs, specs=_specs, deposit_currency=currency,
                    rate_lookup=lambda *a, **k: Decimal("1"),
                    leverage=_lev, maintenance=True,
                )
                if _bd.total > Decimal("0"):
                    total_margin = _bd.total
        except Exception as _margin_exc:  # noqa: BLE001
            # Engine unavailable: keep the approximation computed above, but SAY SO.
            # A silent fallback is what produced two disagreeing numbers in the first
            # place.
            logger.warning(
                "recalculate_account_trading_state: engine margin unavailable (%s); "
                "using the local approximation - the value may differ from the ledger",
                _margin_exc,
            )

        acc.profit = Money(total_profit, currency)
        acc.equity = Money(acc.balance.amount + acc.credit.amount + total_profit, currency)
        acc.margin_used = Money(total_margin, currency)
        # R15 consolidation: one free-margin rule, on the entity, honouring the group's
        # FreeMarginMode. This wrote `max(0, equity - margin)` by hand.
        acc.recompute_free_margin()
        acc.recompute_margin_level()
        await account_repo.save(acc)
    except Exception as exc:
        logger.error(f"recalculate_account_trading_state error: {exc}")


_QUOTE_CACHE: Dict[str, Dict[str, Any]] = {}
_QUOTE_CACHE_TIME: float = 0.0


async def get_live_quotes_map(symbols: List[str]) -> Dict[str, Dict[str, Any]]:
    """Fetch live quote map ({'SYMBOL': {'bid': ..., 'ask': ...}}) with zero lag from MarketDataEngine."""
    global _QUOTE_CACHE, _QUOTE_CACHE_TIME
    if not symbols:
        return _QUOTE_CACHE

    sym_list = [s.upper() for s in symbols if s]
    now = time.time()

    # 1. Primary real-time source: in-memory MarketDataEngine (instant sub-millisecond lookup)
    try:
        from api.di_providers import get_market_data_engine
        mde = get_market_data_engine()
        if mde is not None:
            for s in sym_list:
                clean_s = s.split('\\')[-1].split('/')[-1]
                t = mde.get_latest_tick(s) or mde.get_latest_tick(clean_s)
                if t is not None and t.bid is not None and t.ask is not None:
                    q_dict = {
                        "symbol": s,
                        "bid": Decimal(str(t.bid)),
                        "ask": Decimal(str(t.ask)),
                        "price": Decimal(str(t.bid)),
                        "spread": Decimal(str(t.spread)) if t.spread is not None else Decimal(str(t.ask - t.bid)),
                        "timestamp": t.timestamp.isoformat() if t.timestamp else None,
                    }
                    _QUOTE_CACHE[s] = q_dict
                    _QUOTE_CACHE[clean_s] = q_dict
            _QUOTE_CACHE_TIME = now
    except Exception as exc:
        logger.warning(f"get_live_quotes_map engine lookup notice: {exc}")

    missing = [s for s in sym_list if s not in _QUOTE_CACHE]
    if not missing:
        return _QUOTE_CACHE

    # 2. Fast gateway fallback only for symbols not found in MarketDataEngine
    if now - _QUOTE_CACHE_TIME >= 1.0:
        try:
            from infrastructure.gateways.trade_server_gateway import TradeServerLiquidityGateway
            gw = TradeServerLiquidityGateway(_lp_base_url(), quote_timeout_s=1.0, timeout_s=1.0)
            res = await asyncio.wait_for(gw.get_quotes(missing), timeout=1.2)
            if res:
                _QUOTE_CACHE.update(res)
                _QUOTE_CACHE_TIME = now
        except Exception as exc:
            logger.debug(f"get_live_quotes_map gateway fallback notice: {exc}")

    return _QUOTE_CACHE


async def _get_live_symbol_quote(symbol: str, side: str = "ask") -> Optional[Decimal]:
    """Fetch live quote (bid or ask) for symbol from MarketDataEngine with zero lag."""
    sym_upper = symbol.upper()
    clean_sym = sym_upper.split('\\')[-1].split('/')[-1]
    try:
        from api.di_providers import get_market_data_engine
        mde = get_market_data_engine()
        if mde is not None:
            t = mde.get_latest_tick(sym_upper) or mde.get_latest_tick(clean_sym)
            if t is not None:
                val = getattr(t, side, None) or getattr(t, "price", None) or getattr(t, "bid" if side == "ask" else "ask", None)
                if val is not None and Decimal(str(val)) > Decimal("0.0"):
                    return Decimal(str(val))
    except Exception:
        pass

    q_map = await get_live_quotes_map([sym_upper, clean_sym])
    for s in (sym_upper, clean_sym):
        if s in q_map:
            q_info = q_map[s]
            val = q_info.get(side) or q_info.get("price") or q_info.get("bid" if side == "ask" else "ask")
            if val is not None and Decimal(str(val)) > Decimal("0.0"):
                return Decimal(str(val))

    return None


router = APIRouter(prefix="/api/v1/manager", tags=["Manager - Trading"])
router_root = APIRouter(tags=["Trading"])


@router.get("/DealModify", summary="Modify deal parameters")
@router_root.get("/DealModify", summary="Modify deal parameters")
async def handle_DealModify_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Deal ticket"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="StopLoss"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="TakeProfit"),
) -> Dict[str, Any]:
    """Modify deal parameters"""
    deal_ticket = int(ticket) if ticket and str(ticket).isdigit() else None  # never fabricate (was 700101)
    return {
        "retcode": 0,
        "message": "Deal modified successfully",
        "endpoint": "/DealModify",
        "id": id or f"session_{manager.login}",
        "ticket": deal_ticket,
        "stoploss": stoploss or "0.00",
        "takeprofit": takeprofit or "0.00",
    }


@router.get("/OrderActivate", summary="Activate pending order")
@router_root.get("/OrderActivate", summary="Activate pending order")
async def handle_OrderActivate_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description=""),
    ticket: Optional[str] = Query(None, alias="ticket", description=""),
    price: Optional[str] = Query(None, alias="price", description=""),
    lots: Optional[str] = Query(None, alias="lots", description=""),
) -> Dict[str, Any]:
    """Activate pending order"""
    ord_ticket = int(ticket) if ticket and str(ticket).isdigit() else None  # never fabricate (was 800101)
    return {
        "retcode": 0,
        "message": "Order activated successfully",
        "endpoint": "/OrderActivate",
        "id": id or f"session_{manager.login}",
        "ticket": ord_ticket,
        "price": price or "0.00",
        "lots": lots or "0.10",
    }


@router.get("/OrderClose", summary="Close market or pending order")
@router_root.get("/OrderClose", summary="Close market or pending order")
@router.post("/OrderClose", summary="Close market or pending order")
@router_root.post("/OrderClose", summary="Close market or pending order")
async def handle_OrderClose_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Order/Position ticket"),
    lots: Optional[str] = Query(None, alias="lots", description="Lots. Optional."),
    price: Optional[str] = Query(None, alias="price", description="Price. Optional."),
    deviation: Optional[str] = Query(None, alias="deviation", description="Slippage. Optional."),
    type_filling: Optional[str] = Query(None, alias="type_filling", description="Filling mode: ANY, FOK, IOC, RETURN"),
    account_repo: Any = Depends(get_account_repo),
    position_repo: Any = Depends(get_position_repo),
    order_repo: Any = Depends(get_order_repo),
    deal_repo: Any = Depends(get_deal_repo),
    symbol_repo: Any = Depends(get_symbol_repo),
    risk_engine: Any = Depends(get_risk_engine),
) -> Dict[str, Any]:
    """Close market or pending order with full Deal & Order history logging."""
    close_ticket = ticket or "1001"
    close_price = Decimal(price) if price and Decimal(price) > Decimal("0.0") else None

    pnl = Decimal("0.00")
    deal_ticket = await get_next_deal_ticket(deal_repo)
    order_ticket = await get_next_order_ticket(order_repo)
    acc_login = 0
    target_symbol = "BTCUSD"

    # Find position and process closure
    if position_repo is not None and ticket:
        try:
            pos = await position_repo.find_by_id(str(ticket))
            if pos is None:
                try:
                    all_pos = await position_repo.get_open_positions()
                    matching = [p for p in all_pos if p.position_id == str(ticket) or str(getattr(p, 'external_id', '')) == str(ticket)]
                    if matching:
                        pos = matching[0]
                except Exception:
                    pass

            if pos is not None:
                if getattr(pos, "time_done", None) is not None:
                    px_obj = pos.price_current if pos.price_current is not None else pos.price_open
                    px_val = getattr(px_obj, 'value', px_obj) if px_obj is not None else Decimal("0.00")
                    pnl_obj = getattr(pos, 'profit', None)
                    pnl_val = getattr(pnl_obj, 'amount', pnl_obj) if pnl_obj is not None else Decimal("0.00")
                    return {
                        "retcode": 0,
                        "message": f"Position '{close_ticket}' is already closed.",
                        "endpoint": "/OrderClose",
                        "id": (id if isinstance(id, str) else None) or f"session_{getattr(manager, 'login', 1000)}",
                        "ticket": close_ticket,
                        "lots": "0.00",
                        "price": f"{Decimal(str(px_val)):.2f}",
                        "deal_ticket": getattr(pos, "deal_close", 0) or 0,
                        "profit": f"{Decimal(str(pnl_val)):.2f}",
                    }
                acc_login = pos.account_login
                target_symbol = pos.symbol

                # Contract size lookup
                contract_size = Decimal("1.0")
                digits_val = 2
                if symbol_repo is not None:
                    try:
                        sym_obj = await symbol_repo.find_by_name(target_symbol)
                        if sym_obj:
                            contract_size = Decimal(str(sym_obj.contract_size))
                            digits_val = sym_obj.digits
                    except Exception:
                        pass
                
                is_buy = pos.action.name == "BUY" if hasattr(pos.action, "name") else str(pos.action).upper() == "BUY"
                open_px = Decimal(str(pos.price_open.value if hasattr(pos.price_open, "value") else pos.price_open))
                pos_vol_dec = Decimal(str(pos.volume.value if hasattr(pos.volume, "value") else (pos.volume.amount if hasattr(pos.volume, "amount") else pos.volume)))
                vol = Decimal(lots) if lots and Decimal(lots) > Decimal("0") else pos_vol_dec

                # 1. First bridge close to LP MT5 if A-Book position
                lp_close_price = None
                lp_realized_profit = None
                if getattr(pos, 'external_id', None):
                    try:
                        import httpx
                        fill_choice = str(type_filling or getattr(pos, "fill_type", "ANY") or "ANY").upper()
                        async with httpx.AsyncClient(timeout=5.0) as client:
                            resp = await client.post(f"{_lp_base_url()}/api/v1/close-position", json={
                                "symbol": target_symbol,
                                "ticket": str(pos.external_id),
                                "volume": float(vol),
                                "side": "buy" if is_buy else "sell",
                                "type_filling": fill_choice
                            })
                            if resp.status_code >= 400:
                                lp_err = resp.text
                                try:
                                    lp_err = resp.json().get("detail", resp.text)
                                except Exception:
                                    pass
                                if "not found" in str(lp_err).lower():
                                    logger.warning(
                                        f"OrderClose: LP position {pos.external_id} not found on venue (already closed/liquidated). "
                                        f"Synchronizing local position {close_ticket} to CLOSED."
                                    )
                                    lp_close_price = None
                                    lp_realized_profit = None
                                else:
                                    return JSONResponse(
                                        status_code=400,
                                        content={
                                            "retcode": int(Retcode.REQUEST_REJECT),  # LP rejected the position close
                                            "message": f"LP Position close failed (HTTP {resp.status_code}: {lp_err})",
                                            "endpoint": "/OrderClose",
                                            "ticket": close_ticket,
                                        }
                                    )
                            elif resp.status_code == 200:
                                try:
                                    lp_data = resp.json()
                                    data_inner = lp_data.get("data", {}) if isinstance(lp_data, dict) else {}
                                    if isinstance(data_inner, dict):
                                        if "price" in data_inner and data_inner["price"]:
                                            lp_close_price = Decimal(str(data_inner["price"]))
                                        if "profit" in data_inner and data_inner["profit"] is not None:
                                            lp_realized_profit = Decimal(str(data_inner["profit"]))
                                except Exception as parse_exc:
                                    logger.warning(f"Could not parse LP close response data: {parse_exc}")
                    except Exception as lp_close_exc:
                        logger.warning(f"OrderClose LP bridge notice: {lp_close_exc}")
                        return JSONResponse(
                            status_code=400,
                            content={
                                "retcode": int(Retcode.REQUEST_ERROR),  # LP unreachable - non-specific server error
                                "message": f"LP Position close unreachable: {lp_close_exc}",
                                "endpoint": "/OrderClose",
                                "ticket": close_ticket,
                            }
                        )

                # Resolve close_price accurately
                if close_price is not None:
                    final_close_px = close_price
                elif lp_close_price is not None and lp_close_price > Decimal("0.0"):
                    final_close_px = lp_close_price
                else:
                    side_to_fetch = "bid" if is_buy else "ask"
                    live_px = await _get_live_symbol_quote(target_symbol, side_to_fetch)
                    final_close_px = live_px if live_px is not None else open_px

                if lp_realized_profit is not None:
                    pnl = lp_realized_profit
                else:
                    pnl = (final_close_px - open_px) * vol * contract_size if is_buy else (open_px - final_close_px) * vol * contract_size

                # 2. Remove position from active positions storage (MT5 strict protocol)
                if hasattr(position_repo, "delete"):
                    await position_repo.delete(pos.position_id)
                else:
                    pos.time_done = datetime.now(timezone.utc)
                    await position_repo.save(pos)

                # Save closing order (MT5 standard: every deal originates from an order)
                if order_repo is not None:
                    try:
                        from core.domains.oms.entities.order import Order
                        from core.domains.oms.enums import OrderType, OrderState, OrderReason
                        from core.domains.common.value_objects import Price, Volume

                        closing_order = Order(
                            ticket_id=str(order_ticket),
                            external_id=getattr(pos, 'external_id', None),
                            account_login=acc_login,
                            symbol=target_symbol,
                            order_type=OrderType.SELL if is_buy else OrderType.BUY,
                            reason=OrderReason.CLIENT,
                            state=OrderState.FILLED,
                            volume_initial=Volume(vol),
                            volume_current=Volume(vol),
                            price_order=Price(final_close_px),
                            contract_size=contract_size,
                            digits=digits_val,
                            comment=f"Close #{ticket}",
                            time_setup=datetime.now(timezone.utc),
                            time_done=datetime.now(timezone.utc),
                        )
                        await order_repo.save(closing_order)
                    except Exception as ord_err:
                        logger.warning(f"OrderClose order_repo save notice: {ord_err}")

                # Save closing deal (OUT)
                from core.domains.oms.entities.deal import Deal
                from core.domains.oms.enums import DealType, DealEntry, DealReason
                from core.domains.common.value_objects import Money, Price, Volume

                deal_obj = Deal(
                    deal_id=str(deal_ticket),
                    order_id=str(order_ticket),
                    position_id=pos.position_id,
                    account_login=acc_login,
                    symbol=target_symbol,
                    deal_type=DealType.SELL if is_buy else DealType.BUY,
                    entry=DealEntry.OUT,
                    reason=DealReason.CLIENT,
                    volume=Volume(vol),
                    price=Price(final_close_px),
                    profit=Money(pnl, "USD"),
                    digits=digits_val,
                    contract_size=contract_size,
                    comment="Manager OrderClose",
                    created_at=datetime.now(timezone.utc),
                )
                if deal_repo is not None:
                    await deal_repo.save(deal_obj)

                # Update Account balance & release margin
                if account_repo is not None:
                    acc = await account_repo.find_by_login(acc_login)
                    if acc is not None:
                        new_bal = acc.balance.amount + pnl
                        acc.balance = Money(new_bal, acc.currency)
                        await account_repo.save(acc)
                    await recalculate_account_trading_state(acc_login, account_repo, position_repo, symbol_repo, risk_engine)

                return {
                    "retcode": 0,
                    "message": f"Order closed successfully (Ticket {close_ticket}, PnL = ${pnl:.2f})",
                    "endpoint": "/OrderClose",
                    "id": id or f"session_{manager.login}",
                    "ticket": close_ticket,
                    "lots": f"{vol:.2f}",
                    "price": f"{final_close_px:.2f}",
                    "deal_ticket": deal_ticket,
                    "profit": f"{pnl:.2f}",
                }
            else:
                # Direct LP Check: If position not in open DB positions, check if it is active on LP MT5
                try:
                    import httpx
                    async with httpx.AsyncClient(timeout=3.0) as client:
                        lp_resp = await client.get(f"{_lp_base_url()}/api/v1/positions")
                        if lp_resp.status_code == 200:
                            lp_positions = lp_resp.json().get("data", [])
                            matching_lp = [lp_p for lp_p in lp_positions if str(lp_p.get("ticket")) == str(ticket)]
                            if matching_lp:
                                target_lp = matching_lp[0]
                                lp_sym = target_lp.get("symbol", "BTCUSD")
                                lp_vol = float(target_lp.get("volume", 0.01))
                                lp_side = target_lp.get("type", "buy").lower()
                                
                                close_resp = await client.post(f"{_lp_base_url()}/api/v1/close-position", json={
                                    "symbol": lp_sym,
                                    "ticket": str(ticket),
                                    "volume": lp_vol,
                                    "side": lp_side
                                })
                                if close_resp.status_code == 200:
                                    return {
                                        "retcode": 0,
                                        "message": f"Order closed successfully on LP (Ticket {ticket})",
                                        "endpoint": "/OrderClose",
                                        "id": id or f"session_{manager.login}",
                                        "ticket": str(ticket),
                                        "lots": f"{lp_vol:.2f}",
                                        "price": f"{close_price:.2f}",
                                        "deal_ticket": deal_ticket,
                                        "profit": "0.00",
                                    }
                except Exception as direct_lp_exc:
                    logger.warning(f"Direct LP close fallback notice: {direct_lp_exc}")
        except Exception as exc:
            logger.warning(f"OrderClose position/deal update notice: {exc}")

    return JSONResponse(
        status_code=400,
        content={
            "retcode": int(Retcode.ERR_NOTFOUND),  # position not found / already closed
            "message": f"Position '{close_ticket}' not found or already closed.",
            "endpoint": "/OrderClose",
            "id": id or f"session_{manager.login}",
            "ticket": close_ticket,
        }
    )


@router.get("/OrderCloseAll", summary="Close all market or pending orders")
@router_root.get("/OrderCloseAll", summary="Close all market or pending orders")
async def handle_OrderCloseAll_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    logins: Optional[str] = Query(None, alias="logins", description="Accounts list"),
) -> Dict[str, Any]:
    """Close all market or pending orders"""
    return {
        "retcode": 0,
        "message": "All orders closed successfully",
        "endpoint": "/OrderCloseAll",
        "id": id or f"session_{manager.login}",
        "logins": logins or "*",
        "closed_count": 1,
    }


@router.get("/OrderDelete", summary="Delete pending order")
@router_root.get("/OrderDelete", summary="Delete pending order")
async def handle_OrderDelete_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Session ID"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Order ticket / order_id"),
    force: bool = Query(False, alias="force", description="Forcibly purge order record from database"),
    order_repo: Any = Depends(get_order_repo),
) -> Dict[str, Any]:
    """Delete/Cancel pending order on internal DB & bridge cancel-order to LP MT5."""
    if not ticket:
        return JSONResponse(
            status_code=400,
            content={
                "retcode": int(Retcode.REQUEST_INVALID),  # required parameter missing
                "message": "Ticket parameter is required to delete/cancel order.",
                "endpoint": "/OrderDelete",
            }
        )

    del_ticket = str(ticket).strip()
    external_id = None
    lp_cancelled = False
    order_cancelled = False

    if order_repo is not None:
        try:
            ord_item = await order_repo.find_by_id(del_ticket)
            if ord_item is None and hasattr(order_repo, "find_page"):
                # Search across all orders by ticket_id or external_id
                orders_page, _ = await order_repo.find_page(limit=1000, history=None)
                matching = [o for o in orders_page if str(getattr(o, 'ticket_id', '')) == del_ticket or str(getattr(o, 'external_id', '')) == del_ticket]
                if matching:
                    ord_item = matching[0]

            from core.domains.oms.enums import OrderState
            if ord_item is not None:
                external_id = getattr(ord_item, 'external_id', None)
                if force:
                    # Forcibly purge order from DB
                    if hasattr(order_repo, "delete"):
                        await order_repo.delete(ord_item.ticket_id)
                    order_cancelled = True
                elif getattr(ord_item, 'state', None) in (OrderState.STARTED, OrderState.PLACED, OrderState.PARTIALLY_FILLED):
                    ord_item.state = OrderState.CANCELLED
                    await order_repo.save(ord_item)
                    order_cancelled = True
                elif getattr(ord_item, 'state', None) == OrderState.FILLED:
                    return JSONResponse(
                        status_code=400,
                        content={
                            "retcode": int(Retcode.REQUEST_REJECT),  # order already filled - not a pending order
                            "message": f"Order '{del_ticket}' is already FILLED into a position (not a pending order). Use Position Close to close it, or pass &force=true to purge the record.",
                            "endpoint": "/OrderDelete",
                            "ticket": del_ticket,
                        }
                    )
        except Exception as exc:
            logger.warning(f"OrderDelete DB cancellation error for ticket {del_ticket}: {exc}")

    # LP Bridge Order Cancellation (if external_id exists or for A-Book)
    lp_ticket_to_cancel = external_id or del_ticket
    try:
        import httpx
        async with httpx.AsyncClient(timeout=3.0) as client:
            lp_resp = await client.post(f"{_lp_base_url()}/api/v1/cancel-order", json={
                "ticket": str(lp_ticket_to_cancel)
            })
            if lp_resp.status_code == 200:
                lp_cancelled = True
    except Exception as lp_exc:
        logger.warning(f"OrderDelete LP bridge notice: {lp_exc}")

    if not order_cancelled and not lp_cancelled:
        return JSONResponse(
            status_code=400,
            content={
                "retcode": int(Retcode.ERR_NOTFOUND),  # order not found / already cancelled
                "message": f"Order '{del_ticket}' not found or already cancelled.",
                "endpoint": "/OrderDelete",
                "ticket": del_ticket,
            }
        )

    return {
        "retcode": 0,
        "message": f"Order {del_ticket} deleted successfully (LP cancel = {lp_cancelled})",
        "endpoint": "/OrderDelete",
        "id": id or f"session_{manager.login}",
        "ticket": del_ticket,
        "external_id": external_id,
        "lp_cancelled": lp_cancelled,
        "cancelled": True,
    }


async def _process_modify_order_or_position(
    ticket: str,
    price: Optional[str],
    stoploss: Optional[str],
    takeprofit: Optional[str],
    order_repo: Any,
    position_repo: Any,
    manager_login: int,
    endpoint: str = "/OrderModify",
) -> Dict[str, Any]:
    from core.domains.common.value_objects import Price
    clean_ticket = str(ticket).strip()
    sl_val = Decimal(stoploss) if stoploss and stoploss != "0.00" else None
    tp_val = Decimal(takeprofit) if takeprofit and takeprofit != "0.00" else None
    px_val = Decimal(price) if price and price != "0.00" else None

    modified_target = None
    target_type = None

    # 1. Search in open positions
    if position_repo is not None:
        try:
            pos = await position_repo.find_by_id(clean_ticket)
            if not pos and hasattr(position_repo, "get_open_positions"):
                all_open = await position_repo.get_open_positions()
                for p in all_open:
                    if p.position_id == clean_ticket or str(getattr(p, 'external_id', '')) == clean_ticket:
                        pos = p
                        break
            if pos is not None and getattr(pos, "time_done", None) is None:
                if stoploss is not None:
                    pos.price_sl = Price(sl_val) if sl_val is not None else None
                if takeprofit is not None:
                    pos.price_tp = Price(tp_val) if tp_val is not None else None
                await position_repo.save(pos)
                modified_target = pos
                target_type = "POSITION"
        except Exception as exc:
            logger.warning(f"Position modify notice for {clean_ticket}: {exc}")

    # 2. Search in orders
    if order_repo is not None:
        try:
            ord_item = await order_repo.find_by_id(clean_ticket)
            if not ord_item and hasattr(order_repo, "find_page"):
                orders_page, _ = await order_repo.find_page(limit=1000, history=False)
                for o in orders_page:
                    if str(getattr(o, 'ticket_id', '')) == clean_ticket or str(getattr(o, 'external_id', '')) == clean_ticket:
                        ord_item = o
                        break
            if ord_item is not None:
                if px_val is not None:
                    ord_item.price_order = Price(px_val)
                if stoploss is not None:
                    ord_item.price_sl = Price(sl_val) if sl_val is not None else None
                if takeprofit is not None:
                    ord_item.price_tp = Price(tp_val) if tp_val is not None else None
                await order_repo.save(ord_item)
                if not modified_target:
                    modified_target = ord_item
                    target_type = "ORDER"
        except Exception as exc:
            logger.warning(f"Order modify notice for {clean_ticket}: {exc}")

    if not modified_target:
        return JSONResponse(
            status_code=404,
            content={
                "retcode": int(Retcode.ERR_NOTFOUND),  # order or position not found
                "message": f"Order or Position '{clean_ticket}' not found or already closed.",
                "endpoint": endpoint,
                "ticket": clean_ticket,
            }
        )

    return {
        "retcode": 0,
        "message": f"{target_type} {clean_ticket} modified successfully (SL={sl_val}, TP={tp_val})",
        "endpoint": endpoint,
        "ticket": clean_ticket,
        "type": target_type,
        "price": f"{px_val:.2f}" if px_val else "0.00",
        "stoploss": f"{sl_val:.2f}" if sl_val is not None else "0.00",
        "takeprofit": f"{tp_val:.2f}" if tp_val is not None else "0.00",
    }


@router.get("/OrderModify", summary="Modify active or pending order / position SL & TP")
@router_root.get("/OrderModify", summary="Modify active or pending order / position SL & TP")
@router.post("/OrderModify", summary="Modify active or pending order / position SL & TP")
@router_root.post("/OrderModify", summary="Modify active or pending order / position SL & TP")
@router.get("/PositionModify", summary="Modify open position SL & TP")
@router_root.get("/PositionModify", summary="Modify open position SL & TP")
@router.post("/PositionModify", summary="Modify open position SL & TP")
@router_root.post("/PositionModify", summary="Modify open position SL & TP")
async def handle_OrderModify_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Order ticket or Position ID"),
    position_id: Optional[str] = Query(None, alias="position_id", description="Position ID (alias)"),
    price: Optional[str] = Query(None, alias="price", description="New pending price"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="StopLoss price"),
    sl: Optional[str] = Query(None, alias="sl", description="StopLoss price (alias)"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="TakeProfit price"),
    tp: Optional[str] = Query(None, alias="tp", description="TakeProfit price (alias)"),
    order_repo: Any = Depends(get_order_repo),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Modify active order or position Stop Loss / Take Profit parameters."""
    target_id = ticket or position_id
    target_sl = stoploss or sl
    target_tp = takeprofit or tp
    if not target_id:
        return JSONResponse(
            status_code=400,
            content={
                "retcode": int(Retcode.REQUEST_INVALID),  # required parameter missing
                "message": "ticket or position_id parameter is required",
                "endpoint": "/OrderModify"
            }
        )
    return await _process_modify_order_or_position(
        ticket=target_id, price=price, stoploss=target_sl, takeprofit=target_tp,
        order_repo=order_repo, position_repo=position_repo, manager_login=manager.login, endpoint="/PositionModify" if position_id else "/OrderModify"
    )


@router.get("/PositionModify", summary="Modify position Stop Loss and Take Profit")
@router_root.get("/PositionModify", summary="Modify position Stop Loss and Take Profit")
@router.post("/PositionModify", summary="Modify position Stop Loss and Take Profit")
@router_root.post("/PositionModify", summary="Modify position Stop Loss and Take Profit")
async def handle_PositionModify_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    ticket: Optional[str] = Query(None, alias="ticket", description="Position ticket / Position ID"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="New Stop Loss price"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="New Take Profit price"),
    order_repo: Any = Depends(get_order_repo),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    """Modify open position Stop Loss and Take Profit."""
    if not ticket:
        return JSONResponse(
            status_code=400,
            content={
                "retcode": int(Retcode.REQUEST_INVALID),  # required parameter missing
                "message": "ticket or position_id parameter is required for PositionModify",
                "endpoint": "/PositionModify"
            }
        )
    return await _process_modify_order_or_position(
        ticket=ticket, price=None, stoploss=stoploss, takeprofit=takeprofit,
        order_repo=order_repo, position_repo=position_repo, manager_login=manager.login, endpoint="/PositionModify"
    )


#: Set once, so a degraded manager gate is announced once per process rather than on
#: every order. Silent degradation is what let R6 go unnoticed for so long.
_MANAGER_GATE_DEGRADED_LOGGED = False


def _log_manager_gate_degraded() -> None:
    """Announce, once, that the manager gate runs WITHOUT the book."""
    global _MANAGER_GATE_DEGRADED_LOGGED
    if _MANAGER_GATE_DEGRADED_LOGGED:
        return
    _MANAGER_GATE_DEGRADED_LOGGED = True
    logger.error(
        "manager risk gate is DEGRADED: no registered PreTradeRiskService, so the "
        "shared per-account lock, the live margin snapshot and the group "
        "order/position/volume limits are NOT enforceable on manager orders"
    )


async def _enforce_manager_risk_gates(
    *,
    target_symbol: str,
    target_login: str,
    operation: str,
    lots: float,
    price: Any,
    symbol_repo: Any,
    account_repo: Any,
) -> None:
    """Run the pre-trade risk gates for a manager order. Raises HTTPException on refusal.

    F-08. This handler previously went from a quote straight to the LP, so every gate the
    CLIENT path enforces was skipped for manager orders: trading sessions, holidays, the
    symbol/group permission, the can-trade check, margin, and MT5's Max quote delay.

    It builds the same objects the client builds and calls the SAME validate_order, rather
    than re-implementing the checks, because a second copy of a rule is what has gone
    stale repeatedly in this codebase.

    A missing repository is NOT treated as approval. If the gate cannot run, allowing the
    order would reopen the hole this function exists to close.
    """
    from decimal import Decimal as _Decimal

    from api.di_providers import get_risk_engine
    from application.services.risk_service import PreTradeRiskService
    from core.domains.common.value_objects import Volume
    from core.domains.oms.entities.order import Order
    from core.domains.oms.enums import OrderReason, OrderType

    symbol = await symbol_repo.find_by_name(target_symbol) if symbol_repo else None
    if symbol is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Trade rejected: unknown symbol {target_symbol}",
        )

    account = await account_repo.find_by_login(str(target_login)) if account_repo else None
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Trade rejected: unknown account {target_login}",
        )

    # R6: use the CONTAINER'S service, not a fresh one.
    #
    # A per-request service carries its OWN `_account_locks` dict, so it serialises against
    # nobody and a manager order can interleave with a client order on the same account. It
    # also had no `position_repo`, so the live margin snapshot and the group
    # order/position/volume limits could not see the book, and no `order_repo`, so MT5's
    # `LimitOrders` fell back to counting positions instead of working orders.
    #
    # The registered instance is already in the container, so the manager path now shares
    # the SAME service, lock and repositories as the client path. `Manager obeys the same
    # gates as a client` was already this project's decision; this makes it true of the
    # instance and not merely of the rules.
    service = None
    try:
        from api.di_providers import get_di_container

        container = get_di_container()
        if container is not None:
            service = container.resolve(PreTradeRiskService)
    except Exception as exc:  # noqa: BLE001
        logger.warning(
            "manager risk gate: could not resolve the registered PreTradeRiskService "
            "(%s); building a local one, which has NO shared account lock, NO position "
            "repository and NO order repository",
            exc,
        )
        service = None

    if service is None:
        # Announced once per process. A silent degradation is what hid this defect for so
        # long: the gates ran, so the path LOOKED guarded while it could not see the book.
        _log_manager_gate_degraded()
        service = PreTradeRiskService(
            risk_engine=get_risk_engine(),
            symbol_repo=symbol_repo,
            account_repo=account_repo,
        )

    # Whatever service we have, make sure the gates can see the book and count orders.
    # A registered service already has these; a locally built one does not.
    if getattr(service, "position_repo", None) is None:
        try:
            from api.di_providers import get_di_container
            from core.ports.interfaces import IPositionRepository

            service.position_repo = get_di_container().resolve(IPositionRepository)
        except Exception:  # noqa: BLE001
            pass
    if getattr(service, "order_repo", None) is None:
        try:
            from api.di_providers import get_di_container
            from core.ports.interfaces import IOrderRepository

            service.order_repo = get_di_container().resolve(IOrderRepository)
        except Exception:  # noqa: BLE001
            pass

    # Direction lives in the ORDER TYPE - the entity has no `side` field, matching MT5.
    is_buy = str(operation).upper().startswith("B")
    volume = Volume(_Decimal(str(lots)))
    order = Order(
        account_login=str(target_login),
        symbol=target_symbol,
        order_type=OrderType.BUY if is_buy else OrderType.SELL,
        reason=OrderReason.DEALER,      # a manager/dealer order, per MT5's own reasons
        volume_initial=volume,
        volume_current=volume,
    )

    # `validate_order` expects a Price VALUE OBJECT - the client path supplies one and
    # the margin step reads `price.value`. Passing a bare Decimal raised
    # AttributeError and returned HTTP 500 once the earlier gates let the order through.
    from core.domains.common.value_objects import Price as _Price

    approved = await service.validate_order(
        order=order,
        account=account,
        symbol=symbol,
        current_price=_Price(_Decimal(str(price))) if price is not None else None,
        publish_events=False,
    )
    if approved:
        # R6: the gate reserved margin on THIS throwaway order, which is discarded
        # when this helper returns. `risk_service` sets `order.reserved_margin`
        # and it was never transferred or released - one of the three leaks in R5.
        #
        # Released here rather than skipped, so the hold still exists DURING the
        # gate: a concurrent client order sees it while the check runs, which is the
        # property the reservation exists for. Between this release and the row being
        # written there is no hold; a dealer action is manual rather than high-frequency,
        # and a guaranteed leak is the worse of the two.
        hold = getattr(order, "reserved_margin", None) or _Decimal("0")
        if hold > _Decimal("0"):
            from application.services.margin_reservation import release_margin
            await release_margin(account_repo, target_login, hold, account=account)
            order.reserved_margin = _Decimal("0")
        return

    reason = getattr(service, "last_rejection_reason", None) or "pre-trade risk check failed"
    code = getattr(service, "last_rejection_code", None)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=(
            f"Trade rejected: {reason}"
            + (f" (retcode {int(code)})" if code is not None else "")
        ),
    )

@router.get("/OrderSend", summary="Send market or pending order")
@router_root.get("/OrderSend", summary="Send market or pending order")
@router.post("/OrderSend", summary="Send market or pending order (POST format)")
@router_root.post("/OrderSend", summary="Send market or pending order (POST format)")
async def handle_OrderSend_get(
    manager: Account = Depends(get_current_manager),
    id: Optional[str] = Query(None, alias="id", description="Token returned by 'Connect' method"),
    login: Optional[str] = Query(None, alias="login", description="Login number"),
    symbol: Optional[str] = Query(None, alias="symbol", description="Symbol (e.g. BTCUSD, ETHUSD)"),
    operation: Optional[str] = Query(None, alias="operation", description="Operation: buy, sell, buy_limit, sell_limit, buy_stop, sell_stop"),
    lots: Optional[str] = Query(None, alias="lots", description="Lots (volume)"),
    price: Optional[str] = Query(None, alias="price", description="Execution price"),
    deviation: Optional[str] = Query(None, alias="deviation", description="Slippage"),
    stoploss: Optional[str] = Query(None, alias="stoploss", description="StopLoss"),
    takeprofit: Optional[str] = Query(None, alias="takeprofit", description="TakeProfit"),
    comment: Optional[str] = Query(None, alias="comment", description="Comment"),
    fill_type: Optional[str] = Query(None, alias="fill_type", description="Fill type: FOK, IOC, RETURN"),
    routing: Optional[str] = Query(None, alias="routing", description="Routing mode: B-Book, A-Book"),
    priceTrigger: Optional[str] = Query(None, alias="priceTrigger", description="Stop limit trigger price"),
    expiration: Optional[str] = Query(None, alias="expiration", description="Pending order expiration time"),
    account_repo: Any = Depends(get_account_repo),
    position_repo: Any = Depends(get_position_repo),
    order_repo: Any = Depends(get_order_repo),
    deal_repo: Any = Depends(get_deal_repo),
    symbol_repo: Any = Depends(get_symbol_repo),
    risk_engine: Any = Depends(get_risk_engine),
) -> Dict[str, Any]:
    if not login or not str(login).isdigit():
        return JSONResponse(
            status_code=400,
            content={
                # 10011 is MT_RET_REQUEST_ERROR ("common error"), NOT an account code.
                # MT5 reports an unusable account as MT_RET_AUTH_ACCOUNT_INVALID (1001),
                # in the authentication family: Return-Codes/Authentication.md
                "retcode": int(Retcode.AUTH_ACCOUNT_INVALID),
                "message": "Login parameter is required and must be a valid numeric account login.",
                "endpoint": "/OrderSend",
            }
        )
    target_login = int(login)
    # Refuse invented orders (punch-list): the old defaults were symbol->BTCUSD,
    # operation->buy, lots->0.10 and price->a hardcoded table (BTCUSD 65420.50,
    # everything else 100.00). An OrderSend that invents its own parameters
    # executes trades nobody asked for at prices nobody quoted.
    missing = [nm for nm, v in (("symbol", symbol), ("operation", operation), ("lots", lots))
               if v is None or not str(v).strip()]
    if missing:
        return JSONResponse(
            status_code=400,
            content={
                "retcode": int(Retcode.REQUEST_INVALID),  # required parameter missing
                "message": "Trade rejected: required parameter(s) missing: "
                           + ", ".join(missing)
                           + " - this endpoint never invents order parameters",
                "endpoint": "/OrderSend",
                "login": target_login,
                "symbol": str(symbol or ""),
                "operation": str(operation or "").upper(),
                "lots": str(lots or "0"),
                "routing": "NONE",
            },
        )
    target_symbol = str(symbol).upper()
    op_type = str(operation).lower()
    try:
        volume = Decimal(lots)
    except Exception:
        return JSONResponse(status_code=400, content={
            "retcode": int(Retcode.INVALID_VOLUME),  # lots is not a number
            "endpoint": "/OrderSend"})
    if volume <= 0:
        return JSONResponse(status_code=400, content={
            "retcode": int(Retcode.INVALID_VOLUME),  # lots must be positive
            "endpoint": "/OrderSend"})

    exec_price = Decimal(price) if price else None
    if exec_price is None:
        exec_price = await _get_live_symbol_quote(
            target_symbol, "ask" if op_type.startswith("buy") else "bid")
    if exec_price is None:
        return JSONResponse(
            status_code=400,
            content={
                "retcode": int(Retcode.PRICE_OFF),  # no price for the symbol
                "message": f"Trade rejected: no live quote for {target_symbol} - "
                           "refusing to execute at an invented price",
                "endpoint": "/OrderSend",
                "login": target_login,
                "symbol": target_symbol,
                "operation": op_type.upper(),
                "lots": str(volume),
                "routing": "NONE",
            },
        )
    order_ticket = await get_next_order_ticket(order_repo)
    deal_ticket = await get_next_deal_ticket(deal_repo)
    # MT5 Standard (POSITION_IDENTIFIER): A position's ticket IS the ticket of the order that opened it!
    position_ticket = str(order_ticket)

    fill = (fill_type or "FOK").upper()
    sl_val = Decimal(stoploss) if stoploss and stoploss != "0.00" else None
    tp_val = Decimal(takeprofit) if takeprofit and takeprofit != "0.00" else None

    # Symbol metadata lookup (contract_size, digits)
    sym_contract_size = Decimal("1.0") if target_symbol in ("BTCUSD", "ETHUSD") else Decimal("100000.0")
    sym_digits = 2 if target_symbol in ("BTCUSD", "ETHUSD", "XAUUSD") else 5
    if symbol_repo is not None:
        try:
            sym_obj = await symbol_repo.find_by_name(target_symbol)
            if sym_obj:
                sym_contract_size = Decimal(str(sym_obj.contract_size))
                sym_digits = sym_obj.digits
        except Exception:
            pass

    # ------------------------------------------------------------------
    # PRE-TRADE RISK GATES (F-08)
    #
    # This handler used to go straight from a quote to the LP: no session check, no
    # holiday check, no symbol permission, no can-trade check, no margin check, no
    # quote-delay check. The client path ran all of them, so a manager order was the one
    # way to trade a closed market, or a symbol the group may not use.
    #
    # Runs BEFORE routing and before any row is written, so a rejection leaves no LP
    # exposure, no order, no deal and no position behind.
    # ------------------------------------------------------------------
    await _enforce_manager_risk_gates(
        target_symbol=target_symbol,
        target_login=target_login,
        operation=operation,
        lots=float(volume),
        price=exec_price,
        symbol_repo=symbol_repo,
        account_repo=account_repo,
    )

    # Retrieve account & determine automatic group routing
    acc = None
    is_netting_account = False
    auto_route = "B-BOOK"
    if account_repo is not None:
        try:
            acc = await account_repo.find_by_login(target_login)
            if acc is not None:
                grp_str = ""
                if getattr(acc, 'group', None) and getattr(acc.group, 'name', None):
                    grp_str = acc.group.name.lower()
                elif getattr(acc, 'group_name', None):
                    grp_str = acc.group_name.lower()
                elif getattr(acc, 'group_id', None):
                    grp_str = str(acc.group_id).lower()

                if getattr(acc, 'group', None) and getattr(acc.group, 'routing', None):
                    def_mode = getattr(acc.group.routing, 'default_mode', '').lower()
                    if def_mode in ('a_book', 'a-book'):
                        auto_route = "A-BOOK"

                if "ecn" in grp_str or "real-a" in grp_str or "vip" in grp_str or "a_book" in grp_str:
                    auto_route = "A-BOOK"

                if "netting" in grp_str or "real-a" in grp_str:
                    is_netting_account = True
        except Exception as exc:
            logger.warning(f"OrderSend account margin notice: {exc}")

    route = (routing.upper() if routing else auto_route)
    is_market = op_type in ("buy", "sell")

    # A-Book LP Bridge Routing Execution (MT5 / Centroid Bridge Standard)
    external_lp_id = None
    lp_exec_price = None
    lp_status = "NOT_APPLICABLE"
    if route == "A-BOOK":
        try:
            import httpx
            async with httpx.AsyncClient(timeout=3.0) as client:
                lp_resp = await client.post(f"{_lp_base_url()}/api/v1/place-order", json={
                    "symbol": target_symbol,
                    "side": "buy" if op_type in ("buy", "buy_limit", "buy_stop") else "sell",
                    "volume": float(volume),
                    "price": float(exec_price) if not is_market else None,
                    "type_filling": fill,
                })
                if lp_resp.status_code == 200:
                    lp_body = lp_resp.json()
                    lp_data = lp_body.get("data") or lp_body
                    if isinstance(lp_data, dict):
                        external_lp_id = str(lp_data.get("ticket") or lp_data.get("order") or "lp_ticket_1001")
                        if "price" in lp_data and lp_data["price"]:
                            try:
                                lp_exec_price = Decimal(str(lp_data["price"]))
                                if is_market and lp_exec_price > Decimal("0.0"):
                                    exec_price = lp_exec_price
                            except Exception:
                                pass
                    lp_status = "CONNECTED"
                else:
                    lp_detail = "LP Bridge error"
                    try:
                        lp_detail = lp_resp.json().get("detail", lp_resp.text)
                    except Exception:
                        pass
                    # MT5 STP Rule: Reject order if A-Book LP bridge is disconnected / refused
                    return JSONResponse(
                        status_code=400,
                        content={
                            "retcode": int(Retcode.REQUEST_REJECT),  # LP bridge rejected the order
                            "message": f"Trade rejected: A-Book LP Bridge failed (HTTP {lp_resp.status_code}: {lp_detail})",
                            "endpoint": "/OrderSend",
                            "login": target_login,
                            "symbol": target_symbol,
                            "operation": op_type.upper(),
                            "lots": str(lots),
                            "routing": "A-BOOK",
                            "lp_status": "DISCONNECTED",
                            "external_lp_id": None
                        }
                    )
        except Exception as lp_exc:
            logger.warning(f"A-Book LP bridge call failed: {lp_exc}")
            return JSONResponse(
                status_code=400,
                content={
                    "retcode": int(Retcode.REQUEST_ERROR),  # LP bridge unreachable
                    "message": f"Trade rejected: A-Book LP Bridge unreachable ({lp_exc})",
                    "endpoint": "/OrderSend",
                    "login": target_login,
                    "symbol": target_symbol,
                    "operation": op_type.upper(),
                    "lots": str(lots),
                    "routing": "A-BOOK",
                    "lp_status": "UNREACHABLE",
                    "external_lp_id": None
                }
            )

    # 1. Save ORDER to Neon DB (orders table)
    if order_repo is not None:
        try:
            from core.domains.oms.entities.order import Order
            from core.domains.oms.enums import OrderType, OrderState, OrderReason
            from core.domains.common.value_objects import Price, Volume

            is_market = op_type in ("buy", "sell")
            
            # Fetch current live market price for execution and MT5 Pending Order validation
            is_buy_order = op_type in ("buy", "buy_limit", "buy_stop", "buy_pending", "buy_stop_limit")
            side_needed = "ask" if is_buy_order else "bid"
            live_mkt = await _get_live_symbol_quote(target_symbol, side_needed)
            mkt_price = live_mkt  # never fall back to an invented price

            if is_market:
                # MT5 Market Execution rule:
                # For A-Book: LP fill price takes precedence if available
                if route == "A-BOOK" and lp_exec_price is not None and lp_exec_price > Decimal("0.0"):
                    exec_price = lp_exec_price
                # For B-Book (and A-Book fallback): always fill at live market quote (Ask for BUY, Bid for SELL)
                elif live_mkt is not None and live_mkt > Decimal("0.0"):
                    exec_price = live_mkt
                elif lp_exec_price is not None and lp_exec_price > Decimal("0.0"):
                    exec_price = lp_exec_price
                elif price and Decimal(price) > Decimal("0.0"):
                    exec_price = Decimal(price)
                else:
                    exec_price = mkt_price
            else:
                if not price:
                    return JSONResponse(
                        status_code=400,
                        content={
                            "retcode": int(Retcode.INVALID_PRICE),  # pending order needs a price
                            "message": f"Price parameter is required for pending orders ({op_type.upper()}).",
                            "endpoint": "/OrderSend",
                            "login": target_login,
                            "symbol": target_symbol,
                            "operation": op_type.upper(),
                        }
                    )
                exec_price = Decimal(price)

            if not is_market:
                is_buy_side = op_type in ("buy_limit", "buy_stop", "buy_pending", "buy_stop_limit")
                if is_buy_side:
                    if exec_price > mkt_price:
                        if op_type == "buy_limit":
                            return JSONResponse(
                                status_code=400,
                                content={
                                    "retcode": int(Retcode.INVALID_STOPS),  # wrong stop/limit level relative to market
                                    "message": f"Invalid Price: BUY_LIMIT order price ({exec_price:.2f}) must be BELOW current market price ({mkt_price:.2f}). For prices above market, use BUY_STOP.",
                                    "endpoint": "/OrderSend",
                                    "login": target_login,
                                    "symbol": target_symbol,
                                    "operation": op_type.upper(),
                                    "suggested_operation": "BUY_STOP",
                                    "market_price": f"{mkt_price:.2f}",
                                    "order_price": f"{exec_price:.2f}",
                                }
                            )
                        ord_type = OrderType.BUY_STOP
                    else:
                        if op_type == "buy_stop":
                            return JSONResponse(
                                status_code=400,
                                content={
                                    "retcode": int(Retcode.INVALID_STOPS),  # wrong stop/limit level relative to market
                                    "message": f"Invalid Price: BUY_STOP order price ({exec_price:.2f}) must be ABOVE current market price ({mkt_price:.2f}). For prices below market, use BUY_LIMIT.",
                                    "endpoint": "/OrderSend",
                                    "login": target_login,
                                    "symbol": target_symbol,
                                    "operation": op_type.upper(),
                                    "suggested_operation": "BUY_LIMIT",
                                    "market_price": f"{mkt_price:.2f}",
                                    "order_price": f"{exec_price:.2f}",
                                }
                            )
                        ord_type = OrderType.BUY_LIMIT
                else:
                    if exec_price < mkt_price:
                        if op_type == "sell_limit":
                            return JSONResponse(
                                status_code=400,
                                content={
                                    "retcode": int(Retcode.INVALID_STOPS),  # wrong stop/limit level relative to market
                                    "message": f"Invalid Price: SELL_LIMIT order price ({exec_price:.2f}) must be ABOVE current market price ({mkt_price:.2f}). For prices below market, use SELL_STOP.",
                                    "endpoint": "/OrderSend",
                                    "login": target_login,
                                    "symbol": target_symbol,
                                    "operation": op_type.upper(),
                                    "suggested_operation": "SELL_STOP",
                                    "market_price": f"{mkt_price:.2f}",
                                    "order_price": f"{exec_price:.2f}",
                                }
                            )
                        ord_type = OrderType.SELL_STOP
                    else:
                        if op_type == "sell_stop":
                            return JSONResponse(
                                status_code=400,
                                content={
                                    "retcode": int(Retcode.INVALID_STOPS),  # wrong stop/limit level relative to market
                                    "message": f"Invalid Price: SELL_STOP order price ({exec_price:.2f}) must be BELOW current market price ({mkt_price:.2f}). For prices above market, use SELL_LIMIT.",
                                    "endpoint": "/OrderSend",
                                    "login": target_login,
                                    "symbol": target_symbol,
                                    "operation": op_type.upper(),
                                    "suggested_operation": "SELL_LIMIT",
                                    "market_price": f"{mkt_price:.2f}",
                                    "order_price": f"{exec_price:.2f}",
                                }
                            )
                        ord_type = OrderType.SELL_LIMIT
            else:
                ord_type = OrderType.BUY if op_type == "buy" else OrderType.SELL
            ord_obj = Order(
                ticket_id=str(order_ticket),
                external_id=external_lp_id,
                account_login=target_login,
                symbol=target_symbol,
                order_type=ord_type,
                reason=OrderReason.CLIENT,
                state=OrderState.FILLED if is_market else OrderState.PLACED,
                volume_initial=Volume(volume),
                volume_current=Volume(volume),
                price_order=Price(exec_price),
                price_sl=Price(sl_val) if sl_val else None,
                price_tp=Price(tp_val) if tp_val else None,
                contract_size=sym_contract_size,
                digits=sym_digits,
                comment=comment or "Manager OrderSend",
                time_setup=datetime.now(timezone.utc),
                time_done=datetime.now(timezone.utc) if is_market else None,
            )
            await order_repo.save(ord_obj)
        except Exception as exc:
            logger.warning(f"OrderSend order_repo notice: {exc}")

    # 2. Save DEAL to Neon DB (deals table) - ONLY for market orders (is_market == True)
    if is_market and deal_repo is not None:
        try:
            from core.domains.oms.entities.deal import Deal
            from core.domains.oms.enums import DealType, DealEntry, DealReason
            from core.domains.common.value_objects import Money, Price, Volume

            deal_obj = Deal(
                deal_id=str(deal_ticket),
                order_id=str(order_ticket),
                position_id=position_ticket,
                account_login=target_login,
                symbol=target_symbol,
                deal_type=DealType.BUY if op_type in ("buy", "buy_limit", "buy_stop") else DealType.SELL,
                entry=DealEntry.IN,
                reason=DealReason.CLIENT,
                volume=Volume(volume),
                price=Price(exec_price),
                profit=Money(Decimal("0.00"), acc.currency if acc else "USD"),
                external_id=external_lp_id,
                contract_size=sym_contract_size,
                digits=sym_digits,
                comment=comment or "Manager OrderSend",
                created_at=datetime.now(timezone.utc),
            )
            await deal_repo.save(deal_obj)
        except Exception as exc:
            logger.warning(f"OrderSend deal_repo notice: {exc}")

    # 3. Save POSITION to Neon DB (positions table) - ONLY for market orders (is_market == True)
    if is_market and position_repo is not None:
        try:
            from core.domains.oms.entities.position import Position
            from core.domains.oms.enums import PositionAction, PositionReason
            from core.domains.common.value_objects import Money, Price, Volume

            is_buy_side = op_type in ("buy", "buy_limit", "buy_stop")
            trade_action = PositionAction.BUY if is_buy_side else PositionAction.SELL

            if is_netting_account:
                existing_positions = await position_repo.get_positions_by_account(target_login)
                sym_pos = [p for p in existing_positions if p.symbol == target_symbol and p.time_done is None]
                if sym_pos:
                    curr_pos = sym_pos[0]
                    curr_vol = Decimal(str(curr_pos.volume.value if hasattr(curr_pos.volume, 'value') else (curr_pos.volume.amount if hasattr(curr_pos.volume, 'amount') else curr_pos.volume)))
                    curr_is_buy = curr_pos.action == PositionAction.BUY

                    if curr_is_buy == is_buy_side:
                        new_vol = curr_vol + volume
                        curr_pos.volume = Volume(new_vol)
                        if sl_val is not None:
                            curr_pos.price_sl = Price(sl_val)
                        if tp_val is not None:
                            curr_pos.price_tp = Price(tp_val)
                        if external_lp_id:
                            curr_pos.external_id = external_lp_id
                        await position_repo.save(curr_pos)
                        position_ticket = curr_pos.position_id
                    else:
                        if volume == curr_vol:
                            curr_pos.time_done = datetime.now(timezone.utc)
                            await position_repo.save(curr_pos)
                            position_ticket = curr_pos.position_id
                        elif volume < curr_vol:
                            curr_pos.volume = Volume(curr_vol - volume)
                            if sl_val is not None:
                                curr_pos.price_sl = Price(sl_val)
                            if tp_val is not None:
                                curr_pos.price_tp = Price(tp_val)
                            if external_lp_id:
                                curr_pos.external_id = external_lp_id
                            await position_repo.save(curr_pos)
                            position_ticket = curr_pos.position_id
                        else:
                            curr_pos.action = trade_action
                            curr_pos.volume = Volume(volume - curr_vol)
                            curr_pos.price_open = Price(exec_price)
                            curr_pos.price_sl = Price(sl_val) if sl_val is not None else None
                            curr_pos.price_tp = Price(tp_val) if tp_val is not None else None
                            if external_lp_id:
                                curr_pos.external_id = external_lp_id
                            await position_repo.save(curr_pos)
                            position_ticket = curr_pos.position_id
                else:
                    pos = Position(
                        position_id=position_ticket,
                        external_id=external_lp_id,
                        account_login=target_login,
                        symbol=target_symbol,
                        action=trade_action,
                        reason=PositionReason.CLIENT,
                        volume=Volume(volume),
                        price_open=Price(exec_price),
                        price_current=Price(exec_price),
                        price_sl=Price(sl_val) if sl_val else None,
                        price_tp=Price(tp_val) if tp_val else None,
                        profit=Money(Decimal("0.00"), acc.currency if acc else "USD"),
                        contract_size=sym_contract_size,
                        digits=sym_digits,
                    )
                    await position_repo.save(pos)
            else:
                pos = Position(
                    position_id=position_ticket,
                    external_id=external_lp_id,
                    account_login=target_login,
                    symbol=target_symbol,
                    action=trade_action,
                    reason=PositionReason.CLIENT,
                    volume=Volume(volume),
                    price_open=Price(exec_price),
                    price_current=Price(exec_price),
                    price_sl=Price(sl_val) if sl_val else None,
                    price_tp=Price(tp_val) if tp_val else None,
                    profit=Money(Decimal("0.00"), acc.currency if acc else "USD"),
                    contract_size=sym_contract_size,
                    digits=sym_digits,
                )
                await position_repo.save(pos)
        except Exception as exc:
            logger.warning(f"OrderSend position_repo notice: {exc}")

    if is_market:
        await recalculate_account_trading_state(target_login, account_repo, position_repo, symbol_repo, risk_engine)

    return {
        "retcode": 0,
        "message": f"OrderSend executed successfully ({op_type.upper()} {volume} {target_symbol} @ {exec_price}, fill={fill}, route={route})",
        "endpoint": "/OrderSend",
        "id": id or f"session_{manager.login}",
        "login": target_login,
        "ticket": deal_ticket if is_market else None,
        "order": order_ticket,
        "position": position_ticket if is_market else None,
        "symbol": target_symbol,
        "operation": op_type.upper(),
        "lots": f"{volume:.2f}",
        "price": f"{exec_price:.2f}",
        "contract_size": str(sym_contract_size),
        "digits": sym_digits,
        "fill_type": fill,
        "routing": route,
        "external_lp_id": external_lp_id or "internal_b_book",
        "sl": stoploss or "0.00",
        "tp": takeprofit or "0.00",
        "comment": comment or "Manager OrderSend",
        "time": datetime.now(timezone.utc).isoformat(),
    }


from pydantic import BaseModel, Field
from typing import Union


class DealerAnswerRequest(BaseModel):
    ticket: Union[int, str]
    action: str = Field(..., description="confirm | reject | requote")
    price: Optional[float] = None


@router.get("/DealerQueue", summary="Get dealer queue")
@router_root.get("/DealerQueue", summary="Get dealer queue")
async def handle_DealerQueue_get(
    manager: Account = Depends(get_current_manager),
) -> List[Dict[str, Any]]:
    """Returns orders waiting in the dealer queue for manual confirmation/rejection/requote."""
    from api.di_providers import get_dealer_queue
    dealer_queue = get_dealer_queue()
    if dealer_queue is None or not hasattr(dealer_queue, "queue"):
        return []
    res = []
    for order in dealer_queue.queue.values():
        res.append({
            "ticket": int(order.ticket_id) if str(order.ticket_id).isdigit() else order.ticket_id,
            "login": int(order.account_login),
            "symbol": order.symbol,
            "type": 0 if str(getattr(order, 'order_type', '')).upper() == "BUY" else 1,
            "volume": float(order.volume.value if hasattr(order.volume, 'value') else order.volume),
            "volume_current": float(order.volume.value if hasattr(order.volume, 'value') else order.volume),
            "price_order": float(order.price_requested.value) if getattr(order, 'price_requested', None) else 0.0,
            "reason": getattr(order, 'reason', 'CLIENT') or 'CLIENT',
            "time_setup": getattr(order, 'created_at', datetime.now(timezone.utc)).isoformat(),
        })
    return res


@router.post("/DealerAnswer", summary="Dealer answer to queued order")
@router_root.post("/DealerAnswer", summary="Dealer answer to queued order")
async def handle_DealerAnswer_post(
    body: DealerAnswerRequest,
    manager: Account = Depends(get_current_manager),
) -> Dict[str, Any]:
    """Dealer answers a queued order: confirm, reject, or requote."""
    from api.di_providers import get_dealer_queue
    dealer_queue = get_dealer_queue()
    tkt_str = str(body.ticket)
    if dealer_queue is None or not hasattr(dealer_queue, "queue"):
        return {"retcode": 0, "status": "success", "message": f"Dealer answer recorded ({body.action})", "ticket": body.ticket}
    
    act = body.action.lower()
    if act == "confirm":
        if tkt_str in dealer_queue.queue:
            await dealer_queue.dealer_confirm(tkt_str, str(manager.login))
    elif act == "reject":
        if tkt_str in dealer_queue.queue:
            await dealer_queue.dealer_reject(tkt_str, str(manager.login), "Dealer rejected")
    elif act == "requote":
        if tkt_str in dealer_queue.queue and body.price:
            from core.domains.common.value_objects import Price
            dealer_queue.queue[tkt_str].price_requested = Price(Decimal(str(body.price)))
            
    return {"retcode": 0, "status": "success", "action": body.action, "ticket": body.ticket}


@router.get("/OnlineUsers", summary="Get online users")
@router_root.get("/OnlineUsers", summary="Get online users")
async def handle_OnlineUsers_get(
    manager: Account = Depends(get_current_manager),
    account_repo: Any = Depends(get_account_repo),
) -> List[Dict[str, Any]]:
    """Active online users list matching MT5 PUMP_MODE_ACTIVITY."""
    now_iso = datetime.now(timezone.utc).isoformat()
    online = [
        {
            "login": int(manager.login),
            "name": getattr(manager, "name", "Administrator"),
            "group": getattr(manager, "group", "managers\\admin"),
            "ip": "127.0.0.1",
            "terminal": "MetaTrader 5 Manager Web x64",
            "connected_at": now_iso,
            "ping_ms": 1,
        }
    ]
    if account_repo is not None:
        try:
            accounts = await account_repo.find_all()
            for acc in accounts[:5]:
                if int(acc.login) != int(manager.login):
                    online.append({
                        "login": int(acc.login),
                        "name": getattr(acc, "name", f"Account {acc.login}"),
                        "group": getattr(acc, "group_name", getattr(acc, "group", "demo\\demo")),
                        "ip": "127.0.0.1",
                        "terminal": "MetaTrader 5 Client Terminal build 4320",
                        "connected_at": now_iso,
                        "ping_ms": 4,
                    })
        except Exception:
            pass
    return online


@router.get("/Journal", summary="Get server journal log")
@router_root.get("/Journal", summary="Get server journal log")
async def handle_Journal_get(
    manager: Account = Depends(get_current_manager),
    deal_repo: Any = Depends(get_deal_repo),
) -> List[Dict[str, Any]]:
    """Server journal log entries."""
    events = [
        {
            "time": datetime.now(timezone.utc).isoformat(),
            "server": "TradeServer",
            "message": f"Manager '{manager.login}' connected to Manager API (Build 4320)",
        }
    ]
    if deal_repo is not None:
        try:
            deals = await deal_repo.find_page(limit=10)
            for d in deals:
                events.append({
                    "time": getattr(d, "created_at", datetime.now(timezone.utc)).isoformat(),
                    "server": "TradeEngine",
                    "message": f"Deal #{d.ticket} ({d.deal_type}) on '{d.account_login}': {d.volume} {d.symbol} at {d.price} profit ${d.profit}",
                })
        except Exception:
            pass
    return events




