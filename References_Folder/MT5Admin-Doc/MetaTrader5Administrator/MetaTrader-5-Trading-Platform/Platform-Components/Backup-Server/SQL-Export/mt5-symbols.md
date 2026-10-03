[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_symbols

[Previous](Installation-and-Setup-of-PostgreSQL.md) | [Next](mt5-symbols/Enumerations.md)

# mt5_symbols

[Symbols'](../../../Platform-Setup/Symbols.md) configurations are exported to the table. The table contains the following fields:

Name | Type | Description  
Symbol_ID | Integer | Primary key. Unique symbol ID for more efficient request of the symbol data from the database. Assigned automatically during the export.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
Symbol | String | Symbol name.  
Path | String | Path to a symbol.  
ISIN | String | International Securities Identification Number (ISIN) of a symbol.  
Description | String | Symbol description.  
International | String | The international symbol name.  
Category | String | The name of the category or sector to which the symbol belongs.  
Exchange | String | The name of the exchange in which the security is traded.  
CFI | String | Instrument classification in accordance with the ISO 10962 standard.  
Sector | Integer | The economic sector the instrument belongs to. Passed as a value of the [EnSectors (#ensectors)](mt5-symbols/Enumerations.md#ensectors) enumeration.  
Industry | Integer | The industry branch the instrument belongs to. Passed as a value of the [EnIndustries (#enindustries)](mt5-symbols/Enumerations.md#enindustries) enumeration.  
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
Color | COLORREF | The color of the symbol in the "Market Watch" window of the terminals.  
ColorBackground | COLORREF | The color of the symbol background in the "Market Watch" window of the terminals.  
Digits | Integer | The number of decimal places in the price of the symbol.  
Point | Float | Point size. Calculated as 1/10^Digits.  
Multiply | Float | The value to multiply the price to, to get the number of points. Calculated as 10^Digits.  
TickFlags | Integer | Options for working with tick data. Passed as a value of the [EnTicksFlags (#entickflags)](mt5-symbols/Enumerations.md#entickflags) enumeration (sum of values of appropriate flags).  
TickBookDepth | Integer | The range of the Depth of Market.  
FilterSoft | Integer | The soft level of price filtering.  
FilterSoftTicks | Integer | The value of the ticks counter for the soft filtering.  
FilterHard | Integer | The hard level of price filtering.  
FilterHardTicks | Integer | The value of the ticks counter for the hard filtering.  
FilterDiscard | Integer | The discard level of price filtering.  
FilterSpreadMax | Integer | The maximum allowed spread value.  
FilterSpreadMin | Integer | The minimum allowed spread.  
SubscriptionsDelay | Integer | The delivery delay for the quotes provided by subscription. Indicated in minutes.  
TradeMode | Integer | The symbol trading mode. Passed in a value of the [EnTradeMode (#entrademode)](mt5-symbols/Enumerations.md#entrademode) enumeration.  
CalcMode | Integer | The mode of margin and profit calculation. Passed in a value of the [EnCalcMode (#encalcmode)](mt5-symbols/Enumerations.md#encalcmode) enumeration.  
ExecMode | Integer | Execution mode of a symbol. Passed in a value of the [EnExecutionMode (#enexecutionmode)](mt5-symbols/Enumerations.md#enexecutionmode) enumeration.  
GTCMode | Integer | Types of orders that can be set for the symbol. Passed as a value of the [EnGTCMode (#engtcmode)](mt5-symbols/Enumerations.md#engtcmode) enumeration (sum of values of appropriate flags).  
FillFlags | Integer | Types of filling allowed for the symbol. Passed as a value of the [EnFillingFlags (#enfillingflags)](mt5-symbols/Enumerations.md#enfillingflags) enumeration (sum of values of appropriate flags).  
ExpirFlags | Integer | Available types of order expiration for a symbol. Passed as a value of the [EnExpirationFlags (#enexpirationflags)](mt5-symbols/Enumerations.md#enexpirationflags) enumeration (sum of values of appropriate flags).  
Spread | Integer | Symbol spread size.  
SpreadBalance | Integer | Symbol spread balance. Spread balance is set a shift from the equal distribution of the spread value between Bid and Ask prices. For example, if the spread is equal to 10 and it is distributed as -5 Bid/+5 Ask, then the spread balance value is 0. The -6 Bid/+4 Ask ratio corresponds to value -1, ratio -4 Bid/+6 Ask corresponds to value 1.  
SpreadDiff | Integer | Symbol spread difference. This parameter returns the base value of the spread, which is actually equal to 0. To work with spread difference of a particular group, the [corresponding parameter of the group](mt5-groups-symbols.md) should be used.  
SpreadDiffBalance | Integer | Spread balance difference. This parameter returns the base value of the balance of spread difference, which is actually equal to 0. To work with the balance of spread difference of a certain group, the [corresponding parameter of the group](mt5-groups-symbols.md) should be used.  
TickValue | Float | The price of one tick of a symbol.  
TickSize | Float | The size of one tick of a symbol.  
ContractSize | Float | The contract size for the symbol.  
StopsLevel | Integer | The price band, within which placing stop orders is not allowed.  
FreezeLevel | Integer | The price band, within which it is not allowed to modify orders and positions.  
QuotesTimeout | Integer | The time to wait for quotes in seconds, after which trading is automatically disabled for the symbol.  
VolumeMin | Integer | The minimum volume of trade operations for a symbol. One unit corresponds to 1/10000 lot.  
VolumeMinExt | Integer | The minimum volume of trade operations for the symbol for the group with extended accuracy. One unit corresponds to 1/100000000 lot.  
VolumeMax | Integer | The maximum volume of trade operations for a symbol. One unit corresponds to 1/10000 lot.  
VolumeMaxExt | Integer | The maximum volume of trade operations for the symbol for the group with extended accuracy. One unit corresponds to 1/100000000 lot.  
VolumeStep | Integer | The volume change step for trade operations for a symbol. One unit corresponds to 1/10000 lot.  
VolumeStepExt | Integer | The volume change step allowed for trade operations for the symbol, with extended accuracy. One unit corresponds to 1/100000000 lot.  
VolumeLimit | Integer | The maximum allowed aggregate volume of positions and orders for a symbol in one direction. One unit corresponds to 1/10000 lot.  
VolumeLimitExt | Integer | The maximum aggregate volume (with extended accuracy) of positions and orders for the symbol in one direction. One unit corresponds to 1/100000000 lot.  
MarginFlags | Integer | Additional margin checking modes. Passed in a value of the [EnMarginFlags (#enmarginflags)](mt5-symbols/Enumerations.md#enmarginflags) enumeration.  
MarginInitial | Float | The size of the initial margin.  
MarginMaintenance | Float | The size of the maintenance margin.  
MarginInitialBuy | Float | The initial margin rate for market Buy orders.  
MarginInitialSell | Float | The initial margin rate for market Sell orders.  
MarginInitialBuyLimit | Float | The initial margin rate for Buy Limit orders.  
MarginInitialSellLimit | Float | The initial margin rate for Sell Limit orders.  
MarginInitialBuyStop | Float | The initial margin rate for Buy Stop orders.  
MarginInitialSellStop | Float | The initial margin rate for Sell Stop orders.  
MarginInitialBuyStopLimit | Float | The initial margin rate for Buy Stop Limit orders.  
MarginInitialSellStopLimit | Float | The initial margin rate for Sell Stop Limit orders.  
MarginMaintenanceBuy | Float | The maintenance margin rate for market Buy orders.  
MarginMaintenanceSell | Float | The maintenance margin rate for market Sell orders.  
MarginMaintenanceBuyLimit | Float | The maintenance margin rate for Buy Limit orders.  
MarginMaintenanceSellLimit | Float | The maintenance margin rate for Sell Limit orders.  
MarginMaintenanceBuyStop | Float | The maintenance margin rate for Buy Stop orders.  
MarginMaintenanceSellStop | Float | The maintenance margin rate for Sell Stop orders.  
MarginMaintenanceBuyStopLimit | Float | The maintenance margin rate for Buy Stop Limit orders.  
MarginMaintenanceSellStopLimit | Float | The maintenance margin rate for Sell Stop Limit orders.  
MarginHedged | Float | The hedged margin value.  
SwapMode | Integer | The swap calculation mode for a symbol. Passed in a value of the [EnSwapMode (#enswapmode)](mt5-symbols/Enumerations.md#enswapmode) enumeration.  
SwapLong | Float | The swap size for long positions.  
SwapShort | Float | The swap size for short positions.  
SwapYearDay | Integer | The number of days in a year used in calculating swap percent. Passed by the [EnSwapDays (#enswapdays)](mt5-symbols/Enumerations.md#enswapdays) enumeration value.  
SwapFlags | Integer | Additional swap settings. Passed by the [EnSwapFlags (#enswapflags)](mt5-symbols/Enumerations.md#enswapflags) enumeration value.  
SwapRateSunday | Float | Swap multiplier for Sundays.  
SwapRateMonday | Float | Swap multiplier for Mondays.  
SwapRateTuesday | Float | Swap multiplier for Tuesdays.  
SwapRateWednesday | Float | Swap multiplier for Wednesdays.  
SwapRateThursday | Float | Swap multiplier for Thursdays.  
SwapRateFriday | Float | Swap multiplier for Fridays.  
SwapRateSaturday | Float | Swap multiplier for Saturdays.  
TimeStart | Integer | The start date of trading for a symbol. It is considered that there is no time limitation for trading by a symbol if both TimeStart and TimeExpiration are equal to 0.  
TimeExpiration | Integer | The date of trading expiration for a symbol. It is considered that there is no time limitation for trading by a symbol if both TimeStart and TimeExpiration are equal to 0.  
REFlags | Integer | The request execution flags. Passed as a value of the [EnRequestsFlags (#enrequestflags)](mt5-symbols/Enumerations.md#enrequestflags) enumeration (sum of values of appropriate flags).  
RETimeout | Integer | Time in seconds during which the price issued by a dealer in the request execution mode is valid.  
IECheckMode | Integer | Check mode for instant execution. Passed in a value of the [EnInstantMode (#eninstantmode)](mt5-symbols/Enumerations.md#eninstantmode) enumeration.  
IETimeout | Integer | The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price.  
IESlipProfit | Integer | The maximum allowed slippage in the profitable direction during instant execution.  
IESlipLosing | Integer | The maximum allowed slippage in the loss direction during instant execution.  
IEVolumeMax | Integer | The maximum volume of a trade operation that can be executed in the instant execution mode. One unit corresponds to 1/10000 lot.  
IEVolumeMaxExt | Integer | The maximum volume (with extended accuracy) of a trade operation that can be executed in the instant execution mode. One unit corresponds to 1/100000000 lot.  
PriceSettle | Float | The clearing price of the previous session.  
PriceLimitMax | Float | The maximum allowed price of the symbol.  
PriceLimitMin | Float | The minimum allowed price of the symbol.  
TradeFlags | Integer | The trade flags of the symbol. Passed in a value of the [EnTradeFlags (#entradeflags)](mt5-symbols/Enumerations.md#entradeflags) enumeration.  
OrderFlags | Integer | The flags of order types that are allowed for the symbol. Passed in a value of the [EnOrderFlags (#enorderflags)](mt5-symbols/Enumerations.md#enorderflags) enumeration (sum of values of appropriate flags).  
MarginRateLiquidity | Float | The liquidity rate of the symbol. It determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).  
MarginRateCurrency | Float | The margin currency rate (rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble).  
FaceValue | Float | The face value of a bond.  
AccruedInterest | Float | The accrued interest of a bond.  
SpliceType | Integer | The futures contract splicing type.  
SpliceTimeType | Integer | The date of splicing of the futures contracts.  
SpliceTimeDays | Integer | The offset of splicing of the futures contracts.  
OptionMode | Integer | [Option](../../../Platform-Setup/Symbols/Symbol-Settings/Options.md) type and style:

  * 0 means a European call option
  * 1 means a European put option
  * 2 means an American call option
  * 3 means an American put option

  
PriceStrike | Float | The price, at which an option gives the right to buy or sell an asset (the strike price).  
FilterGap | Integer | The difference between the previous and the next quote, starting from which a [gap (#gap)](../../../Platform-Setup/Symbols/Symbol-Settings/Quotes.md#gap) is considered to be formed.  
FilterGapTicks | Integer | The number of ticks for disabling the [gap mode (#gap)](../../../Platform-Setup/Symbols/Symbol-Settings/Quotes.md#gap). If no new gap occurs within the specified number of quotes, the mode is disabled.  
TickChartMode | Integer | The mode of creation of the symbol chart: 0 — using the Bid price, 1 — using the Last price.
