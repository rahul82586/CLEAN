[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / MarginInitial

[Previous](MarginLeverage.md) | [Next](MarginMaintenance.md)

# IMTAccount::MarginInitial

Get the current size of the initial margin of positions on a trading account.

C++
    
    
    double  IMTAccount::MarginInitial()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.MarginInitial()

### Return Value

The current size of the initial margin of positions on a trading account.

# IMTAccount::MarginInitial

Set the current size of the initial margin of positions on a trading account.

C++
    
    
    MTAPIRES  IMTAccount::MarginInitial(
       const double  margin      // Initial margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.MarginInitial(
       double        margin      // Initial margin
       )

### Parameters

**margin**  
[in] The current size of the initial margin of positions on a trading account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
