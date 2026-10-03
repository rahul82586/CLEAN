[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](Flags.md)

# IMTConHistorySync::SymbolNext

Get a symbol for which history data are synchronized, based on the position in the list.

C++
    
    
    LPCWSTR  IMTConHistorySync::SymbolNext(
       const UINT  pos      // Position of the symbol
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConHistorySync.SymbolNext(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConHistorySync.SymbolNext(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

### Return Value

If successful, it returns a pointer to a string with the symbol name and path to it in accordance with the hierarchy of symbols in the platform. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConHistorySync](../IMTConHistorySync.md) object.
