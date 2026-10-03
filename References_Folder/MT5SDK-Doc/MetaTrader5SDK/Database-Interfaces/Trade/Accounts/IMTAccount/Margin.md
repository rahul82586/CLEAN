[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Margin

[Previous](Credit.md) | [Next](MarginFree.md)

# IMTAccount::Margin

Get the current value of the account margin.

C++
    
    
    double  IMTAccount::Margin()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Margin()

### Return Value

The current amount of the account funds reserved for maintaining trade positions

# IMTAccount::Margin

Set the current value of the account margin.

C++
    
    
    MTAPIRES  IMTAccount::Margin(
       const double  margin      // Margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Margin(
       double        margin      // Margin
       )

### Parameters

**margin**  
[in] The amount of the account funds reserved for maintaining trade positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
