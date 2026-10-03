[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BackupServer

[Previous](AccessServer.md) | [Next](AntiDDoSServer.md)

# IMTConServer::BackupServer

The interface of the Backup Server.

C++
    
    
    IMTConServerBackup*  IMTConServer::BackupServer()

.NET (Gateway/Manager API)
    
    
    CIMTConServerBackup  CIMTConServer.BackupServer()

Python (Manager API)
    
    
    MTConServer.BackupServer()

### Return Value

It returns a pointer to the object that implements the [IMTConServerBackup](../IMTConServerBackup.md) interface. In case of failure, it returns NULL.

### Note

The server type [IMTConServer::Type()](Type.md) defines what specific parameters the server has.
