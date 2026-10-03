[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / SymbolAdd

[Previous](WorkToMinutes.md) | [Next](SymbolUpdate.md)

# IMTConHoliday::SymbolAdd

Add [a symbol](../../Symbols.md), to which the holiday will apply.

C++
    
    
    MTAPIRES  IMTConHoliday::SymbolAdd(
       LPCWSTR  path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.SymbolAdd(
       string   path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConHoliday.SymbolAdd(
       path     # Path to the symbol
       )

### Parameters

**path**  
[in] Path to a symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

[IMTConSymbol::Path](../../Symbols/IMTConSymbol/Path.md) value is used as the path to the symbol.
