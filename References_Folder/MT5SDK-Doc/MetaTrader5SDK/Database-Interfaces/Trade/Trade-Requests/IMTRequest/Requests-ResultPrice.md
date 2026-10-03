[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultPrice

[Previous](Requests-ResultVolumeExt.md) | [Next](Requests-ResultDealerBid.md)

# IMTRequest::ResultPrice

Get the price used by a dealer to confirm a request.

C++
    
    
    double  IMTRequest::ResultPrice()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.ResultPrice()

### Return Value

The price at which the dealer has confirmed the request.

The return value can be 0 if the request is not processed, or if price is not specified as a result of its confirmation.

### Note

This field is used in cases where a dealer specified a price when processing a request ([IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration):

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


