[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / SOLevel

[Previous](SOTime.md) | [Next](SOEquity.md)

# IMTAccount::SOLevel

Get the margin level of an account at the time of reaching the Stop Out level.

C++
    
    
    double  IMTAccount::SOLevel()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.SOLevel()

### Return Value

[The margin level](MarginLevel.md) of an account at the time it reaches the Stop Out level.

# IMTAccount::SOLevel

Set the margin level of an account at the time of reaching the Stop Out level.

C++
    
    
    MTAPIRES  IMTAccount::SOLevel(
       const double  level      // Margin level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.SOLevel(
       double        level      // Margin level
       )

### Parameters

**level**  
[In] The margin level of an account at the time it reaches the Stop Out level.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
