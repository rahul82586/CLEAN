[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeSellCoverage

[Previous](VolumeSellClientsExt.md) | [Next](VolumeSellCoverageExt.md)

# IMTSummary::VolumeSellCoverage

Gets the total volume of hedging sell positions. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeSellCoverage()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeSellCoverage()

### Return Value

The total volume of open hedging Sell positions on the symbol. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
