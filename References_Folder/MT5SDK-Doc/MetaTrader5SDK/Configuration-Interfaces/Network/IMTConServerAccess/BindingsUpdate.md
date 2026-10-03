[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / BindingsUpdate

[Previous](BindingsAdd.md) | [Next](BindingsShift.md)

# IMTConServerAccess::BindingsUpdate

Update the binding at the specified position in the list.

C++
    
    
    MTAPIRES  IMTConServerAccess::BindingsUpdate(
       const UINT  pos,         // Position of the binding
       LPCWSTR     address      // Binding address and port
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.BindingsUpdate(
       uint        pos,         // Position of the binding
       string      address      // Binding address and port
       )

Python (Manager API)
    
    
    MTConServerAccess.BindingsUpdate(
       pos,        # Position of the binding
       address     # Binding address and port
       )

### Parameters

**pos**  
[in] Position of the binding in the list, starting with 0.

**address**  
[in] Address and port of the binding, separated by a colon.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The binding is specified in the format address:port.
