[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / AccessServer

[Previous](HistoryServer.md) | [Next](BackupServer.md)

# IMTConServer::AccessServer

The interface of the Access Server.

C++
    
    
    IMTConServerAccess*  IMTConServer::AccessServer()

.NET (Gateway/Manager API)
    
    
    CIMTConServerAccess  CIMTConServer.AccessServer()

Python (Manager API)
    
    
    MTConServer.AccessServer()

### Return Value

It returns a pointer to the object that implements the [IMTConServerAccess](../IMTConServerAccess.md) interface. In case of failure, it returns NULL.

### Note

The server type [IMTConServer::Type()](Type.md) defines what specific parameters the server has.
