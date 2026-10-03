[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / BindingsDelete

[Previous](BindingsShift.md) | [Next](BindingsClear.md)

# IMTConServerAccess::BindingsDelete

Delete a binding by the index.

C++
    
    
    MTAPIRES  IMTConServerAccess::BindingsDelete(
       const UINT  pos      // Position of the binding
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.BindingsDelete(
       uint        pos      // Position of the binding
       )

Python (Manager API)
    
    
    MTConServerAccess.BindingsDelete(
       pos         # Position of the binding
       )

### Parameters

**pos**  
[in] Position of the binding in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is obsolete. Use [IMTConServer::BindingsDelete](../IMTConServer/BindingsDelete.md) instead.
