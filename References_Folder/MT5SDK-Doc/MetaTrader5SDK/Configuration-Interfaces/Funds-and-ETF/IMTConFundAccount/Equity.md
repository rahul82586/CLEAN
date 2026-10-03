[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundAccount](../IMTConFundAccount.md) / Equity

[Previous](Balance.md) | [Next](Currency.md)

# IMTConFundAccount::Equity

Get the current equity of the account used for fund management.

C++
    
    
    double  IMTConFundAccount::Equity()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConFundAccount.Equity()

### Return Value

The current equity of the account used for fund management.

### Note

The currency in which the value is specified, is determined by the [IMTConFundAccount::Currency](Currency.md) property.
