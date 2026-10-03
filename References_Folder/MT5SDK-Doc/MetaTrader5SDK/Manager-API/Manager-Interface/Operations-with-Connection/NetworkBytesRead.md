[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkBytesRead

[Previous](NetworkBytesSent.md) | [Next](NetworkServer.md)

# IMTManagerAPI::NetworkBytesRead

Receive the number of bytes accepted from the server via Manager API. All copies of [IMTAdminAPI](../../Administrator-Interface.md) and [IMTManagerAPI](../../Manager-Interface.md) in the current process are considered.

C++
    
    
    UINT64  IMTManagerAPI::NetworkBytesRead()

.NET
    
    
    uint    CIMTManagerAPI.NetworkBytesRead()

Python
    
    
    ManagerAPI.NetworkBytesRead()

### Return Value

Number of bytes accepted from the server via Manager API. All copies of [IMTAdminAPI](../../Administrator-Interface.md) and [IMTManagerAPI](../../Manager-Interface.md) in the current process are considered.

### 
