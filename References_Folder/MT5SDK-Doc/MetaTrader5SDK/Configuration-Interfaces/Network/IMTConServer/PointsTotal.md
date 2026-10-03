[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / PointsTotal

[Previous](PointsClear.md) | [Next](PointsNext.md)

# IMTConServer::PointsTotal

Get the number of access points of the Access Server.

C++
    
    
    UINT  IMTConServer::PointsTotal()  const

.NET
    
    
    uint  CIMTConServer.PointsTotal()

Python (Manager API)
    
    
    MTConServer.PointsTotal()

### Return Value

The number of access points of the Access Server.

### Note

Connections from other platform components, client connections from terminals and API (for access servers) are accepted through public access points.
