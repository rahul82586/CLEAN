[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / MarketAsk

[Previous](MarketBid.md) | [Next](MarketLast.md)

# IMTDeal::MarketAsk

Get the market Ask price as at the time of deal execution by the server.

C++
    
    
    double  IMTDeal::MarketAsk()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.MarketAsk()

### Return Value

The market Ask price as at the time of deal execution by the server.

### Note

This field stores the market price not as at the time when the request is placed in the terminal, but as at the time when the deal is executed by the trade server.
