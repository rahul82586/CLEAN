[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyProfitDigits

[Previous](CurrencyProfit.md) | [Next](CurrencyProfitDigitsSet.md)

# IMTConSymbol::CurrencyProfitDigits

Get the accuracy of conversion into the profit currency.

C++
    
    
    UINT  IMTConSymbol::CurrencyProfitDigits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.CurrencyProfitDigits()

Python (Manager API)
    
    
    MTConSymbol.CurrencyProfitDigits

### Return Value

The number of decimal places in the rate of conversion to the profit currency.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.
