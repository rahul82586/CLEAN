[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / VolumeNet

[Previous](VolumeSellCoverageExt.md) | [Next](PriceBuyClients.md)

# IMTSummary::VolumeNet

Gets the differences (net total) between the volume of clients' [Buy](VolumeBuyClients.md) and [Sell](VolumeSellClients.md) positions, while the appropriate amount on hedge accounts is deducted from the volume of clients' Buy or Sell positions ([IMTSummary::VolumeBuyCoverage](VolumeBuyCoverage.md) and [IMTSummary::VolumeSellCoverage](VolumeSellCoverage.md)).

C++
    
    
    double  IMTSummary::VolumeNet()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.VolumeNet()

### Return Value

The difference between clients' Buy and Sell positions after the deduction of appropriate position volumes on hedging accounts.

### Note

Hedging positions of all accounts from all coverage* groups are taken into account.
