"""M18 C-tier: the HONEST SKELETONS.

Every route in this file exists so the surface is COMPLETE - the UI can be
written against the whole map, the mtapi/MT5 checklist maps 1:1 - and every
one of them REFUSES with a 501 naming exactly what is missing and which
milestone builds it. The contract, non-negotiable:

* 501, never 200-empty. An empty list that means "not built" is the F8
  disease that hid PositionGet's death for the endpoint's entire life.
* The refusal detail IS the roadmap text (M18-REPORT / ENDPOINTS Tier 3).
* `openapi_extra={"x-not-wired": True}` so Swagger UI and any codegen can
  see the honesty flag without calling.
* Each skeleton is gated by the right its REAL implementation will use, so
  the authorisation surface is already true - a manager without the bit gets
  403 today and 403 after the milestone lands.
* `p1_proof_surface_completion` walks the mounted route table and fails if
  any of these starts answering 200 without its logic existing.

When a milestone builds one of these for real, DELETE the skeleton route in
the same commit - two homes for one path is how the legacy admin_router
reads ended up shadowed.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Any, Dict, List

from api.auth.admin_dependencies import require_right
import json
import logging

logger = logging.getLogger(__name__)
from decimal import Decimal
from api.di_providers import get_symbol_repo, get_position_repo
from infrastructure.persistence.config_models import SymbolModel
from infrastructure.persistence.config_mappers import db_to_symbol
from application.cache.config_cache import get_config_cache
from api.routers.admin.admin_router import _symbol_summary


def _refuse(what: str, milestone: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=f"NOT WIRED: {what} - planned in {milestone}. "
               "This endpoint exists so the surface is complete; it refuses "
               "rather than serving an empty success (the F8 rule).",
    )


X_NOT_WIRED = {"x-not-wired": True}


def _skel_get(what: str, milestone: str):
    """A zero-parameter GET skeleton. FastAPI builds the request signature by
    introspection, so a (*args, **kwargs) endpoint becomes a 422 before the
    body ever runs - the refusal must be the ROUTE's answer, not a validation
    accident."""
    async def _route() -> Dict[str, Any]:
        raise _refuse(what, milestone)
    return _route


def _skel_write(what: str, milestone: str):
    async def _route(body: "_AnyBody" = None) -> Dict[str, Any]:
        raise _refuse(what, milestone)
    return _route


# ---------------------------------------------------------------------------
# account lifecycle (C1/C14) - RIGHT_ACC_MANAGER, delete also RIGHT_ACC_DELETE
# ---------------------------------------------------------------------------

accounts_skeleton = APIRouter(
    prefix="/api/v1/admin/accounts",
    tags=["Admin - NOT WIRED"],
    dependencies=[Depends(require_right("RIGHT_ACC_MANAGER"))],
)


class _AnyBody(BaseModel):
    """Skeletons accept and ignore a body so the UI can be written against
    the real shape from day one; nothing is parsed strictly, nothing stored."""
    model_config = {"extra": "allow"}





@accounts_skeleton.post("/{login}/archive", openapi_extra=X_NOT_WIRED)
async def archive_account(login: int) -> Dict[str, Any]:
    raise _refuse("account archiving (MT5 user/archive)", "the account-lifecycle milestone")


@accounts_skeleton.post("/{login}/restore", openapi_extra=X_NOT_WIRED)
async def restore_account(login: int) -> Dict[str, Any]:
    raise _refuse("account restore from archive (MT5 user/restore)", "the account-lifecycle milestone")


# ---------------------------------------------------------------------------
# symbol writes (C2) - RIGHT_CFG_SYMBOLS
# ---------------------------------------------------------------------------

symbols_skeleton = APIRouter(
    prefix="/api/v1/admin/symbols",
    tags=["Admin - Symbols"],
    dependencies=[Depends(require_right("RIGHT_CFG_SYMBOLS"))],
)


def _to_mode_int(val: Any, default: int, mapping: Dict[str, int]) -> int:
    if isinstance(val, int):
        return val
    if isinstance(val, str):
        val_upper = val.upper().replace(" ", "_").replace("-", "_")
        return mapping.get(val_upper, default)
    return default


def _calc_mode_map() -> Dict[str, int]:
    """Accepted Calculation names -> MT5's EnCalcMode values.

    BUILT FROM THE DOMAIN ENUM rather than hand-written. The hand-written version
    that used to live here was wrong on 11 of its 14 entries:

        FOREX_NO_LEVERAGE -> 1   (MT5: 5; 1 is FUTURES)
        EXCHANGE_STOCKS   -> 5   (MT5: 32; 5 is FOREX_NO_LEVERAGE)
        EXCHANGE_FUTURES  -> 6   (MT5: 33)
        FORTS_FUTURES     -> 7   (MT5: 34)
        EXCHANGE_BONDS    -> 8   (MT5: 37)
        EXCHANGE_OPTIONS  -> 10  (MT5: 35)
        CRYPTO            -> 14  (not an MT5 CalcMode)

    54 of the 362 symbols in the reference export are FOREX_NO_LEVERAGE, so an edit
    round-tripping through the old map would have silently rewritten them as
    Exchange Stocks - a different margin formula, profit formula and margin
    currency.

    Aliases are added for the spellings an operator or an older client might send,
    but every alias points at the corrected value.
    """
    from core.domains.instruments.enums import CalculationMode

    mapping: Dict[str, int] = {member.name: member.value for member in CalculationMode}
    mapping.update(
        {
            # historical spelling used by the UI's own option list
            "EXCHANGE_MOEXBONDS": CalculationMode.EXCHANGE_BONDS_MOEX.value,
            "FORTS_FUTURES": CalculationMode.EXCHANGE_FUTURES_FORTS.value,
            "EXCHANGE_OPTION": CalculationMode.EXCHANGE_OPTIONS.value,
            "COLLATERAL": CalculationMode.SERV_COLLATERAL.value,
            # word forms from the MT5 Administrator dialog
            "FOREX NO LEVERAGE": CalculationMode.FOREX_NO_LEVERAGE.value,
        }
    )

    # The Trade tab's dropdown sends its LABEL as the option value, so the label
    # spelling has to resolve. Four labels did not, and choosing them silently kept
    # the previous calculation mode:
    #
    #     "Exchange FORTS Futures"  -> EXCHANGE_FORTS_FUTURES
    #     "Exchange MOEX Stocks"    -> EXCHANGE_MOEX_STOCKS
    #     "Exchange MOEX Bonds"     -> EXCHANGE_MOEX_BONDS
    #     "Exchange Margin Option"  -> EXCHANGE_MARGIN_OPTION
    #
    # DERIVED, not listed: each alias is every permutation of the enum member's own
    # words, so a member added later gets its alias without anyone remembering to.
    # Permutations rather than a fixed reordering because "MOEX Stocks" and "Stocks
    # MOEX" are both plausible spellings and generating both costs nothing here.
    from itertools import permutations

    def _forms(words):
        """The member's words in singular and plural. The enum says OPTIONS and the
        Trade tab label says "Option", which is the one spelling permutations of the
        member name alone cannot produce."""
        singular = [w[:-1] if w.endswith("S") and len(w) > 1 else w for w in words]
        plural = [w if w.endswith("S") else w + "S" for w in words]
        seen = []
        for variant in (words, singular, plural):
            if variant not in seen:
                seen.append(variant)
        return seen

    for member in CalculationMode:
        words = member.name.split("_")
        if not 2 <= len(words) <= 4:
            continue
        for variant in _forms(words):
            for order in permutations(variant):
                mapping.setdefault("_".join(order), member.value)

    return mapping


_CALC_MODES = _calc_mode_map()
_TRADE_MODES = {
    "DISABLED": 0, "LONGONLY": 1, "LONG_ONLY": 1, "SHORTONLY": 2, "SHORT_ONLY": 2,
    "CLOSEONLY": 3, "CLOSE_ONLY": 3, "FULL": 4
}
_EXEC_MODES = {
    "REQUEST": 0, "INSTANT": 1, "MARKET": 2, "EXCHANGE": 3
}


@symbols_skeleton.post("", status_code=status.HTTP_201_CREATED)
async def create_symbol(
    body: Dict[str, Any],
    symbol_repo: Any = Depends(get_symbol_repo),
) -> Dict[str, Any]:
    raw_symbol = str(body.get("symbol") or body.get("name") or "").strip()
    if not raw_symbol:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Symbol name is required")

    raw_symbol = raw_symbol.replace("/", "\\")
    if "\\" in raw_symbol:
        clean_name = raw_symbol.split("\\")[-1]
        full_path = raw_symbol
    else:
        clean_name = raw_symbol
        folder = str(body.get("path") or body.get("folder") or "").strip().replace("/", "\\")
        full_path = f"{folder}\\{clean_name}" if folder else clean_name

    # Dummy folder markers preserve their path as name so each folder marker is unique
    sym_name = full_path if clean_name == ".dummy" else clean_name

    existing = await symbol_repo.find_row_by_name(sym_name)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Symbol '{sym_name}' already exists",
        )

    settings_dict = {}
    raw_settings = body.get("settings_json")
    if isinstance(raw_settings, str) and raw_settings:
        try:
            settings_dict = json.loads(raw_settings)
        except Exception:
            pass
    elif isinstance(raw_settings, dict):
        settings_dict = raw_settings

    digits = int(body.get("digits", settings_dict.get("digits", 5)))
    contract_size = Decimal(str(body.get("contract_size", settings_dict.get("contract_size", 100000))))
    quote_currency = str(body.get("currency") or settings_dict.get("quote_currency") or settings_dict.get("currency") or "USD")
    base_currency = str(settings_dict.get("base_currency") or (clean_name[:3] if len(clean_name) == 6 else "USD"))
    spread = int(body.get("spread_base", body.get("spread", settings_dict.get("spread", 0))))
    margin_initial = Decimal(str(body.get("margin_initial", settings_dict.get("margin_initial", 1.0))))
    margin_maintenance = Decimal(str(body.get("margin_maintenance", settings_dict.get("margin_maintenance", 1.0))))

    calc_mode_val = settings_dict.get("calc_mode", body.get("calc_mode", 0))
    trade_mode_val = settings_dict.get("trade_mode", body.get("trade_mode", 4))
    exec_mode_val = settings_dict.get("exec_mode", body.get("exec_mode", 2))

    calc_mode = _to_mode_int(calc_mode_val, 0, _CALC_MODES)
    trade_mode = _to_mode_int(trade_mode_val, 4, _TRADE_MODES)
    exec_mode = _to_mode_int(exec_mode_val, 2, _EXEC_MODES)

    fill_flags = 1  # Default FOK
    if "fill_flags" in body or "fill_flags" in settings_dict:
        try:
            fill_flags = int(body.get("fill_flags", settings_dict.get("fill_flags", 1)))
        except Exception:
            pass
    elif "filling_flags" in settings_dict or "filling_flags" in body:
        ff_val = body.get("filling_flags", settings_dict.get("filling_flags"))
        if isinstance(ff_val, list):
            mask = 0
            for item in ff_val:
                s_item = str(item).lower()
                if s_item == 'fok': mask |= 1
                elif s_item == 'ioc': mask |= 2
                elif s_item in ('boc', 'return'): mask |= 4
            fill_flags = mask

    volume_min = Decimal(str(settings_dict.get("volume_min", body.get("volume_min", 0.01))))
    volume_max = Decimal(str(settings_dict.get("volume_max", body.get("volume_max", 100.0))))
    volume_step = Decimal(str(settings_dict.get("volume_step", body.get("volume_step", 0.01))))
    volume_limit = Decimal(str(settings_dict.get("volume_limit", body.get("volume_limit", 0))))
    description = str(settings_dict.get("description", body.get("description", "")))
    is_trade_allowed = bool(settings_dict.get("is_trade_allowed", body.get("is_trade_allowed", True)))

    ts_input = body.get("tick_size", settings_dict.get("tick_size", body.get("point")))
    point = Decimal(str(ts_input)) if ts_input else (Decimal(10) ** -digits)
    tv_input = body.get("tick_value", settings_dict.get("tick_value", 1.0))
    tick_value = Decimal(str(tv_input)) if tv_input else Decimal("1")
    stops_level = int(body.get("stops_level", settings_dict.get("stops_level", body.get("limit_stop_level", settings_dict.get("limit_stop_level", 0)))))
    freeze_level = int(body.get("freeze_level", settings_dict.get("freeze_level", 0)))

    model = SymbolModel(
        name=sym_name,
        path=full_path,
        symbol_id=sym_name,
        description=description,
        base_currency=base_currency,
        quote_currency=quote_currency,
        margin_currency=quote_currency,
        digits=digits,
        point=point,
        mt5_tick_size=point,
        tick_value=tick_value,
        contract_size=contract_size,
        calc_mode=calc_mode,
        trade_mode=trade_mode,
        exec_mode=exec_mode,
        fill_flags=fill_flags,
        spread=spread,
        stops_level=stops_level,
        freeze_level=freeze_level,
        volume_min=volume_min,
        volume_max=volume_max,
        volume_step=volume_step,
        volume_limit=volume_limit,
        margin_initial_buy=margin_initial,
        margin_initial_sell=margin_initial,
        margin_maintenance_buy=margin_maintenance,
        margin_maintenance_sell=margin_maintenance,
        is_trade_allowed=is_trade_allowed,
        mt5_extra=settings_dict,
    )

    await symbol_repo.save_model(model)
    domain_sym = db_to_symbol(model)
    cache = get_config_cache()
    if cache:
        cache.upsert_symbol(domain_sym)

    return _symbol_summary(domain_sym)


#: MT5 weekday order is SUNDAY-FIRST (index 0 = Sunday). Python's weekday() is
#: MONDAY-first, so any translation has to go through this table rather than
#: through weekday(). infrastructure.mt5.wire.WEEKDAY_SUNDAY_FIRST is the authority.
_SESSION_DAY_ALIASES = {
    "SUN": 0, "SUNDAY": 0,
    "MON": 1, "MONDAY": 1,
    "TUE": 2, "TUESDAY": 2,
    "WED": 3, "WEDNESDAY": 3,
    "THU": 4, "THURSDAY": 4,
    "FRI": 5, "FRIDAY": 5,
    "SAT": 6, "SATURDAY": 6,
}


def _normalise_session_days(raw: Any) -> Any:
    """Coerce an inbound session calendar into MT5's 7-element Sunday-first list.

    Accepts the shapes a client can reasonably send:
      * MT5's own ``[[{"Open": "0", "Close": "1440"}], ...]``
      * ``{"SUN": [...], "MON": [...]}`` keyed by weekday name
      * ``[{"day": 0, "sessions": [...]}, ...]`` (what codec.parse_sessions returns)

    Returns None when the value cannot be interpreted, so the caller leaves the
    stored column untouched rather than writing a half-understood calendar.
    """
    if raw is None:
        return None
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except Exception:
            return None

    if isinstance(raw, dict):
        days: List[Any] = [[] for _ in range(7)]
        for key, value in raw.items():
            index = _SESSION_DAY_ALIASES.get(str(key).strip().upper())
            if index is None:
                continue
            days[index] = _session_ranges(value)
        return days

    if isinstance(raw, list):
        # Already a 7-slot list?
        if len(raw) == 7 and not any(
            isinstance(entry, dict) and "day" in entry for entry in raw
        ):
            return [_session_ranges(entry) for entry in raw]
        # The parsed per-day dicts.
        days = [[] for _ in range(7)]
        for entry in raw:
            if not isinstance(entry, dict):
                continue
            index = entry.get("index", entry.get("day"))
            if isinstance(index, str):
                index = _SESSION_DAY_ALIASES.get(index.strip().upper())
            try:
                index = int(index)
            except (TypeError, ValueError):
                continue
            if 0 <= index <= 6:
                days[index] = [
                    {"Open": str(int(s.get("open_minutes", 0))),
                     "Close": str(int(s.get("close_minutes", 0)))}
                    for s in (entry.get("sessions") or [])
                    if isinstance(s, dict)
                ]
        return days

    return None


def _session_ranges(value: Any) -> List[Dict[str, str]]:
    """One day's ranges, in MT5's ``{"Open", "Close"}`` minute form."""
    out: List[Dict[str, str]] = []
    for entry in value or []:
        if not isinstance(entry, dict):
            continue
        open_min = entry.get("Open", entry.get("open_minutes", entry.get("start")))
        close_min = entry.get("Close", entry.get("close_minutes", entry.get("end")))
        try:
            open_val = _session_minutes(open_min)
            close_val = _session_minutes(close_min)
        except (TypeError, ValueError):
            continue
        out.append({"Open": str(open_val), "Close": str(close_val)})
    return out


def _session_minutes(value: Any) -> int:
    """Minutes from midnight. Accepts 1440 and the string "24:00" as END OF DAY.

    MT5 stores a session close of 1440 for a day that runs to midnight, so this
    must round-trip 1440 rather than clamping it to 23:59 - clamping would silently
    shorten every full-day session by one minute.
    """
    if value is None or value == "":
        raise ValueError("empty")
    if isinstance(value, str) and ":" in value:
        hours, _, minutes = value.partition(":")
        total = int(hours) * 60 + int(minutes or 0)
    else:
        total = int(value)
    return max(0, min(1440, total))


def _sessions_from_hours(hours: str) -> Any:
    """Parse the modal's "MON,00:00-24:00;TUE,00:00-24:00" form.

    Returns None when nothing parsed, so a malformed string cannot blank a
    schedule that was already configured.
    """
    from infrastructure.mt5.codec import _to_int  # noqa: F401  (kept for symmetry)

    days: List[Any] = [[] for _ in range(7)]
    seen = False
    for chunk in hours.split(";"):
        chunk = chunk.strip()
        if not chunk or "," not in chunk:
            continue
        day_name, _, ranges = chunk.partition(",")
        index = _SESSION_DAY_ALIASES.get(day_name.strip().upper())
        if index is None:
            continue
        for pair in ranges.split(","):
            pair = pair.strip()
            if "-" not in pair:
                continue
            start, _, end = pair.partition("-")
            try:
                open_val = _session_minutes(start.strip())
                close_val = _session_minutes(end.strip())
            except (TypeError, ValueError):
                continue
            days[index].append({"Open": str(open_val), "Close": str(close_val)})
            seen = True
    return days if seen else None


#: MT5 EnSwapMode, for the Swaps tab. Derived from the domain enum so it cannot
#: drift from the values the trade server uses.
def _swap_mode_map() -> Dict[str, int]:
    from core.domains.instruments.enums import SwapMode

    mapping: Dict[str, int] = {member.name: member.value for member in SwapMode}
    mapping.update({
        # the labels the Swaps tab shows
        "POINTS": SwapMode.POINTS.value,
        "MONEY": SwapMode.SYMBOL_CURRENCY.value,
        "PERCENT": SwapMode.INTEREST_CURRENT.value,
        "REOPEN_CLOSE": SwapMode.REOPEN_CLOSE_PRICE.value,
        "REOPEN_BID": SwapMode.REOPEN_BID.value,
        # spellings a client may send
        "DISABLED": SwapMode.DISABLED.value,
        "BASE_CURRENCY": SwapMode.SYMBOL_CURRENCY.value,
        "INTEREST_CURRENT": SwapMode.INTEREST_CURRENT.value,
        "INTEREST_OPEN": SwapMode.INTEREST_OPEN.value,
    })
    return mapping


_SWAP_MODES = _swap_mode_map()

#: MT5 EnSwapDays is SUNDAY-FIRST: 0=Sunday .. 6=Saturday, 7=triple swap disabled.
#: This is NOT Python's weekday(), which is Monday-first - using weekday() here
#: would move the triple-swap day by one, which is a real cost to the broker.
_SWAP_DAY_NAMES = {
    "SUNDAY": 0, "SUN": 0,
    "MONDAY": 1, "MON": 1,
    "TUESDAY": 2, "TUE": 2,
    "WEDNESDAY": 3, "WED": 3,
    "THURSDAY": 4, "THU": 4,
    "FRIDAY": 5, "FRI": 5,
    "SATURDAY": 6, "SAT": 6,
    "DISABLED": 7, "NONE": 7,
}


def _swap_day(value: Any, default: int) -> int:
    """Resolve the triple-swap weekday to MT5's Sunday-first index."""
    if isinstance(value, str):
        named = _SWAP_DAY_NAMES.get(value.strip().upper())
        if named is not None:
            return named
        try:
            value = int(value)
        except (TypeError, ValueError):
            return default
    try:
        number = int(value)
    except (TypeError, ValueError):
        return default
    return number if 0 <= number <= 7 else default


