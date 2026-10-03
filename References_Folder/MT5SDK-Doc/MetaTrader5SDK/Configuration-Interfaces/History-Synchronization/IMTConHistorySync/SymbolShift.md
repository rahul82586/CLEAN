[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / SymbolShift

[Previous](SymbolUpdate.md) | [Next](SymbolDelete.md)

# IMTConHistorySync::SymbolShift

Change the position of a symbol for which history data are synchronized.

C++
    
    
    MTAPIRES  IMTConHistorySync::SymbolShift(
       const UINT  pos,       // Position of the symbol
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.SymbolShift(
       uint        pos,       // Position of the symbol
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConHistorySync.SymbolShift(
       pos,        # Position of the symbol
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

**shift**  
[in] Shift of a symbol relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
