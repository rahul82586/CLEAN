[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkBytesSent

[Previous](NetworkRescan.md) | [Next](NetworkBytesRead.md)

# IMTAdminAPI::NetworkBytesSent

Receive the number of bytes sent to the server via Manager API. All copies of [IMTAdminAPI](../../Administrator-Interface.md) and [IMTManagerAPI](../../Manager-Interface.md) in the current process are considered.

C++
    
    
    UINT64  IMTAdminAPI::NetworkBytesSent()

.NET
    
    
    ulong  CIMTAdminAPI.NetworkBytesSent()

Python
    
    
    AdminAPI.NetworkBytesSent()

### Return Value

Number of bytes sent to the server via Manager API. All copies of [IMTAdminAPI](../../Administrator-Interface.md) and [IMTManagerAPI](../../Manager-Interface.md) in the current process are considered.

### 
