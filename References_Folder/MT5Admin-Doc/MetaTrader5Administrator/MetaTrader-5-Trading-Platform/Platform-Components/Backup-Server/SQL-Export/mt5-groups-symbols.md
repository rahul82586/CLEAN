[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_groups_symbols

[Previous](mt5-groups/Enumerations.md) | [Next](mt5-commissions.md)

# mt5_groups_symbols

Individual [symbol settings for groups](../../../Platform-Setup/Groups/Group-Symbol-Settings.md) are exported to the table. The table contains the following fields:

Name | Type | Description  
Symbol_ID | Integer | Primary key. Unique symbol ID for the group.  
Group_ID | Integer | [ID of the group](mt5-groups.md), to which symbol settings are applied.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
Path | String | The path to a symbol or group of symbols that are subject to the special group settings.  
TradeMode | Integer | The symbol trading mode for the group. Passed in a value of the [EnTradeMode (#entrademode)](mt5-symbols/Enumerations.md#entrademode) enumeration.  
ExecMode | Integer | The symbol execution mode for the group. Passed in a value of the [EnExecutionMode (#enexecutionmode)](mt5-symbols/Enumerations.md#enexecutionmode) enumeration.  
FillFlags | Integer | Types of filling allowed for the symbol in this group. Passed as a value of the [EnFillingFlags (#enfillingflags)](mt5-symbols/Enumerations.md#enfillingflags) enumeration (sum of values of appropriate flags).  
ExpirFlags | Integer | Types of order expiration allowed for the symbol in this group. Passed as a value of the [EnExpirationFlags (#enexpirationflags)](mt5-symbols/Enumerations.md#enexpirationflags) enumeration (sum of values of appropriate flags).  
SpreadDiff | Integer | Difference between the symbol spread for the group and the default spread.  
SpreadDiffBalance | Integer | The balance of spread difference set for the group. The balance of spread difference is set a shift from the equal distribution of the spread difference value between Bid and Ask prices. For example, if the spread difference is equal to 4 and it is distributed as -2 Bid/+2 Ask, then the balance of spread difference value is 0. The -3 Bid/+1 Ask ratio corresponds to value -1, ratio -1 Bid/+3 Ask corresponds to value 1.  
StopsLevel | Integer | The price band, within which the group is not allowed to place stop orders for a symbol.  
FreezeLevel | Integer | The price band, within which it is not allowed to modify orders and positions for the group.  
VolumeMin | Integer | The minimum volume of trade operations for a symbol for the group. One unit corresponds to 1/10000 lot.  
VolumeMinExt | Integer | The minimum volume (with extended accuracy) of trade operations for a symbol for the group. One unit corresponds to 1/100000000 lot.  
VolumeMax | Integer | The maximum volume of trade operations for a symbol for the group. One unit corresponds to 1/10000 lot.  
VolumeMaxExt | Integer | The maximum volume (with extended accuracy) of trade operations for a symbol for the group. One unit corresponds to 1/100000000 lot.  
VolumeStep | Integer | The step of change of trade operations volume for a symbol for the group. One unit corresponds to 1/10000 lot.  
VolumeStepExt | Integer | The step of change of trade operations volume (with extended accuracy) for a symbol for the group. One unit corresponds to 1/100000000 lot.  
VolumeLimit | Integer | The maximum allowed aggregate volume of positions and orders for a symbol in one direction for this group. One unit corresponds to 1/10000 lot.  
VolumeLimitExt | Integer | The maximum aggregate volume (with extended accuracy) of positions and orders for a symbol for this group. One unit corresponds to 1/100000000 lot.  
MarginFlags | Integer | The additional modes of symbol margin checking for the group. Passed in a value of the [EnMarginFlags (#enmarginflags)](mt5-symbols/Enumerations.md#enmarginflags) enumeration.  
MarginInitial | Float | The size of initial symbol margin for the group.  
MarginMaintenance | Float | The size of symbol maintenance margin for the group.  
MarginLong | Float | The group margin ratio for long positions and orders for a symbol.  
MarginShort | Float | The group margin ratio for short positions and orders for a symbol.  
MarginLimit | Float | The group margin ratio of limit orders for a symbol.  
MarginStop | Float | The group margin ratio of stop orders for a symbol.  
MarginStopLimit | Float | The group margin ratio for stop-limit orders for a symbol.  
MarginHedged | Float | The hedged margin value.  
SwapMode | Integer | The swap calculation mode for a certain symbol for the group. Passed in a value of the [EnSwapMode (#enswapmode)](mt5-symbols/Enumerations.md#enswapmode) enumeration.  
SwapLong | Float | The long position swap for a symbol for the group.  
SwapShort | Integer | The short position swap for a symbol for the group.  
SwapYearDays | Integer | The number of days in a year used in calculating swap percent for a given group. Passed by the [EnSwapDays (#enswapdays)](mt5-symbols/Enumerations.md#enswapdays) enumeration value.  
SwapFlags | Integer | Additional swap settings by symbol for the given group. Passed by the [EnSwapFlags (#enswapflags)](mt5-symbols/Enumerations.md#enswapflags) enumeration value.  
SwapRateSunday | Float | Sunday swap multiplier in symbol settings for the given group.  
SwapRateMonday | Float | Monday swap multiplier in symbol settings for the given group.  
SwapRateTuesday | Float | Tuesday swap multiplier in symbol settings for the given group.  
SwapRateWednesday | Float | Wednesday swap multiplier in symbol settings for the given group.  
SwapRateThursday | Float | Thursday swap multiplier in symbol settings for the given group.  
SwapRateFriday | Float | Friday swap multiplier in symbol settings for the given group.  
SwapRateSaturday | Float | Saturday swap multiplier in symbol settings for the given group.  
RETimeout | Integer | Time in seconds during which the price issued by a dealer in the request execution mode is valid.  
IECheckMode | Integer | The mode of checking during instant execution set for a group. Passed in a value of the [EnInstantMode (#eninstantmode)](mt5-symbols/Enumerations.md#eninstantmode) enumeration.  
IETimeout | Integer | The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price. The timeout is specified in seconds.  
IESlipProfit | Integer | The maximum allowed slippage in the profitable direction during instant execution.  
IESlipLosing | Integer | The maximum allowed slippage in the loss direction during instant execution.  
IEVolumeMax | Integer | The maximum volume of a trade operation that can be executed in the instant execution mode. One unit corresponds to 1/10000 lot.  
IEVolumeMaxExt | Integer | The maximum volume (with extended accuracy) of a trade operation that can be executed in the instant execution mode. One unit corresponds to 1/100000000 lot.  
OrderFlags | Integer | The flags of order types that are allowed for the symbol. Passed in a value of the [EnOrderFlags (#enorderflags)](mt5-symbols/Enumerations.md#enorderflags) enumeration (sum of values of appropriate flags).  
MarginRateLiquidity | Float | The liquidity rate of the symbol for the group. It determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).  
REFlags | Integer | The flags of request execution for the group.  
  
> NULL value in the fields beginning from TradeMode means that the appropriate setting is inherited from the [base symbol](mt5-symbols.md).
