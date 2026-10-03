[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultDealerLast

[Previous](Requests-ResultDealerAsk.md) | [Next](Requests-ResultMarketBid.md)

# IMTRequest::ResultDealerLast

Get the Last price confirmed by a dealer for this request.

C++
    
    
    double  IMTRequest::ResultDealerLast()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.ResultDealerLast()

### Return Value

The Last price confirmed by a dealer for this request.

### Note

This field is used in cases where the dealer specifies new values of market prices while processing a request [IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration):

  * TA_PRICE — when processing a request of new prices for Request Execution.
  * TA_INSTANT — when requoting a deal request for Instant Execution.


