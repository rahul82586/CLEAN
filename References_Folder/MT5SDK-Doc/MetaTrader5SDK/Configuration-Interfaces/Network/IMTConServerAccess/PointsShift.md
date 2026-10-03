[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PointsShift

[Previous](PointsUpdate.md) | [Next](PointsDelete.md)

# IMTConServerAccess::PointsShift

Move an access point in the list.

C++
    
    
    MTAPIRES  IMTConServerAccess::PointsShift(
       const UINT  pos,       // Position of the access point
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.PointsShift(
       uint        pos,       // Position of the access point
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConServerAccess.PointsShift(
       pos,        # Position of the access point
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the access point in the list, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is obsolete. Use [IMTConServer::PointsShift](../IMTConServer/PointsShift.md) instead.
