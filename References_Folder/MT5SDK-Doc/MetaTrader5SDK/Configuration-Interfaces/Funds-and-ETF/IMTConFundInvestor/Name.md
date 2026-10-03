[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundInvestor](../IMTConFundInvestor.md) / Name

[Previous](Login.md) | [Next](SharesVolume.md)

# IMTConFundInvestor::Name

Get the name of the fund investor.

C++
    
    
    LPCWSTR  IMTConFundInvestor::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFundInvestor.Name()

### Return Value

If successful, a pointer to a string with the name is returned. Otherwise, NULL is returned.

### Note

The name is taken from the fields [IMTUser::FirstName](../../../Database-Interfaces/Users/IMTUser/FirstName.md) and [IMTUser::LastName](../../../Database-Interfaces/Users/IMTUser/FirstName.md) of the investor's account.
