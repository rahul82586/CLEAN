[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / PriceSellCoverage

[Previous](PriceSellClients.md) | [Next](ProfitClients.md)

# IMTSummary::PriceSellCoverage

Gets the weighted average open price of hedging Sell positions.

C++
    
    
    double  IMTSummary::PriceSellCoverage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.PriceSellCoverage()

### Return Value

The weighted average open price of hedging Sell positions.

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
