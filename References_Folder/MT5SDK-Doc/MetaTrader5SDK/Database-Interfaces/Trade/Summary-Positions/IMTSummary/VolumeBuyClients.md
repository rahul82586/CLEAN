[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeBuyClients

[Previous](PositionCoverage.md) | [Next](VolumeBuyClientsExt.md)

# IMTSummary::VolumeBuyClients

Gets the total volume of client buy positions. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeBuyClients()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeBuyClients()

### Return Value

The total volume of clients' open Buy positions on the symbol (in lots). The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTSummary::VolumeBuyClientsExt](VolumeBuyClientsExt.md) method.
