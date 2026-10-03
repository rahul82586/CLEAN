[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / BindingsAdd

[Previous](PointsNext.md) | [Next](BindingsUpdate.md)

# IMTConServerAccess::BindingsAdd

Add a binding.

C++
    
    
    MTAPIRES  IMTConServerAccess::BindingsAdd(
       LPCWSTR  path      // Binding address and port
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.BindingsAdd(
       string   path      // Binding address and port
       )

Python (Manager API)
    
    
    MTConServerAccess.BindingsAdd(
       binding  # Binding address and port
       )

### Parameters

**path**  
[in] Address and port of the binding, separated by a colon.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The binding is specified in the format address:port.
