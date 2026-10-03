[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeSellClients

[Previous](VolumeBuyCoverageExt.md) | [Next](VolumeSellClientsExt.md)

# IMTSummary::VolumeSellClients

Gets the total volume of client sell positions. The volume of open positions of the [selected symbol](Symbol.md) is counted.

C++
    
    
    UINT64  IMTSummary::VolumeSellClients()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSummary.VolumeSellClients()

### Return Value

The total volume of clients' open Sell positions on the symbol. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).
