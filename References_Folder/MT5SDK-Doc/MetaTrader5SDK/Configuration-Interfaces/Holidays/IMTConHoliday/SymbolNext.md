[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](../IMTConHolidaySink.md)

# IMTConHoliday::SymbolNext

Get [a symbol](../../Symbols.md) from the list of symbols, to which the holiday applies, based on its index.

C++
    
    
    LPCWSTR  IMTConHoliday::SymbolNext(
       const UINT  pos      // Position of the symbol
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConHoliday.SymbolNext(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConHoliday.SymbolNext(
       pos         # Position of the symbol
       )
    
    
    MTConHoliday.SymbolGet()

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

### Return Value

If successful, it returns a pointer to a string with the full name of the symbol including the path to it. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConHoliday](../IMTConHoliday.md) object.

### 
