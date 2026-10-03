[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Profit

[Previous](MarginMaintenance.md) | [Next](Storage.md)

# IMTAccount::Profit

Get the size of the current profit for all open positions.

C++
    
    
    double  IMTAccount::Profit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Profit()

### Return Value

The size of the current profit for all open positions.

# IMTAccount::Profit

Set the size of the current profit for all open positions.

C++
    
    
    MTAPIRES  IMTAccount::Profit(
       const double  profit      // Profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Profit(
       double        profit      // Profit
       )

### Parameters

**profit**  
[in] The size of the current profit for all open positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
