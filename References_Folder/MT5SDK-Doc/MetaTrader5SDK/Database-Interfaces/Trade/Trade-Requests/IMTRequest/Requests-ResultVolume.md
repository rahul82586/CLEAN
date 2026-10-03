[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultVolume

[Previous](Requests-ResultOrder.md) | [Next](Requests-ResultVolumeExt.md)

# IMTRequest::ResultVolume

Gets the deal volume confirmed by a dealer for this request.

C++
    
    
    UINT64  IMTRequest::ResultVolume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.ResultVolume()

### Return Value

The volume of a deal confirmed by a dealer for this request, in the UINT64 format (one unit corresponds to 1/10,000 of the lot).

### Note

This field is used in cases where a dealer specified a volume when processing a request ([IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration):

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


