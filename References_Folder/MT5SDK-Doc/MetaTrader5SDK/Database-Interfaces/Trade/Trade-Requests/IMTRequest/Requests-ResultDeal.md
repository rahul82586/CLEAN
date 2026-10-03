[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultDeal

[Previous](Requests-ResultDealer.md) | [Next](Requests-ResultOrder.md)

# IMTRequest::ResultDeal

Get the number of the [deal](../../Deals.md) formed as a result of request execution.

C++
    
    
    UINT64  IMTRequest::ResultDeal()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.ResultDeal()

### Return Value

The number of the deal that is formed as a result of request execution.

The return value can be 0 if the request is not processed, or if deals are not conducted as a result of its execution. To check these situations, use the following methods:

  * [IMTRequest::Type](Requests-Type.md)
  * [IMTRequest::Action](Requests-Action.md)
  * [IMTRequest::ResultRetcode](Requests-ResultRetcode.md)



### Note

This field is used in cases where a new deal is formed after the request execution ([IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration):

  * TA_REQUEST — a request for placing a market order in the request execution mode.
  * TA_INSTANT — a trade operation in the instant execution mode.
  * TA_MARKET — a trade operation in the market execution mode.
  * TA_EXCHANGE — a trade operation in the exchange execution mode.
  * TA_ACTIVATE — order activation.
  * TA_ACTIVATE_SL — closing a position after reaching the Stop Loss level.
  * TA_ACTIVATE_TP — closing a position after reaching the Take Profit level.
  * TA_STOPOUT_POSITION — forced closure of a position when reaching the Stop Out level.
  * TA_DEALER_POS_EXECUTE — execution of a trade operation by a dealer.
  * TA_DEALER_ORD_ACTIVATE — order activation by a dealer.
  * TA_DEALER_BALANCE — conducting a balance operation by a dealer.


