[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Selected Symbols](../Selected-Symbols.md) / SelectedDelete

[Previous](SelectedAddAll.md) | [Next](SelectedDeleteBatch.md)

# IMTManagerAPI::SelectedDelete

Remove a symbol from the list of selected symbols by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedDelete(
       LPCWSTR  symbol      // Symbol name
       )

.NET
    
    
    MTRetCode  CIMIManagerAPI.SelectedDelete(
       string   symbol      // Symbol name
       )

Python
    
    
    ManagerAPI.SelectedDelete(
       str      symbol      # Symbol name
       )

### Parameters

**symbol**  
[in] Symbol name. TheIMTConSymbol::Symbolvalue is used as the symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Symbols for which there are [unfulfilled orders](../Trade-Databases/Orders/OrderGetOpen.md) pr [open positions](../Trade-Databases/Positions/PositionGet.md)(in the appropriate [pimping modes](../Connection-to-the-Server/Pumping-Modes.md)) cannot be deleted.

# IMTManagerAPI::SelectedDelete

Remove a symbol from the list of selected symbols by the index.

C++
    
    
    MTAPIRES  IMTManagerAPI::SelectedDelete(
       const UINT  pos      // Position of the symbol
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SelectedDelete(
       uint        pos      // Position of the symbol
       )

Python
    
    
    ManagerAPI.SelectedDelete(
       int         pos      # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol in the list of selected symbols, ranging from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Symbols for which there are [unfulfilled orders](../Trade-Databases/Orders/OrderGetOpen.md) pr [open positions](../Trade-Databases/Positions/PositionGet.md)(in the appropriate [pimping modes](../Connection-to-the-Server/Pumping-Modes.md)) cannot be deleted.
