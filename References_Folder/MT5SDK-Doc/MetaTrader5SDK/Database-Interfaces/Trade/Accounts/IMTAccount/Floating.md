[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Floating

[Previous](Commission.md) | [Next](Equity.md)

# IMTAccount::Floating

Get the size of floating profit/loss of open positions on the account.

C++
    
    
    double  IMTAccount::Floating()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Floating()

### Return Value

The size of floating profit/loss of open positions on the account. The floating profit/loss is calculated as the sum of [IMTAccount::Profit](Profit.md) and [IMTAccount::Storage](Storage.md) of open positions on the account.

# IMTAccount::Floating

Set the size of floating profit/loss of open positions on the account.

C++
    
    
    MTAPIRES  IMTAccount::Floating(
       const double  floating      // Floating profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Floating(
       double        floating      // Floating profit
       )

### Parameters

**floating**  
[in] The size of floating profit/loss of open positions on the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
