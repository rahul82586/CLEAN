[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Multiply

[Previous](Point.md) | [Next](TickFlags.md)

# IMTConSymbol::Multiply

Get the value to multiply the price to, to get the number of points.

C++
    
    
    double  IMTConSymbol::Multiply()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.Multiply()

Python (Manager API)
    
    
    MTConSymbol.Multiply

### Return Value

The value to multiply the price to, to get the number of points. Calculated as 10^Digits.
