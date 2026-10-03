[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / MarginFree

[Previous](Margin.md) | [Next](MarginLevel.md)

# IMTAccount::MarginFree

Get the free margin of an account.

C++
    
    
    double  IMTAccount::MarginFree()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.MarginFree()

### Return Value

The free margin of an account.

# IMTAccount::MarginFree

Set the free margin of an account.

C++
    
    
    MTAPIRES  IMTAccount::MarginFree(
       const double  margin_free      // Free margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.MarginFree(
       double        margin_free      // Free margin
       )

### Parameters

**margin_free**  
[in] The free margin of an account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
