[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CurrencyDigits

[Previous](Currency.md) | [Next](CurrencyDigitsSet.md)

# IMTConGroup::CurrencyDigits

Get the number of digits after the decimal point in the group deposit currency.

C++
    
    
    UINT  IMTConGroup::CurrencyDigits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.CurrencyDigits()

Python (Manager API)
    
    
    MTConGroup.CurrencyDigits

### Return Value

The number of digits after the decimal point in the group deposit currency.

### Note

This parameter affects the display (number of digits after the decimal point) of the accounts' trading status in the terminals, including the balance, equity, margin, etc.
