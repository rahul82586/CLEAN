"""Instruments domain enumerations.

Every value here is taken from the MT5 SDK C++ headers (``Include.md`` in the
reference corpus), not inferred from the member names. The previous version of this
file was labelled "MT5-accurate" but four enums were not, and because the MT5 wire
format is an integer, mapping by ordinal position silently misreads real server data.

Measured against a live export of 362 symbols, the old values would have produced:

    CalcMode  4  -> read as BONDS     (MT5: CFDLEVERAGE)          245 symbols
    CalcMode  5  -> read as STOCKS    (MT5: FOREX_NO_LEVERAGE)     54 symbols
    CalcMode  2  -> read as FUTURES   (MT5: CFD)                   18 symbols
    SwapMode  3  -> read as INTEREST_CURRENT (MT5: BY_MARGIN_CURRENCY)  7 symbols
    SwapMode  5  -> read as REOPEN_CURRENT   (MT5: INTEREST_CURRENT)    5 symbols

ExecutionMode, TradeMode and ExpirationFlags were already correct and are unchanged.
"""

from enum import Enum, IntFlag


class CalculationMode(Enum):
    """Margin/PnL calculation algorithm (MT5 ``EnCalcMode``).

    This is NOT an asset-class taxonomy. It selects the formula the trade server uses
    to compute margin and profit, which is why ``CFDLEVERAGE`` and
    ``FOREX_NO_LEVERAGE`` exist as distinct modes. The previous FOREX/CFD/FUTURES/
    OPTIONS/BONDS/STOCKS/INDICES/CRYPTO/METALS/ENERGY list described asset classes and
    did not correspond to MT5 at all; asset class belongs in ``Path`` / ``Category`` /
    ``Sector``, which the symbol model stores separately.
    """

    FOREX = 0                 # TRADE_MODE_FOREX
    FUTURES = 1               # TRADE_MODE_FUTURES
    CFD = 2                   # TRADE_MODE_CFD
    CFD_INDEX = 3             # TRADE_MODE_CFDINDEX
    CFD_LEVERAGE = 4          # TRADE_MODE_CFDLEVERAGE - the most common setting
    FOREX_NO_LEVERAGE = 5     # TRADE_MODE_FOREX_NO_LEVERAGE
    EXCHANGE_STOCKS = 32      # TRADE_MODE_EXCH_STOCKS
    EXCHANGE_FUTURES = 33     # TRADE_MODE_EXCH_FUTURES
    EXCHANGE_FUTURES_FORTS = 34  # TRADE_MODE_EXCH_FUTURES_FORTS
    EXCHANGE_OPTIONS = 35     # TRADE_MODE_EXCH_OPTIONS
    EXCHANGE_OPTIONS_MARGIN = 36  # TRADE_MODE_EXCH_OPTIONS_MARGIN
    EXCHANGE_BONDS = 37       # TRADE_MODE_EXCH_BONDS
    EXCHANGE_STOCKS_MOEX = 38  # TRADE_MODE_EXCH_STOCKS_MOEX
    EXCHANGE_BONDS_MOEX = 39  # TRADE_MODE_EXCH_BONDS_MOEX
    SERV_COLLATERAL = 64      # TRADE_MODE_SERV_COLLATERAL


class ExecutionMode(Enum):
    """Order execution mode (MT5 ``EnExecutionMode``). Values already matched MT5."""

    REQUEST = 0    # EXECUTION_REQUEST - manual dealer confirmation
    INSTANT = 1    # EXECUTION_INSTANT - instant execution with slippage control
    MARKET = 2     # EXECUTION_MARKET  - market execution, no requotes
    EXCHANGE = 3   # EXECUTION_EXCHANGE


class TradeMode(Enum):
    """Symbol trade mode (MT5 ``EnTradeMode``). Values already matched MT5."""

    DISABLED = 0   # TRADE_DISABLED
    LONGONLY = 1   # TRADE_LONGONLY
    SHORTONLY = 2  # TRADE_SHORTONLY
    CLOSEONLY = 3  # TRADE_CLOSEONLY
    FULL = 4       # TRADE_FULL


class FillingFlags(IntFlag):
    """Order filling policy (MT5 ``EnFillingFlags``). A BITMASK, not a choice.

    MT5 names bit 4 ``FILL_FLAGS_BOC`` (back of chain); the previous member name
    ``RETURN`` described the same bit and is kept as an alias so existing call sites
    keep working.
    """

    NONE = 0x00000000
    FOK = 0x00000001    # FILL_FLAGS_FOK - fill or kill
    IOC = 0x00000002    # FILL_FLAGS_IOC - immediate or cancel
    BOC = 0x00000004    # FILL_FLAGS_BOC - back of chain
    RETURN = 0x00000004  # deprecated alias for BOC


class ExpirationFlags(IntFlag):
    """Order expiration policy (MT5 ``EnExpirationFlags``). Values already matched MT5."""

    NONE = 0x00000000
    GTC = 0x00000001          # TIME_FLAGS_GTC
    DAY = 0x00000002          # TIME_FLAGS_DAY
    SPECIFIED = 0x00000004    # TIME_FLAGS_SPECIFIED
    SPECIFIED_DAY = 0x00000008  # TIME_FLAGS_SPECIFIED_DAY


