[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Selected Symbols](../Selected-Symbols.md) / SelectedDeleteBatch

[Previous](SelectedDelete.md) | [Next](SelectedDeleteAll.md)

# IMTManagerAPI::SelectedDeleteBatch

Delete a batch of symbols from the list of selected symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedDeleteBatch(
       LPWSTR*          symbols,       // An array of symbols
       UINT             symbols_total  // The number of symbols
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SelectedDeleteBatch(
       array<String^>^  symbols        // An array of symbols
       )

Python
    
    
    ManagerAPI.SelectedDeleteBatch(
       symbols          # An array of symbols
       )

### Parameters

**symbols**  
[in] An array of pointers to symbol names.

**symbols_total**  
[in] The number of elements in the 'symbols' array.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

You cannot delete symbols, for which you currently have [unfilled orders](../Trade-Databases/Orders/OrderGetOpen.md) or [open positions](../Trade-Databases/Positions/PositionGet.md)(in appropriate [pumping modes](../Connection-to-the-Server/Pumping-Modes.md)).
