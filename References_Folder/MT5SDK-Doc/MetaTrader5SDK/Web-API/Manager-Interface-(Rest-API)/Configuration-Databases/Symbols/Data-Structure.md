[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Data Structure

[Previous](../Symbols.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Symbol configuration is passed in JSON format in response to the [/api/symbol/next](Get-by-Index.md), [/api/symbol/get](Get-by-Name-or-Mask.md) and[/api/symbol/get_group](Get-by-Group.md) requests.

<a id="symbol"></a>
## Symbol Parameters (#symbol)

The symbol configuration includes the following parameters:

Option Field | Type | Description  
Symbol | String | Symbol name.  
Path | String | Path to a symbol.  
ISIN | String | International Securities Identification Number (ISIN) of a symbol.  
Description | String | Symbol description.  
International | String | The international symbol name.  
Category | String | The name of the category or sector to which the symbol belongs.  
Exchange | String | The name of the exchange in which the security is traded.  
CFI | String | Instrument classification in accordance with the ISO 10962 standard.  
Sector | Integer | The economic sector the instrument belongs to. Passed as a value of the [EnSectors (#ensectors)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#ensectors) enumeration.  
Industry | Integer | The industry branch the instrument belongs to. Passed as a value of the [EnIndustries (#enindustries)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enindustries) enumeration.  
Country | String | The country of the company whose shares are traded on the stock exchange.  
Basis | String | The underlying asset of a derivative financial instrument.  
Source | String | The name of the source symbol whose quotes are used for the current financial instrument.  
Page | String | The address of the web page of a symbol.  
CurrencyBase | String | The base currency of a symbol.  
CurrencyBaseDigits | Integer | The accuracy of conversion into the base currency.  
CurrencyProfit | String | The profit currency for a symbol.  
CurrencyProfitDigits | Integer | The accuracy of conversion into the profit currency.  
CurrencyMargin | String | The symbol margin currency.  
CurrencyMarginDigits | Integer | The accuracy of conversion into the margin currency.  
Color | Integer | The color of the symbol in the "Market Watch" window of the terminals.  
ColorBackground | Integer | The color of the symbol background in the "Market Watch" window of the terminals.  
Digits | Integer | The number of decimal places in the price of the symbol.  
Point | Float | Point value.  
Multiply | Float | The value to multiply the price to, to get the number of points.  
TickFlags | Integer | Options for working with tick data. Passed as a value of the [EnTickFlags (#entickflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entickflags) enumeration (sum of values of appropriate flags).  
TickBookDepth | Integer | The range of the Depth of Market.  
FilterSoft | Integer | The soft level of price filtering.  
FilterSoftTicks | Integer | The value of the ticks counter for the soft filtering.  
FilterHard | Integer | The hard level of price filtering.  
FilterHardTicks | Integer | The value of the ticks counter for the hard filtering.  
FilterDiscard | Integer | The discard level of price filtering.  
FilterSpreadMax | Integer | The maximum allowed spread value.  
FilterSpreadMin | Integer | The minimum allowed spread.  
FilterGapTicks | Integer | The number of ticks for disabling the gap mode. If no new gap occurs within the specified number of quotes, the mode is disabled.  
SubscriptionsDelay | Integer | The delivery delay for the quotes provided by subscription. Indicated in minutes.  
TickChartMode | Integer | The mode of creation of the symbol chart: 0 — using the Bid price, 1 — using the Last price.  
TradeMode | Integer | The symbol trading mode. Passed in a value of the [EnTradeMode (#entrademode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entrademode) enumeration.  
CalcMode | Integer | The mode of margin and profit calculation. Passed in a value of the [EnCalcMode (#encalcmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode) enumeration.  
ExecMode | Integer | Execution mode of a symbol. Passed in a value of the [EnExecutionMode (#enexecutionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexecutionmode) enumeration.  
GTCMode | Integer | Types of orders that can be set for the symbol. Passed as a value of the [EnGTCMode (#engtcmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#engtcmode) enumeration (sum of values of appropriate flags).  
FillFlags | Integer | Types of filling allowed for the symbol. Passed as a value of the [EnFillingFlags (#enfillingflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enfillingflags) enumeration (sum of values of appropriate flags).  
ExpirFlags | Integer | Available types of order expiration for a symbol. Passed as a value of the [EnExpirationFlags (#enexpirationflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexpirationflags) enumeration (sum of values of appropriate flags).  
Spread | Integer | Symbol spread size.  
SpreadBalance | Integer | Symbol spread balance. Spread balance is set a shift from the equal distribution of the spread value between Bid and Ask prices. For example, if the spread is 10, its distribution in the ratio of -5 Bid/+ 5 Ask is equal to the spread balance value of 0. Ratio -6 Bid/+4 Ask corresponds to -1, ratio -4 Bid/+6 Ask corresponds to 1.  
SpreadDiff | Integer | Symbol spread difference. This parameter returns the base value of the balance of spread difference, which is actually equal to 0. To work with spread difference of a particular group, the [corresponding parameter of the group](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md) should be used.  
SpreadDiffBalance | Integer | Spread balance difference This parameter returns the base value of the balance of spread difference, which is actually equal to 0. To work with the balance of spread difference of a certain group, the [corresponding parameter of the group](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md) should be used.  
TickValue | Float | The price of one tick of a symbol.  
TickSize | Float | The size of one tick of a symbol.  
ContractSize | Float | The contract size for the symbol.  
StopsLevel | Integer | The price band, within which placing stop orders is not allowed.  
FreezeLevel | Integer | The price band, within which it is not allowed to modify orders and positions.  
QuotesTimeout | Integer | The time in seconds to wait for quotes, after which trading is automatically disabled for the symbol.  
VolumeMin | Integer | The minimum volume of trade operations for a symbol. One unit corresponds to 1/10000 lot.  
VolumeMax | Integer | The maximum volume of trade operations for a symbol. One unit corresponds to 1/10000 lot.  
VolumeStep | Integer | The volume change step for trade operations for a symbol. One unit corresponds to 1/10000 lot.  
VolumeLimit | Integer | The maximum allowed aggregate volume of positions and orders for a symbol in one direction. One unit corresponds to 1/10000 lot.  
MarginFlags | Integer | Additional margin checking modes. Passed in a value of the [EnMarginFlags (#enmarginflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enmarginflags).  
MarginInitial | Float | The size of the initial margin.  
MarginMaintenance | Float | The size of the maintenance margin.  
MarginInitialBuy | Float | The initial margin rate for market Buy orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY.  
MarginInitialSell | Float | The initial margin rate for market Sell orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL.  
MarginInitialBuyLimit | Float | The initial margin rate for Buy Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_LIMIT.  
MarginInitialSellLimit | Float | The initial margin rate for Sell Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_LIMIT.  
MarginInitialBuyStop | Float | The initial margin rate for Buy Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP.  
MarginInitialSellStop | Float | The initial margin rate for Sell Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP.  
MarginInitialBuyStopLimit | Float | The initial margin rate for Buy Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP_LIMIT.  
MarginInitialSellStopLimit | Float | The initial margin rate for Sell Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP_LIMIT.  
MarginMaintenanceBuy | Float | The maintenance margin rate for market Buy orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY.  
MarginMaintenanceSell | Float | The maintenance margin rate for market Sell orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL.  
MarginMaintenanceBuyLimit | Float | The maintenance margin rate for Buy Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_LIMIT.  
MarginMaintenanceSellLimit | Float | The maintenance margin rate for Sell Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_LIMIT.  
MarginMaintenanceBuyStop | Float | The maintenance margin rate for Buy Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP.  
MarginMaintenanceSellStop | Float | The maintenance margin rate for Sell Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP.  
MarginMaintenanceBuyStopLimit | Float | The maintenance margin rate for Buy Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP_LIMIT.  
MarginMaintenanceSellStopLimit | Float | The maintenance margin rate for Sell Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP_LIMIT.  
MarginHedged | Float | The hedged margin value.  
MarginRateCurrency | Float | Currency margin rate (rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble).  
MarginRateLiquidity | Float | The liquidity rate of the symbol for the group. It determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).  
SwapMode | Integer | The swap calculation mode for a symbol. Passed in a value of the [EnSwapMode (#enswapmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enswapmode) enumeration.  
SwapLong | Float | The swap size for long positions.  
SwapShort | Float | The swap size for short positions.  
Swap3Day | Integer | The day to charge triple swap. The day is specified by a value 0 (Sunday) to 6 (Saturday).  
SwapYearDays | Integer | The number of days in a year used in calculating swap percent. Passed by the [EnSwapDays (#enswapdays)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enswapdays) enumeration value.  
SwapFlags | Integer | Additional swap settings. Passed by the [EnSwapFlags (#enswapflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enswapflags) enumeration value.  
SwapRateSunday | Float | Swap multiplier for Sundays.  
SwapRateMonday | Float | Swap multiplier for Mondays.  
SwapRateTuesday | Float | Swap multiplier for Tuesdays.  
SwapRateWednesday | Float | Swap multiplier for Wednesdays.  
SwapRateThursday | Float | Swap multiplier for Thursdays.  
SwapRateFriday | Float | Swap multiplier for Fridays.  
SwapRateSaturday | Float | Swap multiplier for Saturdays.  
TimeStart | Integer | The start date of trading for a symbol. It is considered that there is no time limitation for trading by a symbol if both TimeStart and TimeExpiration are equal to 0.  
TimeExpiration | Integer | The date of trading expiration for a symbol. It is considered that there is no time limitation for trading by a symbol if both TimeStart and TimeExpiration are equal to 0.  
SessionsQuotes | Array | The array of [quoting sessions (#session)](Data-Structure.md#session).  
SessionsTrades | Array | The array of [trading sessions (#session)](Data-Structure.md#session).  
REFlags | Integer | The request execution flags. Passed as a value of the [EnRequestsFlags (#enrequestflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enrequestflags) enumeration (sum of values of appropriate flags).  
RETimeout | Integer | Time in seconds during which the price issued by a dealer in the request execution mode is valid.  
IECheckMode | Integer | Check mode for instant execution. Passed in a value of the [EnInstantMode (#eninstantmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#eninstantmode) enumeration.  
IETimeout | Integer | The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price. Specified in seconds.  
IESlipProfit | Integer | The maximum allowed slippage in the profitable direction during instant execution.  
IESlipLosing | Integer | The maximum allowed slippage in the loss direction during instant execution.  
IEVolumeMax | Integer | The maximum volume of a trade operation that can be executed in the instant execution mode.One unit corresponds to 1/10000 lot.  
PriceSettle | Float | The clearing price of the previous session.  
PriceLimitMax | Float | The maximum allowed price of the symbol.  
PriceLimitMin | Float | The minimum allowed price of the symbol.  
TradeFlags | Integer | The trade flags of the symbol. Passed as a value of the [EnTradeFlags (#entradeflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entradeflags) enumeration.  
OrderFlags | Integer | The flags of order types that are allowed for the symbol. Passed in a value of the [EnOrderFlags (#enorderflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enorderflags) enumeration (sum of values of appropriate flags).  
FaceValue | Float | The face value of a bond.  
AccruedInterest | Float | The accrued interest of a bond.  
SpliceType | Integer | The futures contract splicing type.  
SpliceTimeType | Integer | The date of splicing of the futures contracts.  
SpliceTimeDays | Integer | The offset of splicing of the futures contracts.  
ChartMode | Integer | The mode of creation of the symbol chart. Passed as a value of the [EnChartMode (#enchartmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enchartmode) enumeration.  
OptionMode | Integer | Option type and style. Passed as a value of the [EnOptionMode (#enoptionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enoptionmode) enumeration.  
PriceStrike | Float | The price, at which an option gives the right to buy or sell an asset (the strike price).  
  
<a id="session"></a>
## Session Parameters (#session)

Information about quoting and trading sessions is passed as two-dimensional arrays [7][N] in the [SessionsQuotes](Data-Structure.md) and [SessionsTrades](Data-Structure.md) parameters of a symbol. The first dimension denotes days of the wees (starting with Sunday), the second one denotes session parameters shown above. The size of the second dimension varies according to the number of sessions created for the symbol. 

Option Field | Type | Description  
Open | Integer | The opening time of a trading or quoting session of a symbol in minutes elapsed since 00:00. For example, 100 denotes 01:40.  
Close | Integer | The closing time of a trading or quoting session of a symbol in minutes elapsed since 00:00.
