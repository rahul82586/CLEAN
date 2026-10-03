[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyBaseDigits

[Previous](CurrencyBase.md) | [Next](CurrencyBaseDigitsSet.md)

# IMTConSymbol::CurrencyBaseDigits

Get the accuracy of conversion into the base currency.

C++
    
    
    UINT  IMTConSymbol::CurrencyBaseDigits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.CurrencyBaseDigits()

Python (Manager API)
    
    
    MTConSymbol.CurrencyBaseDigits

### Return Value

The number of decimal places in the rate of conversion to the base currency.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.
