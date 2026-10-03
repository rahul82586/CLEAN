[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyMarginDigits

[Previous](CurrencyMargin.md) | [Next](CurrencyMarginDigitsSet.md)

# IMTConSymbol::CurrencyMarginDigits

Get the accuracy of conversion into the margin currency.

C++
    
    
    UINT  IMTConSymbol::CurrencyMarginDigits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.CurrencyMarginDigits()

Python (Manager API)
    
    
    MTConSymbol.CurrencyMarginDigits

### Return Value

The number of decimal places in the rate of conversion to the margin currency.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.
