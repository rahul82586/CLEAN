[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / MarginMaintenance

[Previous](MarginInitial.md) | [Next](Profit.md)

# IMTAccount::MarginMaintenance

Get the current size of the maintenance margin of positions on a trading account.

C++
    
    
    double  IMTAccount::MarginMaintenance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.MarginMaintenance()

### Return Value

The current size of the maintenance margin of positions on a trading account.

# IMTAccount::MarginMaintenance

Set the current size of the maintenance margin of positions on a trading account.

C++
    
    
    MTAPIRES  IMTAccount::MarginMaintenance(
       const double  margin      // Maintenance margin
       )

.NET (Gateway/Manager API)s
    
    
    MTRetCode  CIMTAccount.MarginMaintenance(
       double        margin      // Maintenance margin
       )

### Parameters

**margin**  
[in] The current size of the maintenance margin of positions on a trading account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
