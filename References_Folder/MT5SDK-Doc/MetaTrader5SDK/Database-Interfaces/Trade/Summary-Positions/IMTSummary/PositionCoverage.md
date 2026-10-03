[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / PositionCoverage

[Previous](PositionClients.md) | [Next](VolumeBuyClients.md)

# IMTSummary::PositionCoverage

Gets the number of hedging positions on the selected symbol.

C++
    
    
    UINT  IMTSummary::PositionCoverage()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTSummary.PositionCoverage()

### Return Value

The number of hedging positions on the selected symbol.

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
