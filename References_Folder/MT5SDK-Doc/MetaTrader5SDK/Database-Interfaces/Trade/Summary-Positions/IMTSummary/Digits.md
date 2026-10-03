[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / Digits

[Previous](Symbol.md) | [Next](PositionClients.md)

# IMTSummary::Digits

Gets the number of digits in the weighted average prices of [client](PriceBuyClients.md) and [hedging](PriceBuyCoverage.md) Buy and Sell positions.

C++
    
    
    UINT  IMTSummary::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTSummary.Digits()

### Return Value

The number of digits in the weighted average prices of client and hedging Buy and Sell positions.
