[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultMarketLast

[Previous](Requests-ResultMarketAsk.md) | [Next](Requests-ResultComment.md)

# IMTRequest::ResultMarketLast

Get the market Last price when a request is processed by the server.

C++
    
    
    double  IMTRequest::ResultMarketLast()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.ResultMarketLast()

### Return Value

The market Last price when a request is processed by the server.

### Note

The market price is stored in this field at the moment of receiving and processing a request by the trade server rather than setting a request in the terminal.
