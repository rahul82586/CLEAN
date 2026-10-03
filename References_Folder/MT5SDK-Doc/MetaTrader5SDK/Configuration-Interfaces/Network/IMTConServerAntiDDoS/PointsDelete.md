[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / PointsDelete

[Previous](PointsShift.md) | [Next](PointsClear.md)

# IMTConServerAccess::PointsDelete

Delete a public access point of the Anti DDoS protection provider with the specified index.

C++
    
    
    MTAPIRES  IMTConServerAccess::PointsDelete(
       const UINT  pos      // The position of the access point
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.PointsDelete(
       uint        pos      // The position of the access point
       )

Python (Manager API)
    
    
    MTConServerAccess.PointsDelete(
       pos         # The position of the access point
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The access points should be received from your Anti DDoS protection provider. Clients will connect to the trading platform using these points.