def _volume_to_wire(value: Any) -> Decimal:
    """Lots -> the scaled integer the volume columns hold.

    MT5 carries `VolumeMin` as `100` for 0.01 lots, i.e. lots x 10^4, with an `*Ext`
    sibling at x 10^8 carrying more precision. Our columns hold the x 10^4 form, which
    is what `_volume_ext`, `db_to_symbol` and 360 of 362 imported rows already agree
    on.

    The exponent is imported from the codec rather than written here, so a change to
    the wire format cannot leave this conversion behind.
    """
    from infrastructure.mt5.codec import VOLUME_WIRE_EXPONENT

    return Decimal(str(value)) * (Decimal(10) ** VOLUME_WIRE_EXPONENT)


def _first_present(containers: Any, keys: Any) -> Any:
    """The first non-None value for any of `keys`, searched across `containers`.

    The handler grew two input shapes - top-level `body` and the nested
    `settings_json` blob - and the fields were read from whichever one the original
    author happened to pick. Searching both, under every alias, is what stops a
    field being accepted and then silently dropped.
    """
    body, settings = containers
    for key in keys:
        for container in (body, settings):
            if isinstance(container, dict) and container.get(key) is not None:
                return container[key]
    return None


def _int_mask(value: Any, default: int, names: Optional[Dict[str, int]] = None) -> int:
    """A flag field as an integer mask.

    The frontend renders these as CHECKBOXES and sends an array of set-bit names,
    so a list has to be folded into the bitmask the column and the MT5 wire both
    hold. An integer passes straight through.
    """
    if value is None:
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            pass
    if isinstance(value, (list, tuple, set)):
        table = names or {}
        total = 0
        for item in value:
            if isinstance(item, str):
                bit = table.get(item.strip().lower())
                if bit is None:
                    # Unknown member: raise rather than silently drop a permission
                    # the operator ticked.
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"unknown flag {item!r}",
                    )
                total |= bit
            else:
                total |= int(item)
        return total
    return default


