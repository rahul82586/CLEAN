[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Data Structure

[Previous](../Orders.md) | [Next](Get-Open-by-Ticket.md)

# Data Structure

Information about orders is passed in the JSON format as an additional body of response commands [ORDER_GET](Get-Open-by-Ticket.md), [ORDER_GET_PAGE](Get-Open-Paged.md), [HISTORY_GET](Get-Closed-by-Ticket.md) and [HISTORY_GET_PAGE](Get-Closed-Paged.md). Information about an order contains the following parameters:

Option Field | Type | Description  
Order | Integer | Order ticket.  
ExternalID | String | The order ID in external trading systems.  
Login | Integer | The login of the client, to whom the order belongs.  
Dealer | Integer | The login of a dealer, who has processed an order.  
Symbol | String | Order symbol.  
Digits | Integer | The number of decimal places in the price of an order.  
DigitsCurrency | Integer | The number of decimal places the deposit currency of the client who has placed the order.  
ContractSize | Float | The contract size of the symbol, for which an order was placed.  
State | Integer | The current state of an order. Passed as a value of the [EnOrderState (#enorderstate)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate) enumeration.  
Reason | Integer | The reason for performing a deal. Passed as a value of the [EnOrderReason (#enorderreason)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderreason) enumeration.  
TimeSetup | Integer | The time of order placing in seconds that have elapsed since 01.01.1970.  
TimeExpiration | Integer | The time of order expiration in seconds that have elapsed since 01.01.1970.  
TimeDone | Integer | The time of order execution in seconds that have elapsed since 01.01.1970.  
Type | Integer | Order type. Passed as a value of the [EnOrderType (#enordertype)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype) enumeration.  
TypeFill | Integer | Order filling type. Passed as a value of the [EnOrderFilling (#enorderfilling)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.  
TypeTime | Integer | Order expiration type. Passed as a value of the [EnOrderTime (#enordertime)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertime) enumeration.  
PriceOrder | Float | Order price.  
PriceTrigger | Float | The price, at which a Limit order is placed when the Stop Limit order triggers.  
PriceCurrent | Float | The current price of the symbol, for which an order has been placed.  
PriceSL | Float | The Stop Loss level of an order.  
PriceTP | Float | The Take Profit level of an order.  
VolumeInitial | Integer | The initial order volume. One unit corresponds to 1/10000 lot.  
VolumeInitialExt | Integer | The initial order volume with an extended accuracy. One unit corresponds to 1/100000000 lot.  
VolumeCurrent | Integer | The current unfilled volume of an order. One unit corresponds to 1/10000 lot.  
VolumeCurrentExt | Integer | The current unfilled volume of an order with an extended accuracy. One unit corresponds to 1/100000000 lot.  
ExpertID | Integer | The ID of the Expert Advisor that has placed the order.  
PositionID | Integer | The position ID (ticket) set in the order.  
PositionByID | Integer | The opposite position ID (ticket) set in the order. The property is set for Close By operations ([OP_CLOSE_BY (#enordertype)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype)). The ticket of the position that is closed by the opposite one is set in PositionID.  
Comment | String | Comment to an order.  
ActivationMode | Integer | Order activation type. Passed as a value of the [EnOrderActivation (#enorderactivation)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderactivation) enumeration.  
ActivationTime | Integer | The time of order activation in seconds that have elapsed since 01.01.1970.  
ActivationPrice | Float | The price, at which the order was activated.  
ActivationFlags | Integer | Order activation flags. Passed as a value of the [EnTradeActivationFlags (#entradeactivationflags)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#entradeactivationflags) enumeration (sum of values of appropriate flags).  
TimeSetupMsc | Integer | The order placing time in milliseconds.  
TimeDoneMsc | Integer | The order execution time in milliseconds.  
RateMargin | Float | The rate of conversion of the margin currency of the symbol to the deposit currency of the user, which is used when calculating the margin requirements for the order.  
ModificationFlags | Integer | The order modification flags. Passed as a value of the [EnTradeModifyFlags (#entrademodifyflags)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#entrademodifyflags) enumeration (sum of values of appropriate flags).
