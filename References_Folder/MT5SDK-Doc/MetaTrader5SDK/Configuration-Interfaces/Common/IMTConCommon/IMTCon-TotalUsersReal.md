[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon TotalUsersReal

[Previous](IMTCon-TotalUsers.md) | [Next](IMTCon-TotalDeals.md)

# IMTConCommon::TotalUsersReal

Get the total number of real[clients](../../../Database-Interfaces/Users.md) in the whole trading platform (on all trade server).

C++
    
    
    UINT  IMTConCommon::TotalUsersReal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.TotalUsersReal()

Python (Manager API)
    
    
    MTConCommon.TotalUsersReal

### Return Value

The total number of real clients.

### Note

Real clients imply the accounts that are not included in [groups](../../Groups.md) manager*, demo*, preliminary* and contest*.
