[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / ConnectsCritical

[Previous](ConnectsMax.md) | [Next](Max.md)

# IMTConServer::ConnectsCritical

Get the critical number of simultaneous connections to the server.

C++
    
    
    UINT  IMTConServer::ConnectsCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.ConnectsCritical()

Python (Manager API)
    
    
    MTConServer.ConnectsCritical

### Return Value

Critical number of simultaneous connections to the server.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
