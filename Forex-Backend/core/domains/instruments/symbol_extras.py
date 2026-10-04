"""Symbol fields whose authoritative value lives in ``mt5_extra``, not a column.

WHY THIS MODULE EXISTS
----------------------
A SymbolModel row stores MT5's 121 symbol fields in three places:

1. **real columns** - the ~56 fields the domain models (`digits`, `spread`,
   `stops_level`, ...). Reading and writing these is already handled by
   ``symbol_to_db`` / ``db_to_symbol``.
2. **``mt5_source``** - the complete original wire record, kept so an export stays
   byte-identical. This is the *baseline*.
3. **``mt5_extra``** - MT5 fields with no domain attribute.

The trap this module exists to close: ``symbol_mt5_record`` overlays the
domain-owned wire keys onto the baseline, and only those in
``_SYMBOL_OWNED_WIRE_KEYS`` survive that overlay. Every other field keeps its
*imported* value. So a field written to ``mt5_extra`` - which is where a symbol
editor must write, since these fields have no column - would be **silently masked
by the stale baseline on export**. An operator edits the tick filtration, the
Admin API reports the new value, and the next export to MT5 ships the old one.

FIELDS
------
Everything here is a field MT5 documents on the symbol tabs but our domain does
not model. The wire name is exact (it is the ``mt5_source`` key); the JSON key is
the name the Admin API exposes and accepts.

These were previously carried in ``mt5_extra`` only as raw wire names, which is
why the symbol editor could not show them: the API returned ``{}`` and the UI
read a stale lowercase template instead.

Adding a field here does three things at once, which is the point of keeping one
list:

* ``symbol_mt5_record`` overlays it on export, so an edit reaches MT5;
* the Admin API surfaces it under its JSON key;
* a PUT accepts it, and anything NOT in this list is refused rather than ignored.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any, Dict, NamedTuple, Optional, Tuple

# Field kinds, matching infrastructure.mt5.fieldmap's wire vocabulary.
STR = "str"
DEC = "dec"
INT = "int"
FLAGS = "flags"
#: An ENUMERATED field the wire carries as an integer. Unlike INT, it also accepts the
#: LABEL the UI sends ('none', 'last', 'adjusted') and the MT5 member name, and stores the
#: integer. Every dropdown in the symbol editor sends its label, so an enum field typed as
#: INT rejects the UI's own value - which is exactly what happened to `splice_type`.
ENUM = "enum"


class ExtraField(NamedTuple):
    """One MT5 symbol field that lives in ``mt5_extra``.

    Attributes:
        key:    the JSON key the Admin API exposes and accepts.
        wire:   the exact MT5 wire name - the key inside ``mt5_source``/``mt5_extra``.
        kind:   how to coerce the value on write.
        tab:    the MT5 Administrator symbol-dialog tab this field sits on.
    """

    key: str
    wire: str
    kind: str = STR
    tab: str = "common"


# ---------------------------------------------------------------------------
# Common tab
# ---------------------------------------------------------------------------
# Basis / Source are the two the operator asked about by name. `Source` is the
# one with teeth: MT5 says quotes for a symbol with a Source are taken "directly
# from the corresponding symbols in the data feed (without any transformation
# according to the settings of the corresponding symbol)", so it is a
# quote-routing setting, not a label.
_COMMON: Tuple[ExtraField, ...] = (
    ExtraField("isin", "ISIN", STR, "common"),
    ExtraField("cfi", "CFI", STR, "common"),
    ExtraField("category", "Category", STR, "common"),
    ExtraField("international", "International", STR, "common"),
    ExtraField("exchange", "Exchange", STR, "common"),
    ExtraField("sector", "Sector", STR, "common"),
    ExtraField("industry", "Industry", STR, "common"),
    ExtraField("country", "Country", STR, "common"),
    ExtraField("basis", "Basis", STR, "common"),
    ExtraField("source", "Source", STR, "common"),
    ExtraField("page", "Page", STR, "common"),
    ExtraField("color", "Color", STR, "common"),
    ExtraField("color_background", "ColorBackground", STR, "common"),
    # TickBookDepth is MT5's "Market depth" control. Non-zero ENABLES the book,
    # which per the docs then causes Spread / Spread Balance to be IGNORED and
    # disables tick filtration entirely - so it is not a cosmetic field.
    ExtraField("tick_book_depth", "TickBookDepth", INT, "common"),
    ExtraField("tick_chart_mode", "TickChartMode", ENUM, "common"),
)

# ---------------------------------------------------------------------------
# Currency tab
# ---------------------------------------------------------------------------
# Each of the three currencies carries its OWN digits on the wire. MT5 warns that
# standard world currencies have platform-set digits, while crypto and other
# non-standard currencies may need more - too few digits makes a cross-rate
# profit or margin round to zero.
_CURRENCY: Tuple[ExtraField, ...] = (
    ExtraField("currency_base_digits", "CurrencyBaseDigits", INT, "currency"),
    ExtraField("currency_profit_digits", "CurrencyProfitDigits", INT, "currency"),
    ExtraField("currency_margin_digits", "CurrencyMarginDigits", INT, "currency"),
)

# ---------------------------------------------------------------------------
# Quotes tab
# ---------------------------------------------------------------------------
# The ten filtration fields were completely invisible before this: they are the
# whole substance of the Quotes tab.
_QUOTES: Tuple[ExtraField, ...] = (
    # TickFlags is a BITMASK carrying the tab's four switches:
    #   REALTIME(1) COLLECTRAW(2) FEED_STATS(4) NEGATIVE_PRICES(8)
    ExtraField("tick_flags", "TickFlags", FLAGS, "quotes"),
    ExtraField("filter_soft", "FilterSoft", DEC, "quotes"),
    ExtraField("filter_soft_ticks", "FilterSoftTicks", INT, "quotes"),
    ExtraField("filter_hard", "FilterHard", DEC, "quotes"),
    ExtraField("filter_hard_ticks", "FilterHardTicks", INT, "quotes"),
    ExtraField("filter_discard", "FilterDiscard", DEC, "quotes"),
    ExtraField("filter_spread_min", "FilterSpreadMin", DEC, "quotes"),
    ExtraField("filter_spread_max", "FilterSpreadMax", DEC, "quotes"),
    ExtraField("filter_gap", "FilterGap", DEC, "quotes"),
    ExtraField("filter_gap_ticks", "FilterGapTicks", INT, "quotes"),
    ExtraField("subscriptions_delay", "SubscriptionsDelay", INT, "quotes"),
)

# ---------------------------------------------------------------------------
# Trade tab
# ---------------------------------------------------------------------------
_TRADE: Tuple[ExtraField, ...] = (
    # TRADE_FLAGS_PROFIT_BY_MARKET(1) | TRADE_FLAGS_ALLOW_SIGNALS(2)
    ExtraField("trade_flags", "TradeFlags", FLAGS, "trade"),
    # Max quote delay: seconds of quote silence after which trading auto-disables.
    ExtraField("quotes_timeout", "QuotesTimeout", INT, "trade"),
    # Futures-only settlement/limit prices (Exchange Futures / FORTS).
    ExtraField("price_settle", "PriceSettle", DEC, "trade"),
    ExtraField("price_limit_min", "PriceLimitMin", DEC, "trade"),
    ExtraField("price_limit_max", "PriceLimitMax", DEC, "trade"),
    ExtraField("splice_type", "SpliceType", ENUM, "trade"),
    ExtraField("splice_time_type", "SpliceTimeType", ENUM, "trade"),
    ExtraField("splice_time_days", "SpliceTimeDays", INT, "trade"),
)

# ---------------------------------------------------------------------------
# Execution tab
# ---------------------------------------------------------------------------
# The Instant-mode deviation controls. Documented as: the order is requoted when
# the price deviates more than these, in the profitable / losing direction
# respectively.
_EXECUTION: Tuple[ExtraField, ...] = (
    ExtraField("ie_check_mode", "IECheckMode", INT, "execution"),
    ExtraField("ie_timeout", "IETimeout", INT, "execution"),
    ExtraField("ie_slip_profit", "IESlipProfit", INT, "execution"),
    ExtraField("ie_slip_losing", "IESlipLosing", INT, "execution"),
    ExtraField("ie_volume_max", "IEVolumeMax", DEC, "execution"),
    # REQUEST_FLAGS_ORDER(1): dealer must additionally confirm.
    ExtraField("re_flags", "REFlags", FLAGS, "execution"),
    ExtraField("re_timeout", "RETimeout", INT, "execution"),
)

# ---------------------------------------------------------------------------
# Margin tab
# ---------------------------------------------------------------------------
# MarginInitial / MarginMaintenance / MarginHedged are read by db_to_symbol from
# mt5_extra already; listing them here makes them WRITABLE and exportable too.
_MARGIN: Tuple[ExtraField, ...] = (
    # MARGIN_FLAGS_CHECK_PROCESS(1) | MARGIN_FLAGS_CHECK_SLTP(2)
    ExtraField("margin_flags", "MarginFlags", FLAGS, "margin"),
    ExtraField("margin_initial_value", "MarginInitial", DEC, "margin"),
    ExtraField("margin_maintenance_value", "MarginMaintenance", DEC, "margin"),
    ExtraField("margin_hedged_value", "MarginHedged", DEC, "margin"),
    # The two RATES on the Margin Rates tab (merchant discounts on the value of
    # collateral / the FORTS currency radius), distinct from the eight
    # order-type multipliers which have their own columns.
    ExtraField("margin_liquidity_rate", "MarginLiquidity", DEC, "margin_rates"),
    ExtraField("margin_currency_rate", "MarginCurrency", DEC, "margin_rates"),
)

# ---------------------------------------------------------------------------
# Swaps tab
# ---------------------------------------------------------------------------
# The per-weekday multiplier curve. Wednesday carries the triple swap by market
# convention, which is why the reference export shows 3 on Friday for some
# symbols and 1 elsewhere - the curve is per symbol, not a global constant.
_SWAPS: Tuple[ExtraField, ...] = (
    ExtraField("swap_flags", "SwapFlags", FLAGS, "swaps"),
    ExtraField("swap_rate_sunday", "SwapRateSunday", DEC, "swaps"),
    ExtraField("swap_rate_monday", "SwapRateMonday", DEC, "swaps"),
    ExtraField("swap_rate_tuesday", "SwapRateTuesday", DEC, "swaps"),
    ExtraField("swap_rate_wednesday", "SwapRateWednesday", DEC, "swaps"),
    ExtraField("swap_rate_thursday", "SwapRateThursday", DEC, "swaps"),
    ExtraField("swap_rate_friday", "SwapRateFriday", DEC, "swaps"),
    ExtraField("swap_rate_saturday", "SwapRateSaturday", DEC, "swaps"),
)


EXTRA_FIELDS: Tuple[ExtraField, ...] = (
    _COMMON + _CURRENCY + _QUOTES + _TRADE + _EXECUTION + _MARGIN + _SWAPS
)

#: JSON key -> descriptor.
BY_KEY: Dict[str, ExtraField] = {f.key: f for f in EXTRA_FIELDS}

#: Alternative names the symbol editor uses for the SAME stored field.
#:
#: Each alias maps to the canonical descriptor, so accepting the alias does not create a
#: second stored key that could drift from the first. The Common tab sends `chart_mode`;
#: the registry and the MT5 wire both say `tick_chart_mode` / `TickChartMode`. Without
#: this the tab's own dropdown is rejected with the same 400 that `splice_type` produced.
ALIASES: Dict[str, str] = {
    "chart_mode": "tick_chart_mode",
}

#: Every alias, resolved to its canonical descriptor - so a lookup by any accepted name
#: finds the one field it means.
BY_ALIAS: Dict[str, ExtraField] = {
    alias: BY_KEY[canonical] for alias, canonical in ALIASES.items()
}

#: All accepted keys, canonical and alias alike. This is what the PUT allow-list and the
#: coercion consult, so a field cannot be accepted-but-ignored, or ignored-but-documented.
ACCEPTED_KEYS: Dict[str, ExtraField] = {**BY_KEY, **BY_ALIAS}

#: MT5 wire name -> descriptor.
BY_WIRE: Dict[str, ExtraField] = {f.wire: f for f in EXTRA_FIELDS}

#: The wire names an export must overlay from ``mt5_extra`` instead of leaving to
#: the imported baseline. See the module docstring - without this an edit is
#: masked on export.
OWNED_WIRE_KEYS = frozenset(f.wire for f in EXTRA_FIELDS)


#: Labels -> MT5 integer for the enumerated extras. The labels are the ones the symbol
#: editor's own dropdowns send, taken from SymbolDraftContext.tsx, so the registry and the
#: UI agree by construction rather than by luck.
_ENUM_LABELS: Dict[str, Dict[str, int]] = {
    # IMTConSymbol::EnSpliceType
    "SpliceType": {"NONE": 0, "UNADJUSTED": 1, "ADJUSTED": 2,
                   "NO_SPLICING": 0, "SPLICE_NONE": 0},
    # The extension period unit for spliced futures. MT5 documents the values as a plain
    # integer; labels are accepted for the ones the UI can produce.
    "SpliceTimeType": {"NONE": 0, "DAYS": 1, "WEEKS": 2, "MONTHS": 3},
    # IMTConSymbol::EnChartMode
    "TickChartMode": {"BID": 0, "BID_PRICE": 0, "LAST": 1, "LAST_PRICE": 1, "OLD": 255},
    # IMTConSymbol::EnOptionMode
    "OptionMode": {"EUROPEAN": 0, "AMERICAN": 1},
}


def _enum_int(field: ExtraField, value: Any) -> Optional[int]:
    """An enumerated extra as its MT5 integer, from a label, member name or integer.

    Returns None for a value that is not one of the known labels, so the caller raises a
    400 naming the field rather than storing something the trade server cannot read.
    """
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    text = str(value).strip()
    if text == "":
        return None
    # A numeric string is the integer form.
    try:
        return int(text)
    except ValueError:
        pass
    table = _ENUM_LABELS.get(field.wire)
    if table is None:
        return None
    # Normalise the label the way the UI writes it: 'none', 'bid', 'last', 'adjusted'.
    key = text.upper().replace("-", "_").replace(" ", "_")
    if key in table:
        return table[key]
    # Accept the canonical member name too, with or without its enum prefix.
    for prefix in ("SPLICE_", "CHART_MODE_"):
        if key.startswith(prefix):
            stripped = key[len(prefix):]
            if stripped in table:
                return table[stripped]
    return None


def _coerce(field: ExtraField, value: Any) -> Any:
    """Normalise an inbound value to what the wire expects.

    Raises ValueError on a value the field cannot hold, so a bad request is a 400
    rather than a row that silently stores something MT5 will not read back.
    """
    if value is None or value == "":
        return None

    if field.kind == INT:
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{field.key}: expected an integer, got {value!r}") from exc

    if field.kind == FLAGS:
        # Flags arrive either as the integer bitmask or as a list of set bit names;
        # both are accepted because the UI renders checkboxes.
        if isinstance(value, (list, tuple, set)):
            total = 0
            for name in value:
                member = getattr(_flag_enum(field), str(name).upper(), None)
                if member is None:
                    raise ValueError(f"{field.key}: unknown flag {name!r}")
                total |= int(member)
            return total
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{field.key}: expected flags, got {value!r}") from exc

    if field.kind == ENUM:
        resolved = _enum_int(field, value)
        if resolved is None:
            allowed = sorted(_ENUM_LABELS.get(field.wire, {}) or [])
            raise ValueError(
                f"{field.key}: {value!r} is not a valid value"
                + (f" (expected one of: {', '.join(allowed)})" if allowed else "")
            )
        return resolved

    if field.kind == DEC:
        try:
            # Stored as a STRING deliberately: MT5 decimals carry a per-field wire
            # scale, and a float would lose it.
            return str(Decimal(str(value)))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise ValueError(f"{field.key}: expected a number, got {value!r}") from exc

    return str(value)


def _flag_enum(field: ExtraField):
    from . import enums as instrument_enums

    mapping = {
        "TickFlags": instrument_enums.SymbolTickFlags,
        "TradeFlags": instrument_enums.SymbolTradeFlags,
        "MarginFlags": instrument_enums.SymbolMarginFlags,
        "SwapFlags": instrument_enums.SymbolSwapFlags,
        "REFlags": instrument_enums.SymbolRequestFlags,
    }
    return mapping[field.wire]


def read_values(extra: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Pull every known field out of an ``mt5_extra`` blob, under its JSON key.

    Only fields actually PRESENT are returned. A field the row does not carry is
    left out rather than defaulted to zero: MT5's own exports omit fields, and a
    fabricated 0 for a filtration level would read as "filter everything".
    """
    source = extra or {}
    out: Dict[str, Any] = {}
    for field in EXTRA_FIELDS:
        if field.wire in source:
            out[field.key] = source[field.wire]
    return out


