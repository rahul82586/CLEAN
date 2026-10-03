[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeBuyCoverage

[Previous](VolumeBuyClientsExt.md) | [Next](VolumeBuyCoverageExt.md)

# IMTSummary::VolumeBuyCoverage

Gets the total volume of hedging buy positions. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeBuyCoverage()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeBuyCoverage()

### Return Value

The total volume of open hedging Buy positions on the symbol. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
