[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BindingsTotal

[Previous](BindingsClear.md) | [Next](BindingsNext.md)

# IMTConServer::BindingsTotal

Get the number of bindings of the Access Server.

C++
    
    
    UINT  IMTConServer::BindingsTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.BindingsTotal()

Python (Manager API)
    
    
    MTConServer.BindingsTotal()

### Return Value

The number of bindings of the Access Server.

### Note

Address for listening (binding) is the address and port to be listened to by the access server for the availability of external connections.
