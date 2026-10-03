[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / AntiDDoSServer

[Previous](BackupServer.md) | [Next](PointsAdd.md)

# IMTConServer::AntiDDoSServer

The Anti DDoS server interface.

C++
    
    
    IMTConServerBackup*  IMTConServer::AntiDDoSServer()

.NET (Gateway/Manager API)
    
    
    CIMTConServerBackup  CIMTConServer.AntiDDoSServer()

Python (Manager API)
    
    
    MTConServer.AntiDDoSServer()

### Return Value

It returns a pointer to the object that implements the [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) interface. In case of failure, it returns NULL.

### Note

Depending on the server type [IMTConServer::Type()](Type.md), it is defined which specific parameters the server has.
