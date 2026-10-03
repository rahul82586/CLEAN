[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / TotalUsersReal

[Previous](TotalUsers.md) | [Next](TotalDeals.md)

# IMTConServerTrade::TotalUsersReal

Get the total number of real [clients](../../../Database-Interfaces/Users.md) on the trade server.

C++
    
    
    UINT  IMTConServerTrade::TotalUsersReal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerTrade.TotalUsersReal()

Python (Manager API)
    
    
    MTConServerTrade.TotalUsersReal

### Return Value

The total number of real clients.

### Note

Real clients imply the accounts that are not included in [groups](../../Groups.md) manager*, demo*, preliminary* and contest*.
