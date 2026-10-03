[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / PointsUpdate

[Previous](PointsAdd.md) | [Next](PointsShift.md)

# IMTConServer::PointsUpdate

Update the access point (public address) at the specified position in the list.

C++
    
    
    MTAPIRES  IMTConServer::PointsUpdate(
       const UINT  pos,         // Position of the access point
       LPCWSTR     address      // Address and port of the access point
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.PointsUpdate(
       uint        pos,         // Position of the access point
       string      address      // Address and port of the access point
       )

Python (Manager API)
    
    
    MTConServer.PointsUpdate(
       pos,        # Position of the access point
       address     # Address and port of the access point
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

**address**  
[in] The updated address and port of the access point, separated by a colon.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An access point is specified in the format address:port.
