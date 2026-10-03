[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Connected

[Previous](LastBootTime.md) | [Next](OS.md)

# IMTConServer::Connected

Get the status of a server connection to the main trade server.

C++
    
    
    bool  IMTConServer::Connected()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConServer.Connected()

Python (Manager API)
    
    
    MTConServer.Connected

### Return Value

0 - the server is not connected to the main trade server, 1 - the server is connected.
