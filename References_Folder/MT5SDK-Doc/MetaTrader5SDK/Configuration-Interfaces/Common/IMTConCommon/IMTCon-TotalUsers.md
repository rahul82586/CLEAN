[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon TotalUsers

[Previous](IMTCon-LiveUpdateMode.md) | [Next](IMTCon-TotalUsersReal.md)

# IMTConCommon::TotalUsers

Get the total number of [client accounts](../../../Database-Interfaces/Users.md) in the whole trading platform (on all trade server).

C++
    
    
    UINT  IMTConCommon::TotalUsers()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.TotalUsers()

Python (Manager API)
    
    
    MTConCommon.TotalUsers

### Return Value

The total number of client accounts.
