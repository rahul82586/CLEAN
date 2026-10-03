[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapYearDaysDefault

[Previous](SwapYearDays.md) | [Next](SwapFlags.md)

# IMTConGroupSymbol::SwapYearDaysDefault

Get the default number of days in a year specified for the symbol. For further details please refer to the ["Use of Default methods" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT  IMTConGroupSymbol::SwapYearDaysDefault()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.SwapYearDaysDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapYearDaysDefault

### Return Value

The number of days in a year.

### Note

The number of days in a year is used when calculating [percentage swaps (#percentage)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps#percentage).
