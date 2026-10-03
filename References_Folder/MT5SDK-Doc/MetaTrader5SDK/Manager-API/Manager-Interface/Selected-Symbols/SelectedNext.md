[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Selected Symbols](../Selected-Symbols.md) / SelectedNext

[Previous](SelectedTotal.md) | [Next](../Clients.md)

# IMTManagerAPI::SelectedNext

Get the name of a symbol by a position in the list of selected symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedNext(
       const UINT  pos,         // Symbol position
       MTAPISTR&   symbol       // Symbol name
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SelectedNext(
       uint        pos,         // Symbol position
       out string  symbol       // Symbol name
       )

Python
    
    
    ManagerAPI.SelectedNext(
       pos         # Symbol position
       )

### Parameters

**pos**  
[in] Position of the symbol in the list of selected symbols, ranging from 0.

**symbol**  
[out] Symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
