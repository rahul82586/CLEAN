[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PointsDelete

[Previous](PointsShift.md) | [Next](PointsClear.md)

# IMTConServerAccess::PointsDelete

Delete an access point by the index.

C++
    
    
    MTAPIRES  IMTConServerAccess::PointsDelete(
       const UINT  pos      // Position of the access point
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.PointsDelete(
       uint        pos      // Position of the access point
       )

Python (Manager API)
    
    
    MTConServerAccess.PointsDelete(
       pos         # Position of the access point
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is obsolete. Use [IMTConServer::PointsDelete](../IMTConServer/PointsDelete.md) instead.
