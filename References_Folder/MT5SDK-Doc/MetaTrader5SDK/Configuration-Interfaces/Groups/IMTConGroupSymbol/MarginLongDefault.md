[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginLongDefault

[Previous](MarginLong.md) | [Next](MarginShort.md)

# IMTConGroupSymbol::MarginLongDefault

Get the default [margin ratio for long positions and orders](../../Symbols/IMTConSymbol/MarginLong.md) set for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginLongDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginLongDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginLongDefault

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. You should use [IMTConGroupSymbol::MarginRateInitialDefault](MarginRateInitialDefault.md) and [IMTConGroupSymbol::MarginRateMaintenanceDefault](MarginRateMaintenanceDefault.md) instead.
