[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / SymbolShift

[Previous](SymbolUpdate.md) | [Next](SymbolDelete.md)

# IMTConHoliday::SymbolShift

Change the position of [a symbol](../../Symbols.md) in the list of symbols, to which the holiday applies.

C++
    
    
    MTAPIRES  IMTConHoliday::SymbolShift(
       const UINT  pos,       // Position of the symbol
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.SymbolShift(
       uint        pos,       // Position of the symbol
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConHoliday.SymbolShift(
       pos,        # Position of the symbol
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
