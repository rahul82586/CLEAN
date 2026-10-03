[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BindingsDelete

[Previous](BindingsShift.md) | [Next](BindingsClear.md)

# IMTConServer::BindingsDelete

Delete a binding by the index.

C++
    
    
    MTAPIRES  IMTConServer::BindingsDelete(
       const UINT  pos      // Position of the binding
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.BindingsDelete(
       uint        pos      // Position of the binding
       )

Python (Manager API)
    
    
    MTConServer.BindingsDelete(
       pos         # Position of the binding
       )

### Parameters

**pos**  
[in] Position of the binding in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Address for listening (binding) is the address and port to be listened to by the access server for the availability of external connections.
