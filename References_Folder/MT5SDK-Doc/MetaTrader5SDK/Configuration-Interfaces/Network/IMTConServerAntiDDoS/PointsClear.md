[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / PointsClear

[Previous](PointsDelete.md) | [Next](PointsTotal.md)

# IMTConServerAntiDDoS::ServersClear

Clear the list of access points of the Anti DDoS protection provider.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::PointsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.PointsClear()

Python (Manager API)
    
    
    MTConServerAntiDDoS.PointsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The access points should be received from your Anti DDoS protection provider. Clients will connect to the trading platform using these points.
