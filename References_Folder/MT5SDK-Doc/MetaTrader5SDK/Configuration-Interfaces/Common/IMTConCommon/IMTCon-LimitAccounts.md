[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon LimitAccounts

[Previous](IMTCon-LimitWebServers.md) | [Next](IMTCon-LimitDeals.md)

# IMTConCommon::LimitAccounts

Get the maximum number of [accounts](../../../Database-Interfaces/Users.md) that can be opened in the trading platform.

C++
    
    
    UINT  IMTConCommon::LimitAccounts()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.LimitAccounts()

Python (Manager API)
    
    
    MTConCommon.LimitAccounts

### Return Value

The maximum number of accounts.

### Note

The maximum number of accounts is specified in the license.
