[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultMarketAsk

[Previous](Requests-ResultMarketBid.md) | [Next](Requests-ResultMarketLast.md)

# IMTRequest::ResultMarketAsk

Get the market Ask price when a request is processed by the server.

C++
    
    
    double  IMTRequest::ResultMarketAsk()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.ResultMarketAsk()

### Return Value

The market Ask price when a request is processed by the server.

### Note

The market price is stored in this field at the moment of receiving and processing a request by the trade server rather than setting a request in the terminal.
