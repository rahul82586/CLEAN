[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PointsNext

[Previous](PointsTotal.md) | [Next](BindingsAdd.md)

# IMTConServerAccess::PointsNext

Get an access point by the index.

C++
    
    
    MTAPIRES  IMTConServerAccess::PointsNext(
       const UINT  pos      // Position of the access point
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.PointsNext(
       uint        pos      // Position of the access point
       )

Python (Manager API)
    
    
    MTConServerAccess.PointsNext(
       pos         # Position of the access point
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is obsolete. Use [IMTConServer::PointsNext](../IMTConServer/PointsNext.md) instead.
