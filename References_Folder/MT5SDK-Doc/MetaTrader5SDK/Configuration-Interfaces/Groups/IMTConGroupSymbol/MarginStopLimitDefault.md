[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginStopLimitDefault

[Previous](MarginStopLimit.md) | [Next](MarginHedged.md)

# IMTConGroupSymbol::MarginStopLimitDefault

Get the default [margin ratio for stop-limit orders](../../Symbols/IMTConSymbol/MarginStopLimit.md) set for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginStopLimitDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginStopLimitDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginStopLimitDefault

Note

The method is obsolete. The functionality of the method in the future is not guaranteed. You should use [IMTConGroupSymbol::MarginRateInitialDefault](MarginRateInitialDefault.md) and [IMTConGroupSymbol::MarginRateMaintenanceDefault](MarginRateMaintenanceDefault.md) instead.
