[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / PointsDelete

[Previous](PointsShift.md) | [Next](PointsClear.md)

# IMTConServer::PointsDelete

Delete an access point by the index.

C++
    
    
    MTAPIRES  IMTConServer::PointsDelete(
       const UINT  pos      // Position of the access point
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.PointsDelete(
       uint        pos      // Position of the access point
       )

Python (Manager API)
    
    
    MTConServer.PointsDelete(
       pos         # Position of the access point
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Connections from other platform components, client connections from terminals and API (for access servers) are accepted through public access points.