def apply_updates(
    extra: Optional[Dict[str, Any]], updates: Dict[str, Any]
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Merge API-supplied values into an ``mt5_extra`` blob.

    Writes each value under its MT5 WIRE name, which is where the row and the
    export both read it from.

    Returns ``(merged_extra, applied)`` where ``applied`` maps the JSON key to the
    value actually stored, so the caller can report what changed rather than
    claiming success blindly.
    """
    merged = dict(extra or {})
    applied: Dict[str, Any] = {}
    for key, value in updates.items():
        field = ACCEPTED_KEYS.get(key)
        if field is None:
            continue
        coerced = _coerce(field, value)
        if coerced is None:
            merged.pop(field.wire, None)
            applied[key] = None
        else:
            merged[field.wire] = coerced
            applied[key] = coerced
    return merged, applied


def drain_legacy_template(extra: Optional[Dict[str, Any]]) -> Tuple[Dict[str, Any], list]:
    """Drop the stale lowercase frontend-template keys from an ``mt5_extra`` blob.

    A previous write stored a verbatim copy of the frontend's DEFAULT_SYMBOL_DRAFT
    into mt5_extra (lowercase keys such as ``soft_filter_level``). Measured on the
    live database, 25 of 25 sampled values equalled the frontend default exactly
    while the real server values sat unused under the wire names - so the symbol
    editor displayed fiction.

    The real fields are now read from the wire names, which makes the template not
    merely redundant but actively dangerous: anything still reading a lowercase key
    would keep showing the invented value. This removes them.

    Only keys that are BOTH lowercase AND outside the known set are dropped, so a
    deliberate non-MT5 key is not destroyed by accident.

    Returns ``(cleaned_extra, removed_keys)``.
    """
    source = dict(extra or {})
    removed = [k for k in source if k.islower() and k not in _NON_TEMPLATE_KEYS]
    for key in removed:
        source.pop(key, None)
    return source, removed


#: Lowercase keys in mt5_extra that are NOT part of the stale frontend template:
#: they are MT5 fields whose JSON key happens to be lowercase, or values written
#: by a deliberate path. Kept so drain_legacy_template cannot delete real data.
_NON_TEMPLATE_KEYS = frozenset(
    {
        # written by db_to_symbol's fallbacks / earlier migrations
        "margin_initial",
        "margin_maintenance",
        "margin_hedged",
        "hedged_use_larger_leg",
        "calc_hedged_larger_leg",
    }
)
