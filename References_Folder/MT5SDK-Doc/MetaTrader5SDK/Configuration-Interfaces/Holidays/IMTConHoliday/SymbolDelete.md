[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / SymbolDelete

[Previous](SymbolShift.md) | [Next](SymbolClear.md)

# IMTConHoliday::SymbolDelete

Delete a [symbol](../../Symbols.md) from the list of symbols, to which the holiday applies.

C++
    
    
    MTAPIRES  IMTConHoliday::SymbolDelete(
       const UINT  pos      // Position of the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.SymbolDelete(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConHoliday.SymbolDelete(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
