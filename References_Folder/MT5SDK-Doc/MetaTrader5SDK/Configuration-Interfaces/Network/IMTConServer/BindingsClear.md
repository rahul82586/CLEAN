[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BindingsClear

[Previous](BindingsDelete.md) | [Next](BindingsTotal.md)

# IMTConServer::BindingsClear

Clear the list of bindings.

C++
    
    
    MTAPIRES  IMTConServer::BindingsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.BindingsClear()

Python (Manager API)
    
    
    MTConServer.BindingsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of server bindings.