class GTCMode(Enum):
    """Pending-order lifetime (MT5 ``EnGTCMode``).

    MT5 has three members. The previous TRADE/CALENDAR pair did not correspond:
    ``ORDERS_DAILY`` cancels pending orders at end of day, and
    ``ORDERS_DAILY_NO_STOPS`` does the same but preserves SL/TP. Neither is a
    "calendar" mode. ``GTC`` (0) is what the old ``TRADE`` member was reaching for.
    """

    GTC = 0              # ORDERS_GTC
    DAILY = 1            # ORDERS_DAILY
    DAILY_NO_STOPS = 2   # ORDERS_DAILY_NO_STOPS


class SwapMode(Enum):
    """Swap/rollover calculation mode (MT5 ``EnSwapMode``).

    The previous ordinals diverged from MT5 at value 2 and dropped three modes
    entirely (BY_MARGIN_CURRENCY, BY_GROUP_CURRENCY, BY_PROFIT_CURRENCY). Note that
    BY_MARGIN_CURRENCY is the mode that makes the margin currency - which need not
    equal the quote currency - participate in the swap calculation.
    """

    DISABLED = 0            # SWAP_DISABLED
    POINTS = 1              # SWAP_BY_POINTS
    SYMBOL_CURRENCY = 2     # SWAP_BY_SYMBOL_CURRENCY
    MARGIN_CURRENCY = 3     # SWAP_BY_MARGIN_CURRENCY
    GROUP_CURRENCY = 4      # SWAP_BY_GROUP_CURRENCY
    INTEREST_CURRENT = 5    # SWAP_BY_INTEREST_CURRENT
    INTEREST_OPEN = 6       # SWAP_BY_INTEREST_OPEN
    REOPEN_CLOSE_PRICE = 7  # SWAP_REOPEN_BY_CLOSE_PRICE
    REOPEN_BID = 8          # SWAP_REOPEN_BY_BID
    PROFIT_CURRENCY = 9     # SWAP_BY_PROFIT_CURRENCY

    # Deprecated aliases for the old member names, so existing call sites keep
    # resolving. They carry the CORRECT MT5 value, not the old ordinal.
    CURRENCY = 2            # deprecated alias for SYMBOL_CURRENCY
    REOPEN_CURRENT = 7      # deprecated alias for REOPEN_CLOSE_PRICE


class OrderTypeFlags(IntFlag):
    """Which order types a symbol accepts (MT5 ``EnOrderFlags``). A BITMASK.

    This replaces the previous ``OrderFlags`` enum in this module, whose members
    (TRADE / TRADE_EXPERT / TRADE_PLUGIN) described *who placed an order* rather than
    *which order types are permitted*. Those two concepts are unrelated, and the same
    name ``OrderFlags`` was simultaneously used for a third concept in
    ``core.domains.oms.enums`` (NO_SL / NO_TP / NO_SLTP_BY_TICK, which are activation
    flags). Every symbol in the reference export carries the value 127, i.e. all seven
    of these bits set.
    """

    NONE = 0x00000000
    MARKET = 0x00000001       # ORDER_FLAGS_MARKET
    LIMIT = 0x00000002        # ORDER_FLAGS_LIMIT
    STOP = 0x00000004         # ORDER_FLAGS_STOP
    STOP_LIMIT = 0x00000008   # ORDER_FLAGS_STOP_LIMIT
    SL = 0x00000010           # ORDER_FLAGS_SL
    TP = 0x00000020           # ORDER_FLAGS_TP
    CLOSEBY = 0x00000040      # ORDER_FLAGS_CLOSEBY


# Deprecated alias. Prefer OrderTypeFlags; this exists only so that in-flight imports
# of the old name keep resolving to the corrected bitmask rather than failing.
OrderFlags = OrderTypeFlags


class OptionMode(Enum):
    """Option exercise style (MT5 ``EnOptionMode``)."""

    EUROPEAN = 0
    AMERICAN = 1


class HolidayMode(Enum):
    """Holiday applicability (MT5 ``EnHolidayMode``)."""

    DISABLED = 0
    ENABLED = 1
# ---------------------------------------------------------------------------
# Bitmask / enum fields surfaced by the symbol editor
# (Common / Quotes / Trade / Execution / Margin / Swaps tabs)
#
# Every value below is transcribed from the SDK's
# IMTConSymbol/Enumerations.md, not inferred from the member names -- the same
# rule this module's header states, and the same mistake it warns about.
#
# NAMING: MT5 reuses the name TradeFlags for two unrelated bitmasks. The GROUP
# one (accounts.enums.TradeFlags, TRADEFLAGS_*) is a different field with
# different values (0x1F, 0x400...). Ours is therefore SymbolTradeFlags, and
# nothing here shadows the group enum: get_field_schema expands enum names
# across BOTH modules, so a collision would make the group schema silently
# expand the wrong member list.
# ---------------------------------------------------------------------------


