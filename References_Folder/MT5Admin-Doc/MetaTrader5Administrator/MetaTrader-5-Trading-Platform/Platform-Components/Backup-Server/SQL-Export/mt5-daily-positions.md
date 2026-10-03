[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_daily_positions

[Previous](mt5-daily-orders.md) | [Next](mt5-holidays.md)

# mt5_daily_positions

Data on the end-of-day status of positions is exported to this table. The table is generated only if the [backup server settings (#sql-settings)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#sql-settings) have the "Export additional columns for daily reports \ Orders from daily reports" option enabled. The table contains the following fields:

Name | Type | Description  
Datetime | DateTime | The date for which the position status was saved.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
Login | Integer | The login of the client, to whom the trade position belongs.  
Symbol | String | The symbol of a trade position.  
Action | Integer | Position type. Passed in a value of the [EnPositionAction (#enpositionaction)](mt5-positions/Enumerations.md#enpositionaction) enumeration.  
Digits | Integer | The number of decimal places in the price of a position.  
DigitsCurrency | Integer | The number of decimal places the deposit currency of the client who has opened the position.  
Reason | Integer | The reason for position opening. Passed in a value of the [EnPositionReason (#enpositionreason)](mt5-positions/Enumerations.md#enpositionreason) enumeration.  
ContractSize | Float | The contract size of the symbol, for which a position is opened.  
Position | Integer | The ticket (unique identifier) of a trade position in a MetaTrader 5 platform.  
ExternalID | String | The position ticket (unique number) in an external trading system.  
TimeCreate | DateTime | Time of position creation, in seconds that have elapsed since 01.01.1970.  
TimeUpdate | DateTime | Time of the last modification of a position, in seconds that have elapsed since 01.01.1970. The modification time of a position is the time of the last modification of its volume. Virtually, it is the time of the last deal performed by the financial instrument that corresponds to that position.  
TimeCreateMsc | DateTime | Position generation time in the YYYY-MM-DD HH:MM:SS.MS format.  
TimeUpdateMsc | DateTime | Time of a trading position last change in the YYYY-MM-DD HH:MM:SS.MS format. The modification time of a position is the time of the last modification of its volume. Virtually, it is the time of the last deal performed by the financial instrument that corresponds to that position.  
PriceOpen | Float | The weighted average open price of a position. Calculated by the following formula: (price of deal 1 * volume of deal 1 1 + ... + price of deal N * volume of deal N) / (volume of deal 1 + ... + volume of deal N).  
PriceCurrent | Float | The current price of the symbol, for which a trade position has been opened.  
PriceSL | Float | The Stop Loss level of a trade position.  
PriceTP | Float | The Take Profit level of a trade position.  
Volume | Integer | The volume of a trade position. One unit corresponds to 1/10000 lot.  
VolumeExt | Integer | The trade position volume with an extended accuracy. One unit corresponds to 1/100000000 lot.  
Profit | Float | Returns of a trade position in deposit currency.  
Storage | Float | The swap size for a position in deposit currency.  
RateProfit | Float | The exchange rate of the profit currency of a position to the deposit currency of a client group.  
RateMargin | Float | The exchange rate of the margin currency of a position to the client's deposit currency.  
ExpertID | Integer | The ID of the Expert Advisor that has opened the position.  
ExpertPositionID | Integer | Position ID.  
Comment | String | A comment to a position.  
Dealer | Integer | The login of a dealer, who has processed an order, which opened the position.  
ActivationMode | Integer | Position activation type. Passed in a value of the [EnActivation (#enactivation)](mt5-positions/Enumerations.md#enactivation) enumeration.  
ActivationTime | DateTime | Position activation time in the YYYY-MM-DD HH:MM:SS.MS format.  
ActivationPrice | Float | Position activation price.  
ActivationFlags | Integer | Position activation flags. Passed as a value of the [EnTradeActivationFlags (#entradeactivationflags)](mt5-positions/Enumerations.md#entradeactivationflags) enumeration (sum of values of appropriate flags).  
ApiData | String | User data which can be added via MetaTrader 5 API. Sample user data entry: [{pos:0,app_id:1,valInt:500,valUInt:500,valDbl:0.00000000}]. It specifies the user data index, the ID of the application that added it, as well as the data of three types: Int, UInt and double. The string may contain up to 16 such entries.
