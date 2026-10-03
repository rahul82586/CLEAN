[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeBuyClientsExt

[Previous](VolumeBuyClients.md) | [Next](VolumeBuyCoverage.md)

# IMTSummary::VolumeBuyClientsExt

Gets the total volume of client buy positions, with an extended accuracy. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeBuyClientsExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeBuyClientsExt()

### Return Value

The total volume of client buy positions (in lots). The volume is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTSummary::VolumeBuyClients](VolumeBuyClients.md) method.
