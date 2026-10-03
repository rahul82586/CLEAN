[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PointsTotal

[Previous](PointsClear.md) | [Next](PointsNext.md)

# IMTConServerAccess::PointsTotal

Get the number of access points of the Access Server.

C++
    
    
    UINT  IMTConServerAccess::PointsTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAccess.PointsTotal()

Python (Manager API)
    
    
    MTConServerAccess.PointsTotal()

### Return Value

The number of access points of the Access Server.

### Note

The method is obsolete. Use [IMTConServer::PointsTotal](../IMTConServer/PointsTotal.md) instead.