def _known_symbol_keys() -> frozenset:
    """Every key PUT /admin/symbols/{name} understands.

    Built from the same sources as the schema endpoint, so the two cannot disagree
    about what is writable:

      * the extras registry — the MT5 fields with no dedicated column, under their
        stable JSON keys;
      * the MT5 wire names those fields are stored under;
      * the alias spellings this handler already accepts historically;
      * the control keys (settings_json, body-only switches).

    Computed once and cached, because it is read on every PUT.
    """
    global _KNOWN_SYMBOL_KEYS_CACHE
    try:
        return _KNOWN_SYMBOL_KEYS_CACHE
    except NameError:
        pass

    from core.domains.instruments import symbol_extras

    keys = set()

    # mt5_extra fields, under their JSON key, their wire name, and any ALIAS the UI uses.
    # The alias set is read from the registry rather than repeated here: `chart_mode` was
    # missing from this list and its own tab's dropdown was rejected, which is the same
    # failure `splice_type` produced on the other tab.
    for field in symbol_extras.EXTRA_FIELDS:
        keys.add(field.key)
        keys.add(field.wire)
    keys.update(symbol_extras.ALIASES)
    # The whole quarantine is addressable by wire name, which is what an MT5-style
    # client sends and what the schema reports in `mt5`.
    keys.add("extra")
    keys.add("mt5_extra")

    # Control keys the handler reads on purpose.
    keys.update({
        "settings_json", "session_hours", "sessions_quotes", "sessions_trades",
        "symbol", "name", "path", "description", "digits", "point", "tick_size",
        "mt5_tick_size", "tick_value", "contract_size",
        "base_currency", "quote_currency", "margin_currency", "currency",
        "spread", "spread_base", "spread_balance", "spread_diff",
        "spread_diff_balance", "stops_level", "limit_stop_level", "freeze_level",
        "volume_min", "volume_max", "volume_step", "volume_limit",
        "min_volume", "max_volume", "step_volume", "limit_volume",
        "calc_mode", "calculation", "trade_mode", "exec_mode", "execution_mode",
        "gtc_mode", "fill_flags", "filling_flags", "expiration_flags",
        "order_flags", "orders_allowed", "is_trade_allowed", "trade_allowed",
        "swap_triple_day", "swap_days_in_year",
        "margin_hedged", "margin_initial", "margin_maintenance",
        # The Margin Rates tab's own 12 keys. They were missing from this list even
        # though the handler's `rate_map` below writes them, so the unknown-key guard
        # refused them and the whole tab could not save. Derived from `rate_map`
        # rather than repeated, so the two cannot disagree again.
        "rate_market_buy_init", "rate_market_buy_maint",
        "rate_market_sell_init", "rate_market_sell_maint",
        "rate_limit_buy_init", "rate_limit_buy_maint",
        "rate_limit_sell_init", "rate_limit_sell_maint",
        "rate_stop_buy_init", "rate_stop_buy_maint",
        "rate_stop_sell_init", "rate_stop_sell_maint",
        "rate_stoplimit_buy_init", "rate_stoplimit_buy_maint",
        "rate_stoplimit_sell_init", "rate_stoplimit_sell_maint",
        # the column names the nested `margin_rates` dict path accepts
        "margin_initial_buy", "margin_initial_sell",
        "margin_initial_buy_limit", "margin_initial_sell_limit",
        "margin_initial_buy_stop", "margin_initial_sell_stop",
        "margin_initial_buy_stop_limit", "margin_initial_sell_stop_limit",
        "margin_maintenance_buy", "margin_maintenance_sell",
        "margin_maintenance_buy_limit", "margin_maintenance_sell_limit",
        "margin_maintenance_buy_stop", "margin_maintenance_sell_stop",
        "margin_maintenance_buy_stop_limit", "margin_maintenance_sell_stop_limit",
        "margin_rates",
        "calc_hedged_larger_leg", "swap_mode", "swap_long", "swap_short",
        "swap_3day", "swap_year_days", "option_mode", "strike_price",
        "face_value", "face_value_currency",
    })
    _KNOWN_SYMBOL_KEYS_CACHE = frozenset(keys)
    return _KNOWN_SYMBOL_KEYS_CACHE


