[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BindingsAdd

[Previous](PointsNext.md) | [Next](BindingsUpdate.md)

# IMTConServer::BindingsAdd

Add a binding.

C++
    
    
    MTAPIRES  IMTConServer::BindingsAdd(
       LPCWSTR  path      // Binding address and port
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.BindingsAdd(
       string   path      // Binding address and port
       )

Python (Manager API)
    
    
    MTConServer.BindingsAdd(
       path     # Binding address and port
       )

### Parameters

**path**  
[in] Address and port of the binding, separated by a colon.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The binding is specified in the format address:port.
