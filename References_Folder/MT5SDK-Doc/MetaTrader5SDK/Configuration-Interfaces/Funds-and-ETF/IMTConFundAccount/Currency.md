[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundAccount](../IMTConFundAccount.md) / Currency

[Previous](Equity.md) | [Next](CurrencyDigits.md)

# IMTConFundAccount::Currency

Get the currency in which manager account [balance](Balance.md) and [equity](Equity.md) are specified.

C++
    
    
    LPCWSTR  IMTConFundAccount::Currency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFundAccount.Currency()

### Return Value

If successful, the method returns a pointer to a string with the currency name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFundAccount](../IMTConFundAccount.md) object.
