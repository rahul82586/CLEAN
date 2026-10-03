[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeBuyCoverageExt

[Previous](VolumeBuyCoverage.md) | [Next](VolumeSellClients.md)

# IMTSummary::VolumeBuyCoverageExt

Gets the total volume of client hedging positions, with an extended accuracy. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeBuyCoverageExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeBuyCoverageExt()

### Return Value

The total volume of hedging buy positions. The volume is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

Positions on all hedging accounts from all coverage* groups are counted.
