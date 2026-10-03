[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / SymbolDelete

[Previous](SymbolShift.md) | [Next](SymbolTotal.md)

# IMTConHistorySync::SymbolDelete

Delete a symbol for which history data are synchronized, based on the position in the list.

C++
    
    
    MTAPIRES  IMTConHistorySync::SymbolDelete(
       const UINT  pos      // Position of the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.SymbolDelete(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConHistorySync.SymbolDelete(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