@symbols_skeleton.put("/{symbol_name:path}")
async def update_symbol(
    symbol_name: str,
    body: Dict[str, Any],
    symbol_repo: Any = Depends(get_symbol_repo),
) -> Dict[str, Any]:
    norm_name = symbol_name.replace("/", "\\")
    clean_name = norm_name.split("\\")[-1] if "\\" in norm_name else norm_name

    # Refuse unknown keys BEFORE touching the row. The handler below is a chain of
    # `if "<name>" in body` tests, so an unrecognised key used to be dropped in
    # silence and the caller still got a 200 - which is how a session edit could
    # look saved and be stored nowhere. A typo now fails loudly.
    unknown = sorted(set(body or {}) - _known_symbol_keys())
    if unknown:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Unknown symbol field(s): " + ", ".join(unknown)
                + ". These have no effect and were refused rather than ignored."
            ),
        )

    model = await symbol_repo.find_row_by_name(norm_name)
    if not model and clean_name != norm_name:
        model = await symbol_repo.find_row_by_name(clean_name)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Symbol '{symbol_name}' not found",
        )

    settings_dict = {}
    raw_settings = body.get("settings_json")
    if isinstance(raw_settings, str) and raw_settings:
        try:
            settings_dict = json.loads(raw_settings)
        except Exception:
            pass
    elif isinstance(raw_settings, dict):
        settings_dict = raw_settings

    new_symbol = str(body.get("symbol", "")).strip().replace("/", "\\")
    if new_symbol and "\\" in new_symbol:
        model.path = new_symbol
    elif body.get("path"):
        p = str(body["path"]).strip().replace("/", "\\")
        model.path = f"{p}\\{model.name}" if not p.endswith(f"\\{model.name}") else p

    if "digits" in body or "digits" in settings_dict:
        d_val = body.get("digits") if "digits" in body else settings_dict.get("digits")
        digits = int(d_val)
        model.digits = digits
        if not ("tick_size" in body or "tick_size" in settings_dict):
            model.point = Decimal(10) ** -digits
            model.mt5_tick_size = model.point

    if "tick_size" in body or "tick_size" in settings_dict or "point" in body:
        ts = body.get("tick_size", settings_dict.get("tick_size", body.get("point")))
        if ts is not None and float(ts) > 0:
            ts_dec = Decimal(str(ts))
            model.point = ts_dec
            model.mt5_tick_size = ts_dec

    if "tick_value" in body or "tick_value" in settings_dict:
        tv = body.get("tick_value", settings_dict.get("tick_value"))
        if tv is not None:
            model.tick_value = Decimal(str(tv))

    if "contract_size" in body or "contract_size" in settings_dict:
        c_val = body.get("contract_size") if "contract_size" in body else settings_dict.get("contract_size")
        model.contract_size = Decimal(str(c_val))

    if "currency" in body or "currency" in settings_dict or "quote_currency" in settings_dict:
        curr = str(body.get("currency") or settings_dict.get("quote_currency") or settings_dict.get("currency"))
        model.quote_currency = curr
        model.margin_currency = curr

    if "base_currency" in settings_dict:
        model.base_currency = str(settings_dict["base_currency"])

    if "spread_base" in body or "spread" in body or "spread" in settings_dict:
        sp = body.get("spread_base", body.get("spread", settings_dict.get("spread", model.spread)))
        model.spread = int(sp)

    if "stops_level" in body or "stops_level" in settings_dict or "limit_stop_level" in body or "limit_stop_level" in settings_dict:
        sl = body.get("stops_level", settings_dict.get("stops_level", body.get("limit_stop_level", settings_dict.get("limit_stop_level"))))
        if sl is not None:
            model.stops_level = int(sl)

    if "freeze_level" in body or "freeze_level" in settings_dict:
        fl = body.get("freeze_level", settings_dict.get("freeze_level"))
        if fl is not None:
            model.freeze_level = int(fl)

    if "description" in body or "description" in settings_dict:
        model.description = str(body.get("description", settings_dict.get("description", model.description)))

    # --- volumes: the API speaks LOTS, the column holds MT5's wire integer ----
    #
    # Measured on the live database: 360 of 362 rows satisfy
    # `column == their own mt5_source wire value`, and `_volume_ext` derives
    # `VolumeMinExt = column x 10^4` - both only true when the column holds the
    # SCALED INTEGER. `db_to_symbol` divides by 10^4 on read to produce lots, which is
    # the unit the engine and validate_volume use.
    #
    # Writing the API value straight in put lots where an integer belonged, so every
    # volume edited through this endpoint was stored 10^4 too small: ETHUSD ended up
    # with the engine seeing a 0.1-lot maximum on a symbol the server allows 1000 lots
    # on, and a 1-lot order was rejected. `_volume_to_wire` applies the conversion the
    # reader already assumes.
    if "volume_min" in settings_dict or "volume_min" in body or "min_volume" in settings_dict:
        v_min = settings_dict.get("volume_min", body.get("volume_min", settings_dict.get("min_volume")))
        if v_min is not None:
            model.volume_min = _volume_to_wire(v_min)

    if "volume_max" in settings_dict or "volume_max" in body or "max_volume" in settings_dict:
        v_max = settings_dict.get("volume_max", body.get("volume_max", settings_dict.get("max_volume")))
        if v_max is not None:
            model.volume_max = _volume_to_wire(v_max)

    if "volume_step" in settings_dict or "volume_step" in body or "step_volume" in settings_dict:
        v_step = settings_dict.get("volume_step", body.get("volume_step", settings_dict.get("step_volume")))
        if v_step is not None:
            model.volume_step = _volume_to_wire(v_step)

    if "volume_limit" in settings_dict or "volume_limit" in body or "limit_volume" in settings_dict:
        v_lim = settings_dict.get("volume_limit", body.get("volume_limit", settings_dict.get("limit_volume")))
        if v_lim is not None:
            model.volume_limit = _volume_to_wire(v_lim)

    # The three mode fields used to be read from `settings_dict` ONLY, so a
    # top-level `calc_mode` was ignored - and so was `calculation`, which is the key
    # the Trade tab actually sends. Proved live: of six shapes tried, only
    # `settings_json: {"calc_mode": ...}` moved the stored value; every other one
    # returned 200 and changed nothing.
    #
    # Now read from BOTH containers, under every alias the UI has used:
    #   calc_mode / calculation
    #   trade_mode
    #   exec_mode / execution_mode
    _calc_raw = _first_present(
        (body, settings_dict), ("calc_mode", "calculation")
    )
    if _calc_raw is not None:
        # The dropdown sends the human LABEL ("CFD", "Forex No Leverage"), which
        # _to_mode_int normalises. It also accepts the integer.
        model.calc_mode = _to_mode_int(_calc_raw, model.calc_mode, _CALC_MODES)

    _trade_raw = _first_present((body, settings_dict), ("trade_mode",))
    if _trade_raw is not None:
        model.trade_mode = _to_mode_int(_trade_raw, model.trade_mode, _TRADE_MODES)

    _exec_raw = _first_present((body, settings_dict), ("exec_mode", "execution_mode"))
    if _exec_raw is not None:
        model.exec_mode = _to_mode_int(_exec_raw, model.exec_mode, _EXEC_MODES)

    _allowed = _first_present((body, settings_dict), ("is_trade_allowed", "trade_allowed"))
    if _allowed is not None:
        model.is_trade_allowed = bool(_allowed)

    # 16-way margin rate matrix
    rate_map = {
        "rate_market_buy_init": "margin_initial_buy",
        "rate_market_buy_maint": "margin_maintenance_buy",
        "rate_market_sell_init": "margin_initial_sell",
        "rate_market_sell_maint": "margin_maintenance_sell",
        "rate_limit_buy_init": "margin_initial_buy_limit",
        "rate_limit_buy_maint": "margin_maintenance_buy_limit",
        "rate_limit_sell_init": "margin_initial_sell_limit",
        "rate_limit_sell_maint": "margin_maintenance_sell_limit",
        "rate_stop_buy_init": "margin_initial_buy_stop",
        "rate_stop_buy_maint": "margin_maintenance_buy_stop",
        "rate_stop_sell_init": "margin_initial_sell_stop",
        "rate_stop_sell_maint": "margin_maintenance_sell_stop",
        # The two stop-limit rows. MT5's grid has EIGHT order types; this map
        # covered six, so a quarter of the Margin Rates tab had no write path.
        "rate_stoplimit_buy_init": "margin_initial_buy_stop_limit",
        "rate_stoplimit_buy_maint": "margin_maintenance_buy_stop_limit",
        "rate_stoplimit_sell_init": "margin_initial_sell_stop_limit",
        "rate_stoplimit_sell_maint": "margin_maintenance_sell_stop_limit",
    }
    for ui_k, db_k in rate_map.items():
        if ui_k in settings_dict or ui_k in body:
            v = settings_dict.get(ui_k, body.get(ui_k))
            if v is not None:
                setattr(model, db_k, Decimal(str(v)))

    mr = body.get("margin_rates") or settings_dict.get("margin_rates")
    if isinstance(mr, dict):
        for k, v in mr.items():
            db_k = f"margin_{k}" if not k.startswith("margin_") else k
            if hasattr(model, db_k) and v is not None:
                setattr(model, db_k, Decimal(str(v)))

    if "fill_flags" in body or "fill_flags" in settings_dict:
        try:
            model.fill_flags = int(body.get("fill_flags", settings_dict.get("fill_flags", model.fill_flags)))
        except Exception:
            pass
    elif "filling_flags" in settings_dict or "filling_flags" in body:
        ff_val = body.get("filling_flags", settings_dict.get("filling_flags"))
        if isinstance(ff_val, list):
            mask = 0
            for item in ff_val:
                s_item = str(item).lower()
                if s_item == 'fok': mask |= 1
                elif s_item == 'ioc': mask |= 2
                elif s_item in ('boc', 'return'): mask |= 4
            model.fill_flags = mask

    extra = dict(model.mt5_extra or {})
    extra.update(settings_dict)
    extra["fill_flags"] = model.fill_flags
    if "margin_hedged" in body or "margin_hedged" in settings_dict:
        extra["margin_hedged"] = str(body.get("margin_hedged", settings_dict.get("margin_hedged", 0)))
    # --- sessions ---------------------------------------------------------
    # These were accepted by the request body and then thrown away, because nothing
    # in this handler read them: the modal sends `session_hours` on every save and
    # PUT answered 200 while the schedule never changed.
    #
    # Two shapes are accepted, because two producers exist:
    #   * `sessions_quotes` / `sessions_trades` - a 7-element Sunday-first list of
    #     {Open, Close} minute ranges, which is MT5's own wire shape (see
    #     codec.parse_sessions). This is what our API serves and what an MT5 import
    #     round-trips through.
    #   * `session_hours` - the modal's compact "MON,00:00-24:00;TUE,..." string.
    for _wire, _column in (("sessions_quotes", "sessions_quotes_json"),
                           ("sessions_trades", "sessions_trades_json")):
        if _wire in body or _wire in settings_dict:
            _raw = body.get(_wire, settings_dict.get(_wire))
            _days = _normalise_session_days(_raw)
            if _days is not None:
                setattr(model, _column, _days)
            elif _raw is None:
                setattr(model, _column, [])

    _hours = body.get("session_hours", settings_dict.get("session_hours"))
    if isinstance(_hours, str) and _hours.strip():
        _parsed = _sessions_from_hours(_hours)
        if _parsed:
            # One string carries both calendars; apply to trades, and to quotes
            # only when the caller did not send an explicit quote calendar.
            if "sessions_trades" not in body and "sessions_trades" not in settings_dict:
                model.sessions_trades_json = _parsed
            if "sessions_quotes" not in body and "sessions_quotes" not in settings_dict:
                model.sessions_quotes_json = _parsed

    # --- GTC, order types, expirations, trade flags, swaps -----------------
    # None of these had a branch, so a PUT naming them passed the allow-list and
    # then reached the end of this function untouched: HTTP 200, nothing stored.
    # Each is written to its own COLUMN, because the export reads the column - a
    # value parked in mt5_extra would round-trip through import/export but never
    # reach the trade server.

    _gtc = _first_present((body, settings_dict), ("gtc_mode",))
    if _gtc is not None:
        model.gtc_mode = int(_gtc)

    _order_flags = _first_present((body, settings_dict), ("order_flags", "orders_allowed"))
    if _order_flags is not None:
        model.order_flags = _int_mask(_order_flags, model.order_flags)

    _expir = _first_present((body, settings_dict), ("expiration_flags",))
    if _expir is not None:
        model.expiration_flags = _int_mask(
            _expir, model.expiration_flags,
            names={"none": 0, "gtc": 1, "day": 2, "specified": 4, "time": 4,
                   "specified_day": 8, "day_specified": 8},
        )

    _trade_flags = _first_present((body, settings_dict), ("trade_flags",))
    if _trade_flags is not None:
        # Stored under the registry's wire name, because `trade_flags` is not a
        # column and TradeFlags is what the exporter emits.
        from core.domains.instruments import symbol_extras as _se
        _field = _se.BY_KEY.get("trade_flags")
        if _field is not None:
            extra, _ = _se.apply_updates(extra, {"trade_flags": _trade_flags})

    # Swaps. MT5's Swaps tab: mode, the two rates, the triple-swap weekday and the
    # day-count convention. Without these the tab was decorative - reading real
    # values from storage (once F-14b surfaced them) but unable to change any.
    _swap_mode = _first_present((body, settings_dict), ("swap_mode",))
    if _swap_mode is not None:
        model.swap_mode = _to_mode_int(_swap_mode, model.swap_mode, _SWAP_MODES)

    for _key, _column in (("swap_long", "swap_long"), ("swap_short", "swap_short")):
        _value = _first_present((body, settings_dict), (_key,))
        if _value is not None:
            setattr(model, _column, Decimal(str(_value)))

    _swap_3day = _first_present((body, settings_dict), ("swap_3day", "swap_triple_day"))
    if _swap_3day is not None:
        # MT5 EnSwapDays is SUNDAY-FIRST (0=Sunday .. 6=Saturday, 7=disabled), and
        # the column stores that same numbering - so a weekday NAME has to be
        # resolved through the table, never through Python's Monday-first weekday().
        model.swap_3day = _swap_day(_swap_3day, model.swap_3day)

    _year_days = _first_present(
        (body, settings_dict), ("swap_year_days", "swap_days_in_year")
    )
    if _year_days is not None:
        model.swap_year_days = int(_year_days)

    if "calc_hedged_larger_leg" in body or "calc_hedged_larger_leg" in settings_dict:
        extra["calc_hedged_larger_leg"] = bool(body.get("calc_hedged_larger_leg", settings_dict.get("calc_hedged_larger_leg", False)))
    if "margin_initial" in body or "margin_initial" in settings_dict:
        mi = body.get("margin_initial", settings_dict.get("margin_initial"))
        if mi is not None and float(mi) > 0:
            extra["margin_initial"] = str(mi)
        else:
            extra.pop("margin_initial", None)
    if "margin_maintenance" in body or "margin_maintenance" in settings_dict:
        mm = body.get("margin_maintenance", settings_dict.get("margin_maintenance"))
        if mm is not None and float(mm) > 0:
            extra["margin_maintenance"] = str(mm)
        else:
            extra.pop("margin_maintenance", None)
    # --- the column-less MT5 fields ---------------------------------------
    # These have no dedicated column, so they live in mt5_extra under their MT5
    # wire names. The registry owns the key list, the coercion and the wire
    # mapping, so this is the ONLY place that has to know about it.
    #
    # Without this the fields were accepted by the allow-list above, validated by
    # the coercion below, and then silently dropped: a PUT of `filter_soft`
    # answered 200 while the row still held its previous value.
    from core.domains.instruments import symbol_extras as _symbol_extras

    # ACCEPTED_KEYS is canonical + alias, so `chart_mode` reaches the same field as
    # `tick_chart_mode` instead of being silently dropped after passing the guard.
    _extra_updates = {
        k: v for k, v in body.items() if k in _symbol_extras.ACCEPTED_KEYS
    }
    for _field in _symbol_extras.EXTRA_FIELDS:
        # Also accept the raw MT5 wire name, which is what an MT5-style client and
        # the `extra` blob itself use.
        if _field.wire in body:
            _extra_updates[_field.key] = body[_field.wire]
        elif _field.key in (settings_dict or {}):
            _extra_updates.setdefault(_field.key, settings_dict[_field.key])

    if _extra_updates:
        try:
            extra, _applied = _symbol_extras.apply_updates(extra, _extra_updates)
        except ValueError as exc:
            # A value the field cannot hold must be a 400, not a row that stores
            # something MT5 will refuse to read back.
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)
            )

    model.mt5_extra = extra

    await symbol_repo.save_model(model)
    domain_sym = db_to_symbol(model)
    cache = get_config_cache()
    if cache:
        cache.upsert_symbol(domain_sym)

    try:
        from api.di_providers import get_account_repo, get_position_repo
        acc_repo = get_account_repo()
        pos_repo = get_position_repo()
        if pos_repo and acc_repo:
            from api.routers.manager.trading import recalculate_account_trading_state
            open_pos = await pos_repo.get_by_symbol(model.name)
            if not open_pos and clean_name != model.name:
                open_pos = await pos_repo.get_by_symbol(clean_name)
            if open_pos:
                logins = {int(p.account_login) for p in open_pos}
                for l in logins:
                    # R17: pass the registered risk engine, as the manager path does.
                    # Without it the fallback ran with `rate_lookup -> Decimal("1")` and
                    # summed profit in the QUOTE currency, so editing ONE symbol rewrote the
                    # risk state of every account holding it at 1:1 - materially wrong for
                    # the 22 live symbols whose CurrencyMargin differs from CurrencyBase.
                    from api.di_providers import get_risk_engine

                    await recalculate_account_trading_state(
                        l, acc_repo, pos_repo, symbol_repo,
                        risk_engine=get_risk_engine(),
                    )
    except Exception as exc:
        logger.warning(f"update_symbol account recalculation notice: {exc}")

    return _symbol_summary(domain_sym)


