[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeSellClientsExt

[Previous](VolumeSellClients.md) | [Next](VolumeSellCoverage.md)

# IMTSummary::VolumeSellClientsExt

Gets the total volume of client sell positions, with an extended accuracy. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeSellClientsExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeSellClientsExt()

### Return Value

The total volume of client sell positions. The volume is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTSummary::VolumeSellClients](VolumeSellClients.md) method.
