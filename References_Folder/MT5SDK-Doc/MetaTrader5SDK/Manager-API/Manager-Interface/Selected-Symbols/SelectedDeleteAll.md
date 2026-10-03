[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Selected Symbols](../Selected-Symbols.md) / SelectedDeleteAll

[Previous](SelectedDeleteBatch.md) | [Next](SelectedShift.md)

# IMTManagerAPI::SelectedDeleteAll

Delete all symbols from the list of selected symbols

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedDeleteAll()

.NET
    
    
    MTRetCode  CIMTManagerAPI.SelectedDeleteAll()

Python
    
    
    ManagerAPI.SelectedDeleteAll()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Symbols for which there are [unfulfilled orders](../Trade-Databases/Orders/OrderGetOpen.md) pr [open positions](../Trade-Databases/Positions/PositionGet.md)(in the appropriate [pimping modes](../Connection-to-the-Server/Pumping-Modes.md)) cannot be deleted.
