[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Enumerations

[Previous](../IMTConSymbol.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConSymbol](../IMTConSymbol.md) class contains the following enumerations:

  * [IMTConSymbol::EnFillingFlags (#enfillingflags)](Enumerations.md#enfillingflags)
  * [IMTConSymbol::EnExpirationFlags (#enexpirationflags)](Enumerations.md#enexpirationflags)
  * [IMTConSymbol::EnTradeMode (#entrademode)](Enumerations.md#entrademode)
  * [IMTConSymbol::EnExecutionMode (#enexecutionmode)](Enumerations.md#enexecutionmode)
  * [IMTConSymbol::EnCalcMode (#encalcmode)](Enumerations.md#encalcmode)
  * [IMTConSymbol::EnGTCMode (#engtcmode)](Enumerations.md#engtcmode)
  * [IMTConSymbol::EnTickFlags (#entickflags)](Enumerations.md#entickflags)
  * [IMTConSymbol::EnMarginFlags (#enmarginflags)](Enumerations.md#enmarginflags)
  * [IMTConSymbol::EnSwapMode (#enswapmode)](Enumerations.md#enswapmode)
  * [IMTConSymbol::EnSwapDays (#enswapdays)](Enumerations.md#enswapdays)
  * [IMTConSymbol::EnSwapFlags (#enswapflags)](Enumerations.md#enswapflags)
  * [IMTConSymbol::EnInstantMode (#eninstantmode)](Enumerations.md#eninstantmode)
  * [IMTConSymbol::EnRequestFlags (#enrequestflags)](Enumerations.md#enrequestflags)
  * [IMTConSymbol::EnTradeFlags (#entradeflags)](Enumerations.md#entradeflags)
  * [IMTConSymbol::EnOrderFlags (#enorderflags)](Enumerations.md#enorderflags)
  * [IMTConSymbol::EnMarginRateTypes (#enmarginratetypes)](Enumerations.md#enmarginratetypes)
  * [IMTConSymbol::EnSpliceType (#ensplicetype)](Enumerations.md#ensplicetype)
  * [IMTConSymbol::EnSpliceTimeType (#ensplicetimetype)](Enumerations.md#ensplicetimetype)
  * [IMTConSymbol::EnChartMode (#enchartmode)](Enumerations.md#enchartmode)
  * [IMTConSymbol::EnOptionMode (#enoptionmode)](Enumerations.md#enoptionmode)
  * [IMTConSymbol::EnInstantFlags (#eninstantflags)](Enumerations.md#eninstantflags)
  * [IMTConSymbol::EnSectors (#ensectors)](Enumerations.md#ensectors)
  * [IMTConSymbol::EnIndustries (#enindustries)](Enumerations.md#enindustries)



<a id="enfillingflags"></a>
## IMTConSymbol::EnFillingFlags (#enfillingflags)

The order filling methods allowed for a symbol are enumerated in IMTConSymbol::EnFillingFlags.

ID | Value | Description  
FILL_FLAGS_NONE | 0 | All filling methods are disabled.  
FILL_FLAGS_FOK | 1 | The "Fill or Kill" mode. The order must be filled completely or canceled. This type of filling is automatically set for [the instant and request execution](ExecMode.md).  
FILL_FLAGS_IOC | 2 | Immediate or Cancel. An order can be filled partially and the residual volume is canceled. This type of filling is only available for [the stock and market execution](ExecMode.md).  
FILL_FLAGS_BOC | 4 | "Passive" mode. It indicates that an order can only be placed in the Depth of Market (order book). If the order can be filled immediately when placed, this order is canceled. This policy guarantees that the price of the placed order will be worse than the current market. BOC is used to implement passive trading: it is guaranteed that the order cannot be executed immediately when placed and thus it does not affect current liquidity. This fill policy is only supported for limit and stop limit orders.  
FILL_FLAGS_FIRST |  | Beginning of enumeration. Corresponds to FILL_FLAGS_FOK.  
FILL_FLAGS_ALL | 7 | End of enumeration. All flags are enabled.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::FillFlags](FillFlags.md)
  * [IMTConGroupSymbol::FillFlags](../../Groups/IMTConGroupSymbol/FillFlags.md)
  * [IMTConGroupSymbol::FillFlagsDeafult](../../Groups/IMTConGroupSymbol/FillFlagsDefault.md)



<a id="enexpirationflags"></a>
## IMTConSymbol::EnExpirationFlags (#enexpirationflags)

Types of order expiration allowed for the symbol are enumerated in IMTConSymbol::EnExpirationFlags.

ID | Value | Description  
TIME_FLAGS_NONE | 0 | All expiration types are disabled.  
TIME_FLAGS_GTC | 1 | Orders are good till canceled.  
TIME_FLAGS_DAY | 2 | Orders are effective only during the current trading day.  
TIME_FLAGS_SPECIFIED | 4  | Orders are effective till the date specified by the trader.  
TIME_FLAGS_SPECIFIED_DAY | 8 | Orders with expiration at a specified day. An order expires at 00:00 of a specified day or at a nearest trade time. The expiration time is 00:00 of the specified day or the nearest trading time.  
TIME_FLAGS_FIRST |  | Beginning of enumeration. Corresponds to TIME_FLAGS_GTC.  
TIME_FLAGS_ALL | 15 | End of enumeration. All flags are enabled.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::ExpirFlags](ExpirFlags.md)
  * [IMTConGroupSymbol::ExpirFlags](../../Groups/IMTConGroupSymbol/ExpirFlags.md)
  * [IMTConGroupSymbol::ExpirFlagsDefault](../../Groups/IMTConGroupSymbol/ExpirFlagsDefault.md)



<a id="entrademode"></a>
## IMTConSymbol::EnTradeMode (#entrademode)

Symbol trading modes are enumerated in IMTConSymbol::EnTradeMode.

ID | Value | Description  
TRADE_DISABLED | 0 | Trade is disabled.  
TRADE_LONGONLY | 1 | Only long positions are allowed.  
TRADE_SHORTONLY | 2 | Only short positions are allowed.  
TRADE_CLOSEONLY | 3 | Only closure is allowed.  
TRADE_FULL | 4  | Full trading access.  
TRADE_FIRST |  | Beginning of enumeration. Corresponds to TRADE_DISABLED.  
TRADE_LAST |  | End of enumeration. Corresponds to TRADE_FULL.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::TradeMode](TradeMode.md)
  * [IMTConGroupSymbol::TradeMode](../../Groups/IMTConGroupSymbol/TradeMode.md)
  * [IMTConGroupSymbol::TradeModeDefault](../../Groups/IMTConGroupSymbol/TradeModeDefault.md)



<a id="enexecutionmode"></a>
## IMTConSymbol::EnExecutionMode (#enexecutionmode)

Execution types are enumerated in IMTConSymbol::EnExecutionMode.

ID | Value | Description  
EXECUTION_REQUEST | 0 | Request execution mode.  
EXECUTION_INSTANT | 1 | Instant execution mode.  
EXECUTION_MARKET | 2 | Market execution mode.  
EXECUTION_EXCHANGE | 3 | Exchange execution mode.  
EXECUTION_FIRST |  | Beginning of enumeration. Corresponds to EXECUTION_REQUEST.  
EXECUTION_LAST |  | End of enumeration. Corresponds to EXECUTION_EXCHANGE.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::ExecMode](ExecMode.md)
  * [IMTConGroupSymbol::ExecMode](../../Groups/IMTConGroupSymbol/ExecMode.md)
  * [IMTConGroupSymbol::ExecModeDefault](../../Groups/IMTConGroupSymbol/ExecModeDefault.md)



<a id="encalcmode"></a>
## IMTConSymbol::EnCalcMode (#encalcmode)

Types of profit and margin calculation for a symbol are enumerated in IMTConSymbol::EnCalcMode.

ID | Value | Description  
TRADE_MODE_FOREX | 0 | The Forex calculation mode.  
TRADE_MODE_FUTURES | 1 | The Futures calculation mode.  
TRADE_MODE_CFD | 2 | The CFD calculation mode.  
TRADE_MODE_CFDINDEX | 3 | The CFDIndex calculation mode.  
TRADE_MODE_CFDLEVERAGE | 4  | The CFDLeverage calculation mode.  
TRADE_MODE_FOREX_NO_LEVERAGE | 5 | Totally equivalent to the TRADE_MODE_FOREX type except that the client leverage is not taken into account when [calculating the margin (#noleverage)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex#noleverage). TRADE_MODE_FOREX_NO_LEVERAGE can be used if it is necessary to calculate the margin with a fixed leverage for all clients regardless of their actual leverage. If this type is selected, the client leverage is not taken into account when calculating the margin. A fixed leverage can be set through [margin rates](MarginRateInitial.md) (for example, the rate of 0.01 is similar to the leverage of 1:100).  
TRADE_MODE_MM_FIRST |  | Beginning of the enumeration of market modes. Corresponds to TRADE_MODE_FOREX.  
TRADE_MODE_MM_LAST |  | End of the enumeration of market modes. Corresponds to TRADE_MODE_FOREX_NO_LEVERAGE.  
TRADE_MODE_EXCH_STOCKS | 32 | The Exchange Stocks calculation mode.  
TRADE_MODE_EXCH_FUTURES | 33 | The Exchange Futures calculation mode.  
TRADE_MODE_EXCH_FORTS | 34 | The Exchange FORTS calculation mode for Derivatives Market of the Moscow Exchange.  
TRADE_MODE_EXCH_OPTIONS | 35 | The Exchange Options calculation mode.  
TRADE_MODE_EXCH_OPTIONS_MARGIN | 36 | The Exchange Margin Options calculation mode. The value is outdated and is not used.  
TRADE_MODE_EXCH_BONDS | 37 | The Exchange Bonds calculation mode.  
TRADE_MODE_EXCH_STOCKS_MOEX | 38 | Profit and margin calculation mode for the stocks traded at Moscow Exchange.  
TRADE_MODE_EXCH_BONDS_MOEX | 39 | Profit and margin calculation mode for the bonds traded at Moscow Exchange.  
TRADE_MODE_EXCH_FIRST |  | Beginning of the enumeration of exchange modes. Corresponds to TRADE_MODE_EXCH_STOCKS.  
TRADE_MODE_EXCH_LAST |  | End of the enumeration of exchange modes. Corresponds to TRADE_MODE_EXCH_BONDS_MOEX.  
TRADE_MODE_SERV_COLLATERAL | 64 | Non-tradable instruments of this type are used as client's assets to provide the required margin for open positions of other instruments. For these instruments the margin and profit are not calculated.  
TRADE_MODE_SERV_FIRST |  | Beginning of the enumeration of service modes. Corresponds to TRADE_MODE_SERV_COLLATERAL.  
TRADE_MODE_SERV_LAST |  | End of the enumeration of service modes. Corresponds to TRADE_MODE_SERV_COLLATERAL.  
TRADE_MODE_FIRST |  | Beginning of enumeration. Corresponds to TRADE_MODE_FOREX.  
TRADE_MODE_LAST |  | End of enumeration. Corresponds to TRADE_MODE_SERV_COLLATERAL.  
  
This enumeration is used in the [IMTConSymbol::CalcMode](CalcMode.md) method.

<a id="engtcmode"></a>
## IMTConSymbol::EnGTCMode (#engtcmode)

Modes of keeping orders at a trade day change are enumerated in IMTConSymbol::EnGTCMode.

ID | Value | Description  
ORDERS_GTC | 0 | "Good till canceled" orders. As a trade day changes, pending orders are preserved.  
ORDERS_DAILY | 1 | "Good till today including SL/TP" mode. As a trade day changes, all Stop Loss and Take Profit levels, as well all pending orders are deleted.  
ORDERS_DAILY_NO_STOPS | 2 | "Good till today excluding SL/TP" mode. As a trade day changes, only pending orders are deleted, Stop Loss and Take Profit levels are preserved.  
ORDERS_FIRST |  | Beginning of enumeration. Corresponds to ORDERS_GTC.  
ORDERS_LAST |  | End of enumeration. Corresponds to ORDERS_DAILY_NO_STOPS.  
  
This enumeration is used in the [IMTConSymbol::GTCMode](GTCMode.md) method.

<a id="entickflags"></a>
## IMTConSymbol::EnTickFlags (#entickflags)

Options of working with the symbol's tick data are enumerated in IMTConSymbol::EnTickFlags.

ID | Value | Description  
TICK_REALTIME | 1 | Allow real-time quotes from data feeds.  
TICK_COLLECTRAW | 2 | Save quotes as they come from data feeds. Ticks accepted by the platform in accordance with all filters and symbol settings are unconditionally saved. This option enables the additional saving of prices that the platform has not accepted (has discarded). You can use this option for the addition control and verification of filter operations. When enabling this options, please note that the stream of raw quotes will take up additional disk space.  
TICK_FEED_STATS | 4  | Receive market statistics (Ask High, Bid Low, etc.) directly from data feeds without calculation on the history server. If this flag is not set, the statistical information is calculated by the history server. This flag can only be set together with TICK_REALTIME.  
TICK_NEGATIVE_PRICES | 8 | The trading platform supports operations with negative security prices. If such a situation occurs in the market, all the appropriate functions will work correctly. This includes the display of quotes, calculation of profit margin, placing of orders, etc. However, such market situations are extremely rare, and negative values in the price stream are usually caused by an error on the data source side. Therefore, the history server rejects negative prices by default. To allow negative prices in the platform, you should enable the TICK_NEGATIVE_PRICES flag.  
TICK_NONE | 0 | Beginning of enumeration. Corresponds to the absence of rights.  
TICK_ALL | 7 | End of enumeration. Corresponds to enabling of all permissions.  
  
This enumeration is used in the [IMTConSymbol::TickFlags](TickFlags.md) method.

<a id="enmarginflags"></a>
## IMTConSymbol::EnMarginFlags (#enmarginflags)

The additional margin checks are enumerated in IMTConSymbol::EnMarginFlags.

ID | Value | Description  
MARGIN_FLAGS_NONE | 0x0000000 | The standard mode of margin checking. The margin is checked when any order is placed and when a pending orders triggers.  
MARGIN_FLAGS_CHECK_PROCESS | 0x0000001 | If this flags is enabled, another check of margin is added to those described above: the margin is checked before executing an order after it is confirmed (checked) by the server (at automated execution), by a dealer or by a gateway.  
MARGIN_FLAGS_CHECK_SLTP | 0x0000002 | This flag enables an additional check of margin before a position is closed by stop loss or take profit. If the position close results in reducing the margin to a level insufficient to maintain open positions and orders, the stop loss/take profit will not trigger, the position will stay open. This check must be enabled in case the trade operations are transmitted to an external system (exchange).  
MARGIN_FLAGS_HEDGE_LARGE_LEG | 0x0000004 | If the flag is enabled, the margin for hedged positions is calculated using larger leg (the total volume of users positions and orders opened in the same direction).  
MARGIN_FLAGS_EXCLUDE_PL | 0x0000008 | The flag affects the display of positions purchased with own funds, on accounts with margin trading enabled. If the flag is enabled, profit/loss of positions for the symbol will be ignored when calculating free margin, margin level and account equity. Also, Stop Out will not be applied to such positions.  
MARGIN_FLAGS_RECALC_RATES | 0x0000010 | If this flag is enabled, at the end of the trading day, the server will update the position margin conversion rate ([IMTPosition::RateMarin](../../../Database-Interfaces/Trade/Positions/IMTPosition/RateMargin.md)) at current market prices. For further details, please see the [Basic Margin Calculation (#recalculate-margin)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#recalculate-margin) section in MetaTrader 5 Administrator documentation.  
MARGIN_FLAGS_FIRST |  | Beginning of enumeration. Corresponds to MARGIN_FLAGS_NONE.  
MARGIN_FLAGS_LAST |  | End of enumeration. Corresponds to MARGIN_FLAGS_EXCLUDE_PL.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::MarginFlags](MarginFlags.md)
  * [IMTConGroupSymbol::MarginFlags](../../Groups/IMTConGroupSymbol/MarginFlags.md)
  * [IMTConGroupSymbol::MarginFlagsDefault](../../Groups/IMTConGroupSymbol/MarginFlagsDefault.md)



<a id="enswapmode"></a>
## IMTConSymbol::EnSwapMode (#enswapmode)

Types of swap calculation are enumerated in IMTConSymbol::EnSwapMode. The swap size is specified using the [IMTConSymbol::SwapLong](SwapLong.md) and [IMTConSymbol::SwapShort](SwapShort.md) methods.

ID | Value | Description  
SWAP_DISABLED | 0 | Swap charging is disabled.  
SWAP_BY_POINTS | 1 | Swaps are calculated as the amount of points of the symbol price.  
SWAP_BY_SYMBOL_CURRENCY | 2 | Swap charging in the base currency of a symbol.  
SWAP_BY_MARGIN_CURRENCY | 3 | Swap charging in the margin currency of a symbol.  
SWAP_BY_GROUP_CURRENCY | 4  | Swap charging in the group (deposit) currency.  
SWAP_BY_INTEREST_CURRENT | 5 | Swap charging as a per cent from the price of a symbol at calculation of swap.  
SWAP_BY_INTEREST_OPEN | 6 | Swap charging as a per cent from the open price of a position by a symbol.  
SWAP_REOPEN_BY_CLOSE_PRICE | 7 | Swap charging by reopening position. At the end of a trading day position is closed. Next day it is reopened by the close price +/- number of points specified using the [IMTConSymbol::SwapLong](SwapLong.md) and [IMTConSymbol::SwapShort](SwapShort.md) methods.  
SWAP_REOPEN_BY_BID | 8 | Swap charging by reopening position. At the end of a trading day position is closed. At the end of a trading day position is closed. Next day it is reopened by the current Bid price +/- number of points specified using the [IMTConSymbol::SwapLong](SwapLong.md) and [IMTConSymbol::SwapShort](SwapShort.md) methods.  
SWAP_BY_PROFIT_CURRENCY | 9 | Swap charging in the profit currency of a symbol.  
SWAP_FIRST |  | Beginning of enumeration. Corresponds to SWAP_DISABLED.  
SWAP_LAST |  | End of enumeration. Corresponds SWAP_BY_PROFIT_CURRENCY.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::SwapMode](SwapMode.md)
  * [IMTConGroupSymbol::SwapMode](../../Groups/IMTConGroupSymbol/SwapMode.md)
  * [IMTConGroupSymbol::SwapModeDefault](../../Groups/IMTConGroupSymbol/SwapModeDefault.md)



<a id="enswapdays"></a>
## IMTConSymbol::EnSwapDays (#enswapdays)

Triple swap charging days are enumerated in IMTConSymbol::EnSwapDays.

Identifier | Meaning | Declaration  
SWAP_DAY_SUNDAY | 0 | Sunday.  
SWAP_DAY_MONDAY | 1 | Monday.  
SWAP_DAY_TUESDAY | 2 | Tuesday.  
SWAP_DAY_WEDNESDAY | 3 | Wednesday.  
SWAP_DAY_THURSDAY | 4 | Thursday.  
SWAP_DAY_FRIDAY | 5 | Friday.  
SWAP_DAY_SATURDAY | 6 | Saturday.  
SWAP_DAY_DISABLED | 7 | Triple swaps are disabled.  
SWAP_DAY_FIRST |  | Beginning of enumeration. Corresponds to SWAP_DAY_SUNDAY.  
SWAP_DAY_LAST |  | End of enumeration. Corresponds to SWAP_DAY_DISABLED.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::Swap3Day](Swap3Day.md)
  * [IMTConGroupSymbol::SymbolSwap3Day](../../Groups/IMTConGroupSymbol/Swap3Day.md)
  * [IMTConGroupSymbol::Swap3DayDefault](../../Groups/IMTConGroupSymbol/Swap3DayDefault.md)



<a id="enswapflags"></a>
## IMTConSymbol::EnSwapFlags (#enswapflags)

Additional swap settings are enumerated in IMTConSymbol::EnSwapFlags.

ID | Value | Description  
SWAP_FLAGS_NONE | 0 | Additional settings are not used.  
SWAP_FLAGS_CONSIDER_HOLIDAYS | 1 | Account for holidays when calculating swaps. If the flag is enabled, the platform checks holiday configurations ([IMTConHoliday](../../Holidays/IMTConHoliday.md)). The day before the holiday, the swap is doubled. No swap is charged on the day of the holiday.  
SWAP_FLAGS_DEFAULT |  | Beginning of enumeration. Corresponds to SWAP_FLAGS_NONE.  
SWAP_FLAGS_ALL |  | Enumeration end. Corresponds to enabling of all flags.  
  
The enumeration is used in the following methods:

  * [IMTConSymbol::SwapFlags](SwapFlags.md)
  * [IMTConGroupSymbol::SwapFlags](../../Groups/IMTConGroupSymbol/SwapFlags.md)
  * [IMTConGroupSymbol::SwapFlagsDefault](../../Groups/IMTConGroupSymbol/SwapFlagsDefault.md)



<a id="eninstantmode"></a>
## IMTConSymbol::EnInstantMode (#eninstantmode)

Types of check for the instant execution mode are enumerate in IMTConSymbol::EnInstantMode.

ID | Value | Description  
INSTANT_CHECK_NORMAL | 0 | The normal mode of instant execution.  
INSTANT_CHECK_FIRST |  | Beginning of enumeration. Corresponds INSTANT_CHECK_NORMAL.  
INSTANT_CHECK_LAST |  | End of enumeration. Corresponds INSTANT_CHECK_NORMAL.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::IECheckMode](IECheckMode.md)
  * [IMTConGroupSymbol::IECheckMode](../../Groups/IMTConGroupSymbol/IECheckMode.md)
  * [IMTConGroupSymbol::IECheckModeDefault](../../Groups/IMTConGroupSymbol/IECheckModeDefault.md)



<a id="enrequestflags"></a>
## IMTConSymbol::EnRequestFlags (#enrequestflags)

Options of the Request execution mode ([IMTConSymbol::EXECUTION_REQUEST (#enexecutionmode)](Enumerations.md#enexecutionmode)) are enumerated in IMTConSymbol::EnRequestFlags.

ID | Value | Description  
REQUEST_FLAGS_NONE | 0 | No flags.  
REQUEST_FLAGS_ORDER | 1 | Additional confirmation mode.  
REQUEST_FLAGS_ALL |  | End of enumeration. Corresponds to REQUEST_FLAGS_ORDER.  
  
This enumeration is used in [IMTConSymbol::REFlags](REFlags.md).

<a id="entradeflags"></a>
## IMTConSymbol::EnTradeFlags (#entradeflags)

Trade flags of symbols are enumerated in IMTConSymbol::EnTradeFlags.

ID | Value | Description  
TRADE_FLAGS_NONE | 0 | Beginning of enumeration. Corresponds to the absence of flags.  
TRADE_FLAGS_PROFIT_BY_MARKET | 1 | This flag is used for the Forex type symbols only ([IMTConSymbol::TRADE_MODE_FOREX (#encalcmode)](Enumerations.md#encalcmode)).  By default for the conversion of profit/loss from the profit currency to the deposit currency, the price at which a deal (exit from position) is performed is used, the profitability/unprofitability of the deal is not taken into consideration. If this flag is enabled, the conversion is performed using the current Bid/Ask price depending of the profitability/unprofitability of a deal. The Bid price is taken for calculations for profitable deals, because as a result of a profitable deal, a trader obtains a certain amount of the profit currency and needs to sell it for the deposit currency. The Ask price is taken for losing deals, because as a result of a losing deal, a trader needs to buy a certain amount of currency for the deposit currency.  
TRADE_FLAGS_ALLOW_SIGNALS | 2 | If this flag is not enabled, clients will not be able to copy trade operations by this symbol using the ["Signals"](https://www.mql5.com/ru/signals) service. Trading signals can also be disabled on a client group level ([IMTConGroup::EnTradeFlags (#entradeflags)](../../Groups/IMTConGroup/Enumerations.md#entradeflags)).  
TRADE_FLAGS_ALL | 3 | End of enumeration. All flags are enabled.  
  
This enumeration is used in [IMTConSymbol::TradeFlags](TradeFlags.md).

<a id="enorderflags"></a>
## IMTConSymbol::EnOrderFlags (#enorderflags)

Flags of [orders (#enordertype)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype) that are allowed for the symbol are enumerated in IMTConSymbol::EnOrderFlags.

ID | Value | Description  
ORDER_FLAGS_NONE | 0 | Beginning of enumeration. Corresponds to the absence of flags.  
ORDER_FLAGS_MARKET | 1 | Market orders Buy and Sell are allowed.  
ORDER_FLAGS_LIMIT | 2 | Limit orders Buy Limit and Sell Limit are allowed.  
ORDER_FLAGS_STOP | 4  | Stop orders Buy Stop and Sell Stop are allowed.  
ORDER_FLAGS_STOP_LIMIT | 8 | Stop Limit orders Buy Stop Limit and Sell Stop Limit are allowed.  
ORDER_FLAGS_SL | 16 | Stop Loss orders are allowed.  
ORDER_FLAGS_TP | 32 | Take Profit orders are allowed.  
ORDER_FLAGS_CLOSEBY | 64 | Orders to close a position by an opposite one ([IMTOrder::OP_CLOSE_BY (#enordertype)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype)) are allowed. Close By permission of a symbol does not mean that this type of orders will be available on netting accounts. Close By orders can only be used on hedging accounts ([IMTConGroup::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](../../Groups/IMTConGroup/Enumerations.md#enmarginmode)).  
ORDER_FLAGS_FIRST |  | The first allowed order type in the enumeration. Corresponds to ORDER_FLAGS_MARKET.  
ORDER_FLAGS_ALL | 127 | End of enumeration. All flags are enabled.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::OrderFlags](OrderFlags.md)
  * [IMTConGroupSymbol::OrderFlags](../../Groups/IMTConGroupSymbol/OrderFlags.md)
  * [IMTConGroupSymbol::OrderFlagsDefault](../../Groups/IMTConGroupSymbol/OrderFlagsDefault.md)



<a id="enmarginratetypes"></a>
## IMTConSymbol::EnMarginRateTypes (#enmarginratetypes)

Types of [orders (#enordertype)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype) used for specified margin rates are enumerated in IMTConSymbol::EnMarginRateTypes.

ID | Value | Description  
MARGIN_RATE_BUY | 0 | A market Buy order.  
MARGIN_RATE_SELL | 1 | A market Sell order.  
MARGIN_RATE_BUY_LIMIT | 2 | A pending Buy Limit order.  
MARGIN_RATE_SELL_LIMIT | 3 | A pending Sell Limit order.  
MARGIN_RATE_BUY_STOP | 4  | A pending Buy Stop order.  
MARGIN_RATE_SELL_STOP | 5 | A pending Sell Stop order.  
MARGIN_RATE_BUY_STOP_LIMIT | 6 | Buy Stop Limit pending order.  
MARGIN_RATE_SELL_STOP_LIMIT | 7 | Sell Stop Limit pending order.  
MARGIN_RATE_FIRST |  | Beginning of enumeration. Corresponds to MARGIN_RATE_BUY.  
MARGIN_RATE_LAST |  | End of enumeration. Corresponds to MARGIN_RATE_SELL_STOP_LIMIT.  
  
This enumeration is used in the following methods:

  * [IMTConSymbol::MarginRateInitial](MarginRateInitial.md)
  * [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md)
  * [IMTConGroupSymbol::MarginRateInitial](../../Groups/IMTConGroupSymbol/MarginRateInitial.md)
  * [IMTConGroupSymbol::MarginRateInitialDefault](../../Groups/IMTConGroupSymbol/MarginRateInitialDefault.md)
  * [IMTConGroupSymbol::MarginRateMaintenance](../../Groups/IMTConGroupSymbol/MarginRateMaintenance.md)
  * [IMTConGroupSymbol::MarginRateMaintenanceDefault](../../Groups/IMTConGroupSymbol/MarginRateMaintenanceDefault.md)



<a id="ensplicetype"></a>
## IMTConSymbol::EnSpliceType (#ensplicetype)

Futures splicing types are available in IMTConSymbol::EnSpliceType.

ID | Value | Description  
SPLICE_NONE | 0 | No splicing.  
SPLICE_UNADJUSTED | 1 | Splicing futures quotes "as is" — the price level of the previous contract is not adjusted to the current (front) contract prices.  
SPLICE_ADJUSTED | 2 | In this mode, a difference between the last quote of the previous contract and the first quote of the front contract is calculated. This makes a spliced chart look smooth without gaps between contracts.  
SPLICE_FIRST |  | Beginning of enumeration. Corresponds to SPLICE_NONE.  
SPLICE_LAST |  | End of enumeration. Corresponds to SPLICE_ADJUSTED.  
  
This enumeration is used in the following methods:

  * [IMTConSymbols::SpliceType](SpliceType.md)



<a id="ensplicetimetype"></a>
## IMTConSymbol::EnSpliceTimeType (#ensplicetimetype)

Futures splicing dates are available in IMTConSymbol::EnSpliceTimeType.

ID | Value | Description  
SPLICE_TIME_EXPIRATION | 0 | Splicing at the very moment of instrument expiration [IMTConSymbol::TimeExpiration](TimeExpiration.md).  
SPLICE_FIRST |  | Beginning of enumeration. Corresponds to SPLICE_TIME_EXPIRATION.  
SPLICE_LAST |  | End of enumeration. Corresponds to SPLICE_TIME_EXPIRATION.  
  
This enumeration is used in the following methods:

  * [IMTConSymbols::SpliceTimeType](SpliceTimeType.md)



<a id="enchartmode"></a>
## IMTConSymbol::EnChartMode (#enchartmode)

IMTConSymbol::EnChartMode contains symbol charting modes.

Identifier | Value | Description  
CHART_MODE_BID_PRICE | 0 | The symbol chart is based on Bid prices.  
CHART_MODE_LAST_PRICE | 1 | The symbol chart is based on Last prices.  
CHART_MODE_OLD | 255 | Service value for internal use.  
CHART_MODE_FIRST |  | Beginning of enumeration. Corresponds to CHART_MODE_BID_PRICE.  
CHART_MODE_LAST |  | End of enumeration. Corresponds to CHART_MODE_OLD.  
  
This enumeration is used in the [IMTConSymbol::ChartMode](ChartMode.md) method.

<a id="enoptionmode"></a>
## IMTConSymbol::EnOptionMode (#enoptionmode)

Option types and styles are enumerated in IMTConSymbol::EnOptionMode.

Identifier | Value | Description  
OPTION_MODE_EUROPEAN_CALL | 0 | A European Call option  
OPTION_MODE_EUROPEAN_PUT | 1 | A European Put option  
OPTION_MODE_AMERICAN_CALL | 2 | An American Call option  
OPTION_MODE_AMERICAN_PUT | 3 | An American Out option  
OPTION_MODE_FIRST |  | Beginning of enumeration. Corresponds to OPTION_MODE_EUROPEAN_CALL.  
OPTION_MODE_LAST |  | End of enumeration. Corresponds to OPTION_MODE_AMERICAN_PUT.  
  
The enumeration is used in the [IMTConSymbol::OptionMode](OptionsMode.md) method.

<a id="eninstantflags"></a>
## IMTConSymbol::EnInstantFlags (#eninstantflags)

Options for the Instant execution mode ([IMTConSymbol::EXECUTION_INSTANT (#enexecutionmode)](Enumerations.md#enexecutionmode)) are enumerated in IMTConSymbol::EnInstantFlags.

Identifier | Value | Description  
INSTANT_FLAGS_NONE | 0 | No flags.  
INSTANT_FLAGS_FAST_CONFIRMATION | 1 | The option is disabled by default. When creating a trade request in the instant execution mode, the client can specify tolerance, i.e. by how many points the request execution price can differ from the price specified in the order. If a dealer returns a requote in response to such a request, and the requote price is within the tolerable deviation specified by the client, the order will be returned to the dealer for confirmation after the client confirms this new price. If the option is enabled, the order will be executed immediately after the client confirms the price. No additional confirmation from a dealer is required.  
INSTANT_FLAGS_ALL |  | End of enumeration. Corresponds to INSTANT_FLAGS_FAST_CONFIRMATION.  
  
The enumeration is used in the [IMTConSymbol::IEFlags](IEFlags.md) method.

<a id="ensectors"></a>
## IMTConSymbol::EnSectors (#ensectors)

IMTConSymbol::EnSectors lists economic sectors a trading instrument may belong to.

ID | Value | Description  
SECTOR_UNDEFINED | 0 | Undefined  
SECTOR_BASIC_MATERIALS | 1 | Basic materials  
SECTOR_COMMUNICATION_SERVICES | 2 | Communication services  
SECTOR_CONSUMER_CYCLICAL | 3 | Consumer cyclical  
SECTOR_CONSUMER_DEFENSIVE | 4 | Consumer defensive  
SECTOR_ENERGY | 5 | Energy  
SECTOR_FINANCIAL | 6 | Finance  
SECTOR_HEALTHCARE | 7 | Healthcare  
SECTOR_INDUSTRIALS | 8 | Industrials  
SECTOR_REAL_ESTATE | 9 | Real estate  
SECTOR_TECHNOLOGY | 10 | Technology  
SECTOR_UTILITIES | 11 | Utilities  
SECTOR_CURRENCY | 12 | Currency  
SECTOR_CURRENCY_CRYPTO | 13 | Crypto currency  
SECTOR_INDEXES | 14 | Indices  
SECTOR_COMMODITIES | 15 | Commodities  
SECTOR_FIRST |  | Beginning of enumeration. Corresponds to SECTOR_UNDEFINED.  
SECTOR_LAST |  | End of enumeration. Corresponds to SECTOR_UTILITIES.  
  
The enumeration is used in the [IMTConSymbol::Sector](Sector.md) method.

<a id="enindustries"></a>
## IMTConSymbol::EnIndustries (#enindustries)

IMTConSymbol::EnIndustries lists industry branches a trading instrument may belong to.

ID | Value | Description  
INDUSTRY_UNDEFINED | 0 | Undefined  
Basic materials  
INDUSTRY_AGRICULTURAL_INPUTS | 1 | Agricultural inputs  
INDUSTRY_ALUMINIUM | 2 | Aluminium  
INDUSTRY_BUILDING_MATERIALS | 3 | Building materials  
INDUSTRY_CHEMICALS | 4 | Chemicals  
INDUSTRY_COKING_COAL | 5 | Coking coal  
INDUSTRY_COPPER | 6 | Copper  
INDUSTRY_GOLD | 7 | Gold  
INDUSTRY_LUMBER_WOOD | 8 | Lumber and wood production  
INDUSTRY_INDUSTRIAL_METALS | 9 | Other industrial metals and mining  
INDUSTRY_PRECIOUS_METALS | 10 | Other precious metals and mining  
INDUSTRY_PAPER | 11 | Paper and paper products  
INDUSTRY_SILVER | 12 | Silver  
INDUSTRY_SPECIALTY_CHEMICALS | 13 | Specialty chemicals  
INDUSTRY_STEEL | 14 | Steel  
INDUSTRY_BASIC_MATERIALS_FIRST | 1 | Beginning of the basic materials types enumeration. Corresponds to INDUSTRY_AGRICULTURAL_INPUTS.  
INDUSTRY_BASIC_MATERIALS_LAST | 14 | End of the basic materials types enumeration. Corresponds to INDUSTRY_STEEL.  
INDUSTRY_BASIC_MATERIALS_END | 50 | Basic materials types enumeration limit.  
Communication services  
INDUSTRY_ADVERTISING | 51 | Advertising agencies  
INDUSTRY_BROADCASTING | 52 | Broadcasting  
INDUSTRY_GAMING_MULTIMEDIA | 53 | Electronic gaming and multimedia  
INDUSTRY_ENTERTAINMENT | 54 | Entertainment  
INDUSTRY_INTERNET_CONTENT | 55 | Internet content and information  
INDUSTRY_PUBLISHING | 56 | Publishing  
INDUSTRY_TELECOM | 57 | Telecom services  
INDUSTRY_COMMUNICATION_FIRST | 51 | Beginning of the communication services types enumeration. Corresponds to INDUSTRY_ADVERTISING.  
INDUSTRY_COMMUNICATION_LAST | 57 | End of the communication services types enumeration. Corresponds to INDUSTRY_TELECOM.  
INDUSTRY_COMMUNICATION_END | 100 | Communication services types enumeration limit.  
Consumer cyclical  
INDUSTRY_APPAREL_MANUFACTURING | 101 | Apparel manufacturing  
INDUSTRY_APPAREL_RETAIL | 102 | Apparel retail  
INDUSTRY_AUTO_MANUFACTURERS | 103 | Auto manufacturers  
INDUSTRY_AUTO_PARTS | 104 | Auto parts  
INDUSTRY_AUTO_DEALERSHIP | 105 | Auto and truck dealerships  
INDUSTRY_DEPARTMENT_STORES | 106 | Department stores  
INDUSTRY_FOOTWEAR_ACCESSORIES | 107 | Footwear and accessories  
INDUSTRY_FURNISHINGS | 108 | Furnishing, fixtures and appliances  
INDUSTRY_GAMBLING | 109 | Gambling  
INDUSTRY_HOME_IMPROV_RETAIL | 110 | Home improvement retail  
INDUSTRY_INTERNET_RETAIL | 111 | Internet retail  
INDUSTRY_LEISURE | 112 | Leisure  
INDUSTRY_LODGING | 113 | Lodging  
INDUSTRY_LUXURY_GOODS | 114 | Luxury goods  
INDUSTRY_PACKAGING_CONTAINERS | 115 | Packaging and containers  
INDUSTRY_PERSONAL_SERVICES | 116 | Personal services  
INDUSTRY_RECREATIONAL_VEHICLES | 117 | Recreational vehicles  
INDUSTRY_RESIDENT_CONSTRUCTION | 118 | Residential construction  
INDUSTRY_RESORTS_CASINOS | 119 | Resorts and casinos  
INDUSTRY_RESTAURANTS | 120 | Restaurants  
INDUSTRY_SPECIALTY_RETAIL | 121 | Specialty retail  
INDUSTRY_TEXTILE_MANUFACTURING | 122 | Textile manufacturing  
INDUSTRY_TRAVEL_SERVICES | 123 | Travel services  
INDUSTRY_CONSUMER_CYCL_FIRST | 101 | Beginning of enumeration of industry branches related to production of goods and services of cyclical demand. Corresponds to INDUSTRY_APPAREL_MANUFACTURING.  
INDUSTRY_CONSUMER_CYCL_LAST | 123 | End of enumeration of industry branches related to production of goods and services of cyclical demand. Corresponds to INDUSTRY_TRAVEL_SERVICES.  
INDUSTRY_CONSUMER_CYCL_END | 150 | Limit of the enumeration of industry branches related to production of goods and services of cyclical demand.  
Consumer defensive  
INDUSTRY_BEVERAGES_BREWERS | 151 | Beverages - Brewers  
INDUSTRY_BEVERAGES_NON_ALCO | 152 | Beverages - Non-alcoholic  
INDUSTRY_BEVERAGES_WINERIES | 153 | Beverages - Wineries and distilleries  
INDUSTRY_CONFECTIONERS | 154 | Confectioners  
INDUSTRY_DISCOUNT_STORES | 155 | Discount stores  
INDUSTRY_EDUCATION_TRAINIG | 156 | Education and training services  
INDUSTRY_FARM_PRODUCTS | 157 | Farm products  
INDUSTRY_FOOD_DISTRIBUTION | 158 | Food distribution  
INDUSTRY_GROCERY_STORES | 159 | Grocery stores  
INDUSTRY_HOUSEHOLD_PRODUCTS | 160 | Household and personal products  
INDUSTRY_PACKAGED_FOODS | 161 | Packaged foods  
INDUSTRY_TOBACCO | 162 | Tobacco  
INDUSTRY_CONSUMER_DEF_FIRST | 151 | Beginning of enumeration of industry branches related to production of consumer defensive goods and services. Corresponds to INDUSTRY_BEVERAGES_BREWERS.  
INDUSTRY_CONSUMER_DEF_LAST | 162 | End of enumeration of industry branches related to production of consumer defensive goods and services. Corresponds to INDUSTRY_TOBACCO.  
INDUSTRY_CONSUMER_DEF_END | 200 | Limit of the enumeration of industry branches related to production of consumer defensive goods and services.  
Energy  
INDUSTRY_OIL_GAS_DRILLING | 201 | Oil and gas drilling  
INDUSTRY_OIL_GAS_EP | 202 | Oil and gas extraction and processing  
INDUSTRY_OIL_GAS_EQUIPMENT | 203 | Oil and gas equipment and services  
INDUSTRY_OIL_GAS_INTEGRATED | 204 | Oil and gas integrated  
INDUSTRY_OIL_GAS_MIDSTREAM | 205 | Oil and gas midstream  
INDUSTRY_OIL_GAS_REFINING | 206 | Oil and gas refining and marketing  
INDUSTRY_THERMAL_COAL | 207 | Thermal coal  
INDUSTRY_URANIUM | 208 | Uranium  
INDUSTRY_ENERGY_FIRST | 201 | Beginning of enumeration of energy industry types. Corresponds to INDUSTRY_OIL_GAS_DRILLING.  
INDUSTRY_ENERGY_LAST | 208 | End of enumeration of energy industry types. Corresponds to INDUSTRY_URANIUM.  
INDUSTRY_ENERGY_END | 250 | Limit of the energy industry types enumeration.  
Finance  
INDUSTRY_EXCHANGE_TRADED_FUND | 251 | Exchange traded fund  
INDUSTRY_ASSETS_MANAGEMENT | 252 | Assets management  
INDUSTRY_BANKS_DIVERSIFIED | 253 | Banks - Diversified  
INDUSTRY_BANKS_REGIONAL | 254 | Banks - Regional  
INDUSTRY_CAPITAL_MARKETS | 255 | Capital markets  
INDUSTRY_CLOSE_END_FUND_DEBT | 256 | Closed-End fund - Debt  
INDUSTRY_CLOSE_END_FUND_EQUITY | 257 | Closed-end fund - Equity  
INDUSTRY_CLOSE_END_FUND_FOREIGN | 258 | Closed-end fund - Foreign  
INDUSTRY_CREDIT_SERVICES | 259 | Credit services  
INDUSTRY_FINANCIAL_CONGLOMERATE | 260 | Financial conglomerates  
INDUSTRY_FINANCIAL_DATA_EXCHANGE | 261 | Financial data and stock exchange  
INDUSTRY_INSURANCE_BROKERS | 262 | Insurance brokers  
INDUSTRY_INSURANCE_DIVERSIFIED | 263 | Insurance - Diversified  
INDUSTRY_INSURANCE_LIFE | 264 | Insurance - Life  
INDUSTRY_INSURANCE_PROPERTY | 265 | Insurance - Property and casualty  
INDUSTRY_INSURANCE_REINSURANCE | 266 | Insurance - Reinsurance  
INDUSTRY_INSURANCE_SPECIALTY | 267 | Insurance - Specialty  
INDUSTRY_MORTGAGE_FINANCE | 268 | Mortgage finance  
INDUSTRY_SHELL_COMPANIES | 269 | Shell companies  
INDUSTRY_FINANCIAL_FIRST | 251 | Beginning of enumeration of the financial services types. Corresponds to INDUSTRY_EXCHANGE_TRADED_FUND.  
INDUSTRY_FINANCIAL_LAST | 269 | End of enumeration of the financial services types. Corresponds to INDUSTRY_SHELL_COMPANIES.  
INDUSTRY_FINANCIAL_END | 300 | Limit of the financial services types enumeration.  
Healthcare  
INDUSTRY_BIOTECHNOLOGY | 301 | Biotechnology  
INDUSTRY_DIAGNOSTICS_RESEARCH | 302 | Diagnostics and research  
INDUSTRY_DRUGS_MANUFACTURERS | 303 | Drugs manufacturers - general  
INDUSTRY_DRUGS_MANUFACTURERS_SPEC | 304 | Drugs manufacturers - Specialty and generic  
INDUSTRY_HEALTHCARE_PLANS | 305 | Healthcare plans  
INDUSTRY_HEALTH_INFORMATION | 306 | Health information services  
INDUSTRY_MEDICAL_FACILITIES | 307 | Medical care facilities  
INDUSTRY_MEDICAL_DEVICES | 308 | Medical devices  
INDUSTRY_MEDICAL_DISTRIBUTION | 309 | Medical distribution  
INDUSTRY_MEDICAL_INSTRUMENTS | 310 | Medical instruments and supplies  
INDUSTRY_PHARM_RETAILERS | 311 | Pharmaceutical retailers  
INDUSTRY_HEALTHCARE_FIRST | 301 | Beginning of enumeration of healthcare services types. Corresponds to INDUSTRY_BIOTECHNOLOGY.  
INDUSTRY_HEALTHCARE_LAST | 311 | End of enumeration of healthcare services types. Corresponds to INDUSTRY_PHARM_RETAILERS.  
INDUSTRY_HEALTHCARE_END | 350 | Limit of the healthcare services types enumeration.  
Industrials  
INDUSTRY_AEROSPACE_DEFENSE | 351 | Aerospace and defense  
INDUSTRY_AIRLINES | 352 | Airlines  
INDUSTRY_AIRPORTS_SERVICES | 353 | Airports and air services  
INDUSTRY_BUILDING_PRODUCTS | 354 | Building products and equipment  
INDUSTRY_BUSINESS_EQUIPMENT | 355 | Business equipment and supplies  
INDUSTRY_CONGLOMERATES | 356 | Conglomerates  
INDUSTRY_CONSULTING_SERVICES | 357 | Consulting services  
INDUSTRY_ELECTRICAL_EQUIPMENT | 358 | Electrical equipment and parts  
INDUSTRY_ENGINEERING_CONSTRUCTION | 359 | Engineering and construction  
INDUSTRY_FARM_HEAVY_MACHINERY | 360 | Farm and heavy construction machinery  
INDUSTRY_INDUSTRIAL_DISTRIBUTION | 361 | Industrial distribution  
INDUSTRY_INFRASTRUCTURE_OPERATIONS | 362 | Infrastructure operations  
INDUSTRY_FREIGHT_LOGISTICS | 363 | Integrated freight and logistics  
INDUSTRY_MARINE_SHIPPING | 364 | Marine shipping  
INDUSTRY_METAL_FABRICATION | 365 | Metal fabrication  
INDUSTRY_POLLUTION_CONTROL | 366 | Pollution and treatment controls  
INDUSTRY_RAILROADS | 367 | Railroads  
INDUSTRY_RENTAL_LEASING | 368 | Rental and leasing services  
INDUSTRY_SECURITY_PROTECTION | 369 | Security and protection services  
INDUSTRY_SPEALITY_BUSINESS_SERVICES | 370 | Specialty business services  
INDUSTRY_SPEALITY_MACHINERY | 371 | Specialty industrial machinery  
INDUSTRY_STUFFING_EMPLOYMENT | 372 | Stuffing and employment services  
INDUSTRY_TOOLS_ACCESSORIES | 373 | Tools and accessories  
INDUSTRY_TRUCKING | 374 | Trucking  
INDUSTRY_WASTE_MANAGEMENT | 375 | Waste management  
INDUSTRY_INDUSTRIALS_FIRST | 351 | Beginning of enumeration of industry types. Corresponds to INDUSTRY_AEROSPACE_DEFENSE.  
INDUSTRY_INDUSTRIALS_LAST | 375 | End of enumeration of industry types. Corresponds to INDUSTRY_WASTE_MANAGEMENT.  
INDUSTRY_INDUSTRIALS_END | 400 | Limit of the industry types enumeration.  
Real estate  
INDUSTRY_REAL_ESTATE_DEVELOPMENT | 401 | Real estate - Development  
INDUSTRY_REAL_ESTATE_DIVERSIFIED | 402 | Real estate - Diversified  
INDUSTRY_REAL_ESTATE_SERVICES | 403 | Real estate services  
INDUSTRY_REIT_DIVERSIFIED | 404 | REIT - Diversified  
INDUSTRY_REIT_HEALTCARE | 405 | REIT - Healthcase facilities  
INDUSTRY_REIT_HOTEL_MOTEL | 406 | REIT - Hotel and motel  
INDUSTRY_REIT_INDUSTRIAL | 407 | REIT - Industrial  
INDUSTRY_REIT_MORTAGE | 408 | REIT - Mortgage  
INDUSTRY_REIT_OFFICE | 409 | REIT - Office  
INDUSTRY_REIT_RESIDENTAL | 410 | REIT - Residential  
INDUSTRY_REIT_RETAIL | 411 | REIT - Retail  
INDUSTRY_REIT_SPECIALITY | 412 | REIT - Specialty  
INDUSTRY_REAL_ESTATE_FIRST | 401 | Beginning of enumeration of the real estate services types. Corresponds to INDUSTRY_REAL_ESTATE_DEVELOPMENT.  
INDUSTRY_REAL_ESTATE_LAST | 412 | End of enumeration of the real estate services types. Corresponds to INDUSTRY_REIT_SPECIALITY.  
INDUSTRY_REAL_ESTATE_END | 450 | Limit of the real estate services types enumeration.  
Technology  
INDUSTRY_COMMUNICATION_EQUIPMENT | 451 | Communication equipment  
INDUSTRY_COMPUTER_HARDWARE | 452 | Computer hardware  
INDUSTRY_CONSUMER_ELECTRONICS | 453 | Consumer electronics  
INDUSTRY_ELECTRONIC_COMPONENTS | 454 | Electronic components  
INDUSTRY_ELECTRONIC_DISTRIBUTION | 455 | Electronics and computer distribution  
INDUSTRY_IT_SERVICES | 456 | Information technology services  
INDUSTRY_SCIENTIFIC_INSTRUMENTS | 457 | Scientific and technical instruments  
INDUSTRY_SEMICONDUCTOR_EQUIPMENT | 458 | Semiconductor equipment and materials  
INDUSTRY_SEMICONDUCTORS | 459 | Semiconductors  
INDUSTRY_SOFTWARE_APPLICATION | 460 | Software - Application  
INDUSTRY_SOFTWARE_INFRASTRUCTURE | 461 | Software - Infrastructure  
INDUSTRY_SOLAR | 462 | Solar  
INDUSTRY_TECHNOLOGY_FIRST | 451 | Beginning of enumeration of high-tech industry types. Corresponds to INDUSTRY_COMMUNICATION_EQUIPMENT.  
INDUSTRY_TECHNOLOGY_LAST | 462 | End of enumeration of high-tech industry types. Corresponds to INDUSTRY_SOLAR.  
INDUSTRY_TECHNOLOGY_END | 500 | Limit of the high-tech industry types enumeration.  
Utilities  
INDUSTRY_UTILITIES_DIVERSIFIED | 501 | Utilities - Diversified  
INDUSTRY_UTILITIES_POWERPRODUCERS | 502 | Utilities - Independent power producers  
INDUSTRY_UTILITIES_RENEWABLE | 503 | Utilities - Renewable  
INDUSTRY_UTILITIES_REGULATED_ELECTRIC | 504 | Utilities - Regulated electric  
INDUSTRY_UTILITIES_REGULATED_GAS | 505 | Utilities - Regulated gas  
INDUSTRY_UTILITIES_REGULATED_WATER | 506 | Utilities - Regulated water  
INDUSTRY_UTILITIES_FIRST | 501 | Beginning of enumeration of utilities services types. Corresponds to INDUSTRY_UTILITIES_DIVERSIFIED.  
INDUSTRY_UTILITIES_LAST | 506 | End of enumeration of utilities services types. Corresponds to INDUSTRY_UTILITIES_REGULATED_WATER.  
INDUSTRY_UTILITIES_END | 550 | Limit of the utilities services types enumeration.  
Commodities  
INDUSTRY_COMMODITIES_AGRICULTURAL | 551 | Agriculture  
INDUSTRY_COMMODITIES_ENERGY | 552 | Energy  
INDUSTRY_COMMODITIES_METALS | 553 | Metals  
INDUSTRY_COMMODITIES_PRECIOUS | 554 | Precious metals  
INDUSTRY_COMMODITIES_FIRST | 551 | Beginning of enumeration of commodity types. Corresponds to INDUSTRY_COMMODITIES_AGRICULTURAL.  
INDUSTRY_COMMODITIES_LAST | 554 | End of enumeration of commodity types Corresponds to INDUSTRY_COMMODITIES_PRECIOUS.  
INDUSTRY_COMMODITIES_END | 600 | Limit of the commodity type enumeration.  
INDUSTRY_FIRST | 0 | Beginning of enumeration. Corresponds to INDUSTRY_UNDEFINED.  
INDUSTRY_LAST | 506 | End of enumeration. Corresponds to INDUSTRY_COMMODITIES_LAST.  
  
The enumeration is used in the [IMTConSymbol::Industry](Industry.md) method.
