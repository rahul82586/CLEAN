[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / SymbolUpdate

[Previous](SymbolAdd.md) | [Next](SymbolShift.md)

# IMTConHistorySync::SymbolUpdate

Modify the symbol for which history data are synchronized, based on the position in the list.

C++
    
    
    MTAPIRES  IMTConHistorySync::SymbolUpdate(
       const UINT  pos,      // Position of the symbol
       LPCWSTR     path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.SymbolUpdate(
       uint        pos,      // Position of the symbol
       string      path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConHistorySync.SymbolUpdate(
       pos,        # Position of the symbol
       path        # Path to the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

**path**  
[in] Path to the new symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Path](../../Symbols/IMTConSymbol/Path.md) value is used as the path to the symbol.
