[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon LimitDeals

[Previous](IMTCon-LimitAccounts.md) | [Next](IMTCon-LimitGroups.md)

# IMTConCommon::LimitDeals

Get the maximum number of [deals](../../../Database-Interfaces/Trade/Deals.md) that can be committed in the trading platform.

C++
    
    
    UINT  IMTConCommon::LimitDeals()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.LimitDeals()

Python (Manager API)
    
    
    MTConCommon.LimitDeals

### Return Value

The maximum number of deals.

### Note

The maximum number of deals is specified in the license.
