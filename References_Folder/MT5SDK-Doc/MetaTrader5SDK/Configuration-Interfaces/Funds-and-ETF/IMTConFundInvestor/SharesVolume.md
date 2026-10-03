[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundInvestor](../IMTConFundInvestor.md) / SharesVolume

[Previous](Name.md) | [Next](../IMTConFundSink.md)

# IMTConFundInvestor::SharesVolume

Get the investor's share size.

C++
    
    
    UINT64  IMTConFundInvestor::SharesVolume()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFundInvestor.SharesVolume()

### Return Value

The investor's share size. Corresponds to the size of the fund symbol position ([IMTPosition::Volume](../../../Database-Interfaces/Trade/Positions/IMTPosition/VolumeExt.md)) opened on the investor's account.
