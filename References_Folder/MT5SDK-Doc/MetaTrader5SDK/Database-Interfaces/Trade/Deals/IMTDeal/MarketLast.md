[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / MarketLast

[Previous](MarketAsk.md) | [Next](ModificationFlags.md)

# IMTDeal::MarketLast

Get the market Last price as at the time of deal execution by the server.

C++
    
    
    double  IMTDeal::MarketLast()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.MarketLast()

### Return Value

The market Last price as at the time of deal execution by the server.

### Note

This field stores the market price not as at the time when the request is placed in the terminal, but as at the time when the deal is executed by the trade server.
