[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultMarketBid

[Previous](Requests-ResultDealerLast.md) | [Next](Requests-ResultMarketAsk.md)

# IMTRequest::ResultMarketBid

Get the market Bid price when a request is processed by the server.

C++
    
    
    double  IMTRequest::ResultMarketBid()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.ResultMarketBid()

### Return Value

The market Bid price when a request is processed by the server.

### Note

The market price is stored in this field at the moment of receiving and processing a request by the trade server rather than setting a request in the terminal.
