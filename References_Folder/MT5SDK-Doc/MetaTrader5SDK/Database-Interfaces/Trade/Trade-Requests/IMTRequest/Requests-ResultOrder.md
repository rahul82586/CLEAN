[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultOrder

[Previous](Requests-ResultDeal.md) | [Next](Requests-ResultVolume.md)

# IMTRequest::ResultOrder

Get the number of the [order](../../Orders.md) formed as a result of request execution.

C++
    
    
    UINT64  IMTRequest::ResultOrder()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.ResultOrder()

### Return Value

The number of the order that is formed as a result of request execution.

  * [IMTRequest::Type](Requests-Type.md)
  * [IMTRequest::Action](Requests-Action.md)
  * [IMTRequest::ResultRetcode](Requests-ResultRetcode.md)



### Note

This field is used in cases where after the request execution a new order is formed ([IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration):

  * TA_REQUEST — a request for placing a market order in the request execution mode.
  * TA_INSTANT — a trade operation in the instant execution mode.
  * TA_MARKET — a trade operation in the market execution mode.
  * TA_EXCHANGE — a trade operation in the exchange execution mode.
  * TA_PENDING — a request to place a pending order
  * TA_ACTIVATE_SL — closing a position after reaching the Stop Loss level.
  * TA_ACTIVATE_TP — closing a position after reaching the Take Profit level.
  * TA_STOPOUT_POSITION — forced closure of a position when reaching the Stop Out level.
  * TA_DEALER_POS_EXECUTE — execution of a trade operation by a dealer.
  * TA_DEALER_ORD_PENDING — placing a pending order by a dealer.


