[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon LimitGroups

[Previous](IMTCon-LimitDeals.md) | [Next](IMTCon-LimitSymbols.md)

# IMTConCommon::LimitGroups

Get the maximum number of [groups](../../Groups.md) that can be created in the trading platform.

C++
    
    
    UINT  IMTConCommon::LimitGroups()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.LimitGroups()

Python (Manager API)
    
    
    MTConCommon.LimitGroups

### Return Value

The maximum number of groups.

### Note

The maximum number of groups is specified in the license. This number includes predefined [groups](../../Groups.md).
