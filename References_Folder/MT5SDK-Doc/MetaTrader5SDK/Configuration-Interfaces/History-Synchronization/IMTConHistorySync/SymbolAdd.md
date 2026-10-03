[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / SymbolAdd

[Previous](To.md) | [Next](SymbolUpdate.md)

# IMTConHistorySync::SymbolAdd

Add a symbol for which history data will be synchronized.

C++
    
    
    MTAPIRES  IMTConHistorySync::SymbolAdd(
       LPCWSTR  path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.SymbolAdd(
       string   path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConHistorySync.SymbolAdd(
       path     # путь к символу
       )

### Parameters

**path**  
[in] Path to a symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Path](../../Symbols/IMTConSymbol/Path.md) value is used as the path to the symbol.
