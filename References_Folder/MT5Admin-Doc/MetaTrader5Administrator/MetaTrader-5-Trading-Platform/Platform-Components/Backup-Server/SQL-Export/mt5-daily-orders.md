[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_daily_orders

[Previous](mt5-daily.md) | [Next](mt5-daily-positions.md)

# mt5_daily_orders

Data on the end-of-day status of open [orders](../../../Platform-Setup/Orders.md) is exported to this table. The table is generated only if the [backup server settings (#sql-settings)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#sql-settings) have the "Export additional columns for daily reports \ Orders from daily reports" option enabled. The table contains the following fields:

Name | Type | Description  
Datetime | DateTime | The date for which the order status was saved.  
Order | Integer | Primary key. Order ticket.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
ExternalID | String | The order ID in external trading systems.  
Login | Integer | The login of the client, to whom the order belongs.  
Dealer | Integer | The login of a dealer, who has processed an order.  
Symbol | String | The symbol of an order.  
Digits | Integer | The number of decimal places in the price of an order.  
DigitsCurrency | Integer | The number of decimal places the deposit currency of the client who has placed the order.  
ContractSize | Float  | The contract size of the symbol, for which an order was placed.  
State | Integer | The current state of an order. Passed as a value of the [EnOrderMode (#enorderstate)](mt5-orders/Enumerations.md#enorderstate) enumeration.  
Reason | Integer | The reason for placing the order. Passed as a value of the [EnOrderReason (#enorderreason)](mt5-orders/Enumerations.md#enorderreason) enumeration.  
TimeSetup | DateTime | Order placement time in the YYYY-MM-DD HH:MM:SS format.  
TimeSetupMsc | DateTime | Order placement time in milliseconds in the YYYY-MM-DD HH:MM:SS.MS format.  
TimeExpiration | DateTime | Order expiration time in the YYYY-MM-DD HH:MM:SS format.  
TimeDone | DateTime | Order execution time in the YYYY-MM-DD HH:MM:SS format.  
TimeDoneMsc | DateTime | Order execution time in milliseconds in the YYYY-MM-DD HH:MM:SS.MS format.  
ModifyFlags | Integer | The order modification flags. Passed as a value of the [EnTradeModifyFlags (#entrademodifyflags)](mt5-orders/Enumerations.md#entrademodifyflags) enumeration (sum of values of appropriate flags).  
Type | Integer | Order type. Passed as a value of the [EnOrderType (#enordertype)](mt5-orders/Enumerations.md#enordertype) enumeration.  
TypeFill | Integer | Order filling type. Passed as a value of the [EnOrderFilling (#enorderfilling)](mt5-orders/Enumerations.md#enorderfilling) enumeration.  
TypeTime | Integer | Order expiration type. Passed in a value of the [EnOrderTime (#enordertime)](mt5-orders/Enumerations.md#enordertime) enumeration.  
PriceOrder | Float  | Order price.  
PriceTrigger | Float | The order triggering price.  
PriceCurrent | Float | The current price of the symbol, for which an order has been placed.  
PriceSL | Float | The Stop Loss level of an order.  
PriceTP | Float | The Take Profit level of an order.  
VolumeInitial | Integer | The initial order volume. One unit corresponds to 1/10000 lot.  
VolumeInitialExt | Integer | The initial order volume with an extended accuracy. One unit corresponds to 1/100000000 lot.  
VolumeCurrent | Integer | The current unfilled volume of an order. One unit corresponds to 1/10000 lot.  
VolumeCurrentExt | Integer | The current unfilled order volume with an extended accuracy. One unit corresponds to 1/100000000 lot.  
ExpertID | Integer | The ID of the Expert Advisor that has placed the order.  
PositionID | Integer | The position ID (ticket) set in the order.  
PositionByID | Integer | The opposite position ID (ticket) set in the order. The property is set for Close By operations ([OP_CLOSE_BY (#enordertype)](mt5-orders/Enumerations.md#enordertype)). The ticket of the position that is closed by the opposite one is set in PositionID.  
Comment | String | A comment to an order.  
ActivationMode | Integer | Order activation type. Passed in a value of the [EnOrderActivation (#enorderactivation)](mt5-orders/Enumerations.md#enorderactivation) enumeration.  
ActivationTime | DateTime | Order activation time in the YYYY-MM-DD HH:MM:SS format.  
ActivationPrice | Float | The price, at which the order was activated.  
ActivationFlags | Integer | Order activation flags. Passed as a value of the [EnTradeActivationFlags (#entradeactivationflags)](mt5-orders/Enumerations.md#entradeactivationflags) enumeration (sum of values of appropriate flags).  
RateMargin | Float | The rate of conversion of the margin currency of the symbol to the deposit currency of the user, which is used when calculating the margin requirements for the order.  
ApiData | String | User data which can be added via MetaTrader 5 API. Sample user data entry: [{pos:0,app_id:1,valInt:500,valUInt:500,valDbl:0.00000000}]. It specifies the user data index, the ID of the application that added it, as well as the data of three types: Int, UInt and double. The string may contain up to 16 such entries.
