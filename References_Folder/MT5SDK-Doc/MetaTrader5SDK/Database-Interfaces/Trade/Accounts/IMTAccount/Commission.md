[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Commission

[Previous](Storage.md) | [Next](Floating.md)

# IMTAccount::Commission

Get the size of commissions charged for all transactions on the account.

C++
    
    
    double  IMTAccount::Commission()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Commission()

### Return Value

The size of commissions charged for all transactions on the account.

### Note

The field is deprecated and is no longer used.

# IMTAccount::Commission

Set the size of commissions charged for all transactions on the account.

C++
    
    
    MTAPIRES  IMTAccount::Commission(
       const double  storage      // Commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Commission(
       double        storage      // Commission
       )

### Parameters

**storage**  
[in] The size of commissions charged for all transactions on the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The field is deprecated and is no longer used.
