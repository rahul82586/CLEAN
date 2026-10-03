[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / SOMargin

[Previous](SOEquity.md) | [Next](BlockedCommission.md)

# IMTAccount::SOMargin

Get the margin amount on an account at the time of reaching the Stop Out level.

C++
    
    
    double  IMTAccount::SOMargin()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.SOMargin()

### Return Value

The volume of [margin](Margin.md) on the account at the time it reaches the Stop Out level.

# IMTAccount::SOMargin

Set the margin amount on an account at the time of reaching the Stop Out level.

C++
    
    
    MTAPIRES  IMTAccount::SOMargin(
       const double  margin      // Margin
       )

.NET (Gateway/Manager API)
    
    
    MTAPIRES  CIMTAccount.SOMargin(
       double        margin      // Margin
       )

### Parameters

**margin**  
[in] The margin amount on an account at the time of reaching the Stop Out level.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
