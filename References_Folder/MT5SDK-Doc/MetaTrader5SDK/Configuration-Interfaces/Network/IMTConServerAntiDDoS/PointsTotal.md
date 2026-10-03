[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / PointsTotal

[Previous](PointsClear.md) | [Next](PointsNext.md)

# IMTConServerAccess::PointsTotal

Get the number of access points of the Anti DDoS protection provider.

C++
    
    
    UINT  IMTConServerAccess::PointsTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAccess.PointsTotal()

Python (Manager API)
    
    
    MTConServerAccess.PointsTotal()

### Return Value

The number of access points.

### Note

The access points should be received from your Anti DDoS protection provider. Clients will connect to the trading platform using these points.
