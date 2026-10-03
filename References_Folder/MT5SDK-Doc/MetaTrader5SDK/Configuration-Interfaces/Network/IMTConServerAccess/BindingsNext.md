[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / BindingsNext

[Previous](BindingsTotal.md) | [Next](ServersAdd.md)

# IMTConServerAccess::BindingsNext

Gets a binding by the index.

C++
    
    
    MTAPIRES  IMTConServerAccess::BindingsNext(
       const UINT  pos      // Position of the binding
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.BindingsNext(
       uint        pos      // Position of the binding
       )

Python (Manager API)
    
    
    MTConServerAccess.BindingsNext(
       pos         # Position of the binding
       )

### Parameters

**pos**  
[in] Position of the binding in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is obsolete. Use [IMTConServer::BindingsNext](../IMTConServer/BindingsNext.md) instead.
