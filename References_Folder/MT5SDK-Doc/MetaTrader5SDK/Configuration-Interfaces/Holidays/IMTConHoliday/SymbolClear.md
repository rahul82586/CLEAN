[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / SymbolClear

[Previous](SymbolDelete.md) | [Next](SymbolTotal.md)

# IMTConHoliday::SymbolClear

Clear the list of [symbols](../../Symbols.md) to which the holiday applies.

C++
    
    
    MTAPIRES  IMTConHoliday::SymbolClear()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.SymbolClear()

Python (Manager API)
    
    
    MTConHoliday.SymbolClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of holiday symbols.
