[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginLimitDefault

[Previous](MarginLimit.md) | [Next](MarginStop.md)

# IMTConGroupSymbol::MarginLimitDefault

Get the default [margin ratio of limit orders](../../Symbols/IMTConSymbol/MarginLimit.md) set for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginLimitDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginLimitDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginLimitDefault

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. You should use [IMTConGroupSymbol::MarginRateInitialDefault](MarginRateInitialDefault.md) and [IMTConGroupSymbol::MarginRateMaintenanceDefault](MarginRateMaintenanceDefault.md) instead.
