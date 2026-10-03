[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkBytesRead

[Previous](NetworkBytesSent.md) | [Next](NetworkServer.md)

# IMTAdminAPI::NetworkBytesRead

Receive the number of bytes accepted from the server via Manager API. All copies of [IMTAdminAPI](../../Administrator-Interface.md) and [IMTManagerAPI](../../Manager-Interface.md) in the current process are considered.

C++
    
    
    UINT64  IMTAdminAPI::NetworkBytesRead()

.NET
    
    
    ulong  CIMTAdminAPI.NetworkBytesRead()

Python
    
    
    AdminAPI.NetworkBytesRead()

### Return Value

Number of bytes accepted from the server via Manager API. All copies of [IMTAdminAPI](../../Administrator-Interface.md) and [IMTManagerAPI](../../Manager-Interface.md) in the current process are considered.

### 
