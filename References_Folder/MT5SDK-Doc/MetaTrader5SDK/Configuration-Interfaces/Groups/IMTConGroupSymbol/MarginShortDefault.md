[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginShortDefault

[Previous](MarginShort.md) | [Next](MarginLimit.md)

# IMTConGroupSymbol::MarginShortDefault

Get the default [margin ratio for short positions and orders](../../Symbols/IMTConSymbol/MarginShort.md) set for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginShortDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginShortDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginShortDefault

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. You should use [IMTConGroupSymbol::MarginRateInitialDefault](MarginRateInitialDefault.md) and [IMTConGroupSymbol::MarginRateMaintenanceDefault](MarginRateMaintenanceDefault.md) instead.
