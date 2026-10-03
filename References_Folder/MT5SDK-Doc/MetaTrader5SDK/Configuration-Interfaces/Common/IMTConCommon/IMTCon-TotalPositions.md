[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon TotalPositions

[Previous](IMTCon-TotalOrdersHistory.md) | [Next](IMTCon-AccountURL.md)

# IMTConCommon::TotalPositions

Get the total number of [positions](../../../Database-Interfaces/Trade/Positions.md) in the whole trading platform (on all trade server).

C++
    
    
    UINT  IMTConCommon::TotalPositions()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.TotalPositions()

Python (Manager API)
    
    
    MTConCommon.TotalPositions

### Return Value

The total number of positions.
