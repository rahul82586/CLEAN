[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundAccount](../IMTConFundAccount.md) / Balance

[Previous](Name.md) | [Next](Equity.md)

# IMTConFundAccount::Balance

Get the current balance of the account used for fund management.

C++
    
    
    double  IMTConFundAccount::Balance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConFundAccount.Balance()

### Return Value

The current balance of the account used for fund management.

### Note

The currency in which the value is specified, is determined by the [IMTConFundAccount::Currency](Currency.md) property.
