[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundAccount](../IMTConFundAccount.md) / Name

[Previous](Login.md) | [Next](Balance.md)

# IMTConFundAccount::Name

Get the name of the fund manager.

C++
    
    
    LPCWSTR  IMTConFundAccount::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFundAccount.Name()

### Return Value

If successful, a pointer to a string with the name is returned. Otherwise, NULL is returned.

### Note

The name is taken from the fields [IMTUser::FirstName](../../../Database-Interfaces/Users/IMTUser/FirstName.md) and [IMTUser::LastName](../../../Database-Interfaces/Users/IMTUser/FirstName.md) of the manager's account.
