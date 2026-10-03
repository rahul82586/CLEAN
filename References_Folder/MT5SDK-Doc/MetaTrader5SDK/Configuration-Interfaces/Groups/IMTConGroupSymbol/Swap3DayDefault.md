[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / Swap3DayDefault

[Previous](Swap3Day.md) | [Next](SwapYearDays.md)

# IMTConGroupSymbol::Swap3DayDefault

Get the default [day to charge triple swap](../../Symbols/IMTConSymbol/Swap3Day.md) set for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    INT  IMTConGroupSymbol::Swap3DayDefault()  const

.NET (Gateway/Manager API)
    
    
    int  IMTConGroupSymbol::Swap3DayDefault()

### Note

The method is obsolete and is no longer used. Please use default methods for the relevant days [IMTConGroupSymbol::SwapRate*Default](SwapRateSundayDefault.md) instead.