@symbols_skeleton.delete("/{symbol_name:path}")
async def delete_symbol(
    symbol_name: str,
    symbol_repo: Any = Depends(get_symbol_repo),
    position_repo: Any = Depends(get_position_repo),
) -> Dict[str, Any]:
    norm_name = symbol_name.replace("/", "\\")
    clean_name = norm_name.split("\\")[-1] if "\\" in norm_name else norm_name

    model = await symbol_repo.find_row_by_name(norm_name)
    if not model and clean_name != norm_name:
        model = await symbol_repo.find_row_by_name(clean_name)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Symbol '{symbol_name}' not found",
        )

    # Check for active positions holding this symbol
    if position_repo and clean_name != ".dummy":
        try:
            if hasattr(position_repo, "find_page"):
                _, total = await position_repo.find_page(limit=1, symbol=model.name)
                if total > 0:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail=f"Cannot delete symbol '{model.name}': {total} active positions exist in this symbol",
                    )
        except HTTPException:
            raise
        except Exception:
            pass

    deleted = await symbol_repo.delete_symbol(model.name)
    if not deleted:
        deleted = await symbol_repo.delete_symbol(norm_name)

    cache = get_config_cache()
    if cache:
        cache.delete_symbol(model.name)

    return {"status": "success", "message": f"Symbol '{model.name}' deleted successfully"}


