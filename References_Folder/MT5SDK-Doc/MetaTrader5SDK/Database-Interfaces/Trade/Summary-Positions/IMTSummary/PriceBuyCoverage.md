[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / PriceBuyCoverage

[Previous](PriceBuyClients.md) | [Next](PriceSellClients.md)

# IMTSummary::PriceBuyCoverage

Gets the weighted average open price of hedging Buy positions.

C++
    
    
    double  IMTSummary::PriceBuyCoverage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.PriceBuyCoverage()

### Return Value

The weighted average open price of hedging Buy positions.

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