class SymbolTickFlags(IntFlag):
    """IMTConSymbol::EnTickFlags - the Quotes tab's four switches.

    This is the field the Quotes tab is really made of. The previous UI read a
    stale lowercase template out of mt5_extra instead of this, so every tick
    filtration switch shown to an operator was a frontend default rather than
    the value the trade server actually holds.

    Note TICK_ALL is 7, i.e. REALTIME|COLLECTRAW|FEED_STATS -- the SDK does NOT
    include TICK_NEGATIVE_PRICES in ALL, because negative prices are only legal
    for futures. Defining ALL as 15 would silently let negative prices through
    on every instrument.
    """

    NONE = 0             # TICK_NONE
    REALTIME = 1         # TICK_REALTIME        allow real-time quotes from data feeds
    COLLECTRAW = 2       # TICK_COLLECTRAW      save raw, unfiltered ticks
    FEED_STATS = 4       # TICK_FEED_STATS      receive market statistics from data feeds
    NEGATIVE_PRICES = 8  # TICK_NEGATIVE_PRICES futures only
    ALL = 7              # TICK_ALL


class SymbolMarginFlags(IntFlag):
    """IMTConSymbol::EnMarginFlags - the Margin tab's additional margin checks."""

    NONE = 0x0000000           # MARGIN_FLAGS_NONE
    CHECK_PROCESS = 0x0000001  # check before executing orders
    CHECK_SLTP = 0x0000002     # check on SL-TP trigger


class SymbolSwapFlags(IntFlag):
    """IMTConSymbol::EnSwapFlags - the Swaps tab's holiday handling."""

    NONE = 0               # SWAP_FLAGS_NONE
    CONSIDER_HOLIDAYS = 1  # SWAP_FLAGS_CONSIDER_HOLIDAYS


class SymbolRequestFlags(IntFlag):
    """IMTConSymbol::EnRequestFlags - Request execution mode."""

    NONE = 0   # REQUEST_FLAGS_NONE
    ORDER = 1  # REQUEST_FLAGS_ORDER  additional confirmation mode


class SymbolInstantFlags(IntFlag):
    """IMTConSymbol::EnInstantFlags - Instant execution mode."""

    NONE = 0               # INSTANT_FLAGS_NONE
    FAST_CONFIRMATION = 1  # INSTANT_FLAGS_FAST_CONFIRMATION


class SymbolTradeFlags(IntFlag):
    """IMTConSymbol::EnTradeFlags - the Trade tab's two switches.

    Distinct from accounts.enums.TradeFlags, which is the GROUP bitmask. Values
    in the reference export are 0 or 2 (ETHUSD carries 2 = signals on).
    """

    NONE = 0              # TRADE_FLAGS_NONE
    PROFIT_BY_MARKET = 1  # TRADE_FLAGS_PROFIT_BY_MARKET (Forex symbols only)
    ALLOW_SIGNALS = 2     # TRADE_FLAGS_ALLOW_SIGNALS
    ALL = 3               # TRADE_FLAGS_ALL


class SymbolSwapDays(Enum):
    """IMTConSymbol::EnSwapDays - which weekday carries the triple swap.

    Sunday-first, matching the MT5 wire. DISABLED (7) turns triple swaps off.
    The symbol column swap_3day defaults to 3 = WEDNESDAY, the market convention
    and what the reference export carries.
    """

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    DISABLED = 7


class SymbolChartMode(Enum):
    """IMTConSymbol::EnChartMode - the Common tab's chart mode.

    OLD = 255 is a service value the SDK documents as "for internal use". It is
    kept so a round trip of a legacy server value need not invent a member, but
    it is not offered as a choice in the UI.
    """

    BID_PRICE = 0   # CHART_MODE_BID_PRICE
    LAST_PRICE = 1  # CHART_MODE_LAST_PRICE
    OLD = 255       # CHART_MODE_OLD


class SymbolSpliceType(Enum):
    """IMTConSymbol::EnSpliceType - how futures contract quotes are spliced."""

    NONE = 0        # SPLICE_NONE
    UNADJUSTED = 1  # SPLICE_UNADJUSTED
    ADJUSTED = 2    # SPLICE_ADJUSTED


class MarginRateType(Enum):
    """IMTConSymbol::EnMarginRateTypes - the eight Margin Rates tab rows, in the
    order MT5 presents them.

    The tab is a grid: these eight order types down the side and Initial /
    Maintenance across. The order IS the tab's layout, so it is declared here
    rather than left to whichever order a dict happened to be built in.
    """

    BUY = 0              # MARGIN_RATE_BUY
    SELL = 1             # MARGIN_RATE_SELL
    BUY_LIMIT = 2        # MARGIN_RATE_BUY_LIMIT
    SELL_LIMIT = 3       # MARGIN_RATE_SELL_LIMIT
    BUY_STOP = 4         # MARGIN_RATE_BUY_STOP
    SELL_STOP = 5        # MARGIN_RATE_SELL_STOP
    BUY_STOP_LIMIT = 6   # MARGIN_RATE_BUY_STOP_LIMIT
    SELL_STOP_LIMIT = 7  # MARGIN_RATE_SELL_STOP_LIMIT
