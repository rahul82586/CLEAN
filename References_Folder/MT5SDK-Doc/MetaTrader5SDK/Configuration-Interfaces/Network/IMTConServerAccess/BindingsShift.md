[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / BindingsShift

[Previous](BindingsUpdate.md) | [Next](BindingsDelete.md)

# IMTConServerAccess::BindingsShift

Move a binding in the list.

C++
    
    
    MTAPIRES  IMTConServerAccess::BindingsShift(
       const UINT  pos,       // Position of the binding
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.BindingsShift(
       uint        pos,       // Position of the binding
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConServerAccess.BindingsShift(
       pos,        # Position of the binding
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the binding in the list, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is obsolete. Use [IMTConServer::BindingsShift](../IMTConServer/BindingsShift.md) instead.
