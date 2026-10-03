[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / MarketBid

[Previous](PriceGatewaySet.md) | [Next](MarketAsk.md)

# IMTDeal::MarketBid

Get the market Bid price as at the time of deal execution by the server.

C++
    
    
    double  IMTDeal::MarketBid()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.MarketBid()

### Return Value

The market Bid price as at the time of deal execution by the server.

### Note

This field stores the market price not as at the time when the request is placed in the terminal, but as at the time when the deal is executed by the trade server.
