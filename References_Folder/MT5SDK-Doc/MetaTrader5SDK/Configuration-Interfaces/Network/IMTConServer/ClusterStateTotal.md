[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / ClusterStateTotal

[Previous](FailoverTimeout.md) | [Next](ClusterStateNext.md)

# IMTConServer::ClusterStateTotal

Get the number of cluster components, the status of connection with which can be analyzed for the current server.

C++
    
    
    UINT  IMTConServer::ClusterStateTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.ClusterStateTotal()

Python (Manager API)
    
    
    MTConServer.ClusterStateTotal()

### Return Value

The number of cluster components.
