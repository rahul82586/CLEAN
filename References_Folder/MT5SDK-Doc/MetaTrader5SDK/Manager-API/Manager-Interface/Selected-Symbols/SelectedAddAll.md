[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Selected Symbols](../Selected-Symbols.md) / SelectedAddAll

[Previous](SelectedAddBatch.md) | [Next](SelectedDelete.md)

# IMTManagerAPI::SelectedAddAll

Add all available symbols to the list of selected symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedAddAll()

.NET
    
    
    MTRetCode  CIMTManagerAPI.SelectedAddAll()

Python
    
    
    ManagerAPI.SelectedAddAll()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This methods adds all the symbols available to a manager into the list of selected symbols.
