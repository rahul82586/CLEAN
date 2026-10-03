[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / PointsNext

[Previous](PointsTotal.md) | [Next](BindingsAdd.md)

# IMTConServer::PointsNext

Get an access point by the index.

C++
    
    
    MTAPIRES  IMTConServer::PointsNext(
       const UINT  pos      // Position of the access point
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.PointsNext(
       uint        pos      // Position of the access point
       )

Python (Manager API)
    
    
    MTConServer.PointsNext(
       pos         # Position of the access point
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Connections from other platform components, client connections from terminals and API (for access servers) are accepted through public access points.