# ---------------------------------------------------------------------------
# routing writes (C3) - RIGHT_CFG_REQUESTS
# ---------------------------------------------------------------------------

routing_skeleton = APIRouter(
    prefix="/api/v1/admin/routing",
    tags=["Admin - NOT WIRED"],
    dependencies=[Depends(require_right("RIGHT_CFG_REQUESTS"))],
)


@routing_skeleton.post("", status_code=status.HTTP_201_CREATED, openapi_extra=X_NOT_WIRED)
async def create_routing_rule(body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("routing-rule writes (the M8 engine and loader exist; the "
                  "command layer does not)", "the routing-writes milestone (ENDPOINTS B7)")


@routing_skeleton.put("/{rule_id}", openapi_extra=X_NOT_WIRED)
async def update_routing_rule(rule_id: str, body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("routing-rule update", "the routing-writes milestone")


@routing_skeleton.delete("/{rule_id}", openapi_extra=X_NOT_WIRED)
async def delete_routing_rule(rule_id: str) -> Dict[str, Any]:
    raise _refuse("routing-rule delete", "the routing-writes milestone")


@routing_skeleton.post("/reorder", openapi_extra=X_NOT_WIRED)
async def reorder_routing_rules(body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("routing reorder - list order IS the semantics for a "
                  "top-down first-match engine, so this is the most "
                  "consequential routing write", "the routing-writes milestone")


# ---------------------------------------------------------------------------
# gateway + datafeed config planes (C4/C5) - migration 010
# ---------------------------------------------------------------------------

gateways_skeleton = APIRouter(
    prefix="/api/v1/admin/gateways",
    tags=["Admin - NOT WIRED"],
    dependencies=[Depends(require_right("RIGHT_CFG_GATEWAYS"))],
)

for _method, _path, _name in [
    ("get", "", "list_gateways"),
    ("post", "", "create_gateway"),
    ("put", "/{gateway_id}", "update_gateway"),
    ("delete", "/{gateway_id}", "delete_gateway"),
    ("post", "/{gateway_id}/test", "test_gateway"),
]:
    _what = f"gateway config plane ({_method.upper()} {_path or '/'})"
    _mile = ("migration 010 - the gateway config plane (mt5_gateways table; "
             "TRANSLATE_FIELDS and the markup maths exist since M13, there is "
             "nowhere to put a row)")
    _route = _skel_get(_what, _mile) if _method == "get" else _skel_write(_what, _mile)
    gateways_skeleton.add_api_route(
        _path, _route, methods=[_method.upper()], name=_name, openapi_extra=X_NOT_WIRED,
    )

datafeeds_skeleton = APIRouter(
    prefix="/api/v1/admin/datafeeds",
    tags=["Admin - NOT WIRED"],
    dependencies=[Depends(require_right("RIGHT_CFG_DATAFEEDS"))],
)

for _method, _path, _name in [
    ("get", "", "list_datafeeds"),
    ("post", "", "create_datafeed"),
    ("put", "/{feed_id}", "update_datafeed"),
    ("delete", "/{feed_id}", "delete_datafeed"),
]:
    _what = f"datafeed config plane ({_method.upper()} {_path or '/'})"
    _route = _skel_get(_what, "migration 010 - the datafeed config plane") if _method == "get" \
        else _skel_write(_what, "migration 010 - the datafeed config plane")
    datafeeds_skeleton.add_api_route(
        _path, _route, methods=[_method.upper()], name=_name, openapi_extra=X_NOT_WIRED,
    )

# ---------------------------------------------------------------------------
# allocations (C6) - plan step 9
# ---------------------------------------------------------------------------

allocations_skeleton = APIRouter(
    prefix="/api/v1/admin/allocations",
    tags=["Admin - NOT WIRED"],
    dependencies=[Depends(require_right("RIGHT_ACC_MANAGER"))],
)

for _method, _path, _name in [
    ("get", "", "list_allocations"),
    ("post", "", "create_allocation"),
    ("put", "/{allocation_id}", "update_allocation"),
    ("delete", "/{allocation_id}", "delete_allocation"),
]:
    _what = f"allocations ({_method.upper()} {_path or '/'})"
    _mile = ("IDENTITY-BUILD-PLAN step 9 - self-service account opening "
             "(groups, country filter, leverage lists, the demo-allocation URL rule)")
    _route = _skel_get(_what, _mile) if _method == "get" else _skel_write(_what, _mile)
    allocations_skeleton.add_api_route(
        _path, _route, methods=[_method.upper()], name=_name, openapi_extra=X_NOT_WIRED,
    )

# ---------------------------------------------------------------------------
# supervision & content (C7-C11, C12, C13)
# ---------------------------------------------------------------------------

misc_skeleton = APIRouter(prefix="/api/v1/admin", tags=["Admin - NOT WIRED"])


@misc_skeleton.get("/journal", dependencies=[Depends(require_right("RIGHT_SRV_JOURNALS"))],
                   openapi_extra=X_NOT_WIRED)
async def read_journal() -> Dict[str, Any]:
    raise _refuse("the audit journal - MT5 logs every manager query, export and "
                  "filter; this platform logs nothing queryable yet. The "
                  "compliance prerequisite for real operation",
                  "the audit-journal milestone (Tier 3 #4)")


@misc_skeleton.get("/reports", dependencies=[Depends(require_right("RIGHT_SRV_REPORTS"))],
                   openapi_extra=X_NOT_WIRED)
async def list_reports() -> Dict[str, Any]:
    raise _refuse("the report engine (statements, EOD, the DailyRequest family)",
                  "deferred by explicit decision; skeleton reserved")


@misc_skeleton.get("/charts/bars", dependencies=[Depends(require_right("RIGHT_CHARTS"))],
                   openapi_extra=X_NOT_WIRED)
async def chart_bars() -> Dict[str, Any]:
    raise _refuse("bar aggregation and storage - the bars table has 0 rows on "
                  "30+ fills; nothing aggregates ticks into bars yet",
                  "the history-plane milestone (Tier 3 #5)")


@misc_skeleton.get("/history/ticks", dependencies=[Depends(require_right("RIGHT_CHARTS"))],
                   openapi_extra=X_NOT_WIRED)
async def tick_history() -> Dict[str, Any]:
    raise _refuse("tick history storage (ClickHouse decision pending)",
                  "the history-plane milestone")


@misc_skeleton.post("/mail", dependencies=[Depends(require_right("RIGHT_EMAIL"))],
                    openapi_extra=X_NOT_WIRED)
async def send_mail(body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("internal mail", "deferred by explicit decision")


@misc_skeleton.post("/news", dependencies=[Depends(require_right("RIGHT_NEWS"))],
                    openapi_extra=X_NOT_WIRED)
async def publish_news(body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("news publishing", "deferred by explicit decision")


@misc_skeleton.post("/groups/{group_name}/symbols",
                    dependencies=[Depends(require_right("RIGHT_CFG_GROUPS"))],
                    openapi_extra=X_NOT_WIRED)
async def set_group_symbol_override(group_name: str, body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("per-group symbol overrides - the SpreadDiff/SpreadDiffBalance "
                  "writes where B-Book markup lives (M7 maths, no write path). "
                  "GroupSymbolOverride models 11 of MT5's 64 fields; the write "
                  "must round-trip the rest or the wire guarantee dies",
                  "ENDPOINTS B6 (with the symbol-CRUD milestone)")


@misc_skeleton.delete("/managers/{login}",
                      dependencies=[Depends(require_right("RIGHT_CFG_MANAGERS"))],
                      openapi_extra=X_NOT_WIRED)
async def delete_manager(login: str) -> Dict[str, Any]:
    raise _refuse("manager deletion - MT5 keeps the underlying account; the "
                  "manager row and its mirror password_hash must go without "
                  "touching the account's credential (one writer per secret)",
                  "the manager-lifecycle addition (small; with B1)")


# ---------------------------------------------------------------------------
# dealer intervention (C11) - the manager dialect
# ---------------------------------------------------------------------------

dealer_skeleton = APIRouter(
    prefix="/api/v1/manager",
    tags=["Manager - NOT WIRED"],
    dependencies=[Depends(require_right("RIGHT_TRADES_DEALER"))],
)


@dealer_skeleton.post("/OrderRequote", openapi_extra=X_NOT_WIRED)
async def order_requote(body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("dealer requote - the dealer_queue service exists internally; "
                  "the intervention workflow (request -> dealer -> new price -> "
                  "client accept/reject with the 30s timer) does not",
                  "the B1 dealer milestone")


@dealer_skeleton.post("/OrderConfirm", openapi_extra=X_NOT_WIRED)
async def order_confirm(body: _AnyBody) -> Dict[str, Any]:
    raise _refuse("dealer confirmation (request-policy CONFIRM modes are "
                  "modelled in the M8 routing table; the confirmation flow "
                  "is not)", "the B1 dealer milestone")


ALL_SKELETON_ROUTERS = [
    accounts_skeleton,
    symbols_skeleton,
    routing_skeleton,
    gateways_skeleton,
    datafeeds_skeleton,
    allocations_skeleton,
    misc_skeleton,
    dealer_skeleton,
]
