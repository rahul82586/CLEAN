[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginStopDefault

[Previous](MarginStop.md) | [Next](MarginStopLimit.md)

# IMTConGroupSymbol::MarginStopDefault

Get the default [margin ratio for stop orders](../../Symbols/IMTConSymbol/MarginStop.md) set for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginStopDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginStopDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginStopDefault

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. You should use [IMTConGroupSymbol::MarginRateInitialDefault](MarginRateInitialDefault.md) and [IMTConGroupSymbol::MarginRateMaintenanceDefault](MarginRateMaintenanceDefault.md) instead.
