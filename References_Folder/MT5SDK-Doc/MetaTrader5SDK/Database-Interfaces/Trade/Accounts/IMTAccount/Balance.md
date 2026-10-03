[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Balance

[Previous](CurrencyDigits.md) | [Next](Credit.md)

# IMTAccount::Balance

Get the balance of a trading account.

C++
    
    
    double  IMTAccount::Balance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Balance()

### Return Value

The current balance of a trading account.

# IMTAccount::Balance

Set the balance of a trading account.

C++
    
    
    MTAPIRES  IMTAccount::Balance(
       const double  balance      // Balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Balance(
       double        balance      // Balance
       )

### Parameters

**balance**  
The balance of a trading account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
