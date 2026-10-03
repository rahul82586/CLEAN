[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / BindingsClear

[Previous](BindingsDelete.md) | [Next](BindingsTotal.md)

# IMTConServerAccess::BindingsClear

Clear the list of bindings.

C++
    
    
    MTAPIRES  IMTConServerAccess::BindingsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.BindingsClear()

Python (Manager API)
    
    
    MTConServerAccess.BindingsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of server bindings.
