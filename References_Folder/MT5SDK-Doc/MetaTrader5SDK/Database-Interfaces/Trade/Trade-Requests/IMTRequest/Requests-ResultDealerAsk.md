[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultDealerAsk

[Previous](Requests-ResultDealerBid.md) | [Next](Requests-ResultDealerLast.md)

# IMTRequest::ResultDealerAsk

Get the Ask price confirmed by a dealer for this request.

C++
    
    
    double  IMTRequest::ResultDealerAsk()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.ResultDealerAsk()

### Return Value

The Ask price confirmed by a dealer for this request.

### Note

This field is used in cases where the dealer specifies new values of market prices while processing a request [IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration):

  * TA_PRICE — when processing a request of new prices for Request Execution.
  * TA_INSTANT — when requoting a deal request for Instant Execution.


