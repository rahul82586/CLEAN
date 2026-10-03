[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Selected Symbols](../Selected-Symbols.md) / SelectedAdd

[Previous](../Selected-Symbols.md) | [Next](SelectedAddBatch.md)

# IMTManagerAPI::SelectedAdd

Add a symbol to the list by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedAdd(
       LPCWSTR  symbol      // Symbol name
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SelectedAdd(
       string   symbol      // Symbol name
       )

Python
    
    
    ManagerAPI.SelectedAdd(
       symbol   # Symbol name
       )

### Parameters

**symbol**  
[in] Symbol name. TheIMTConSymbol::Symbolvalue is used as the symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
