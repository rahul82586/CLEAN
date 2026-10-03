[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / SOEquity

[Previous](SOLevel.md) | [Next](SOMargin.md)

# IMTAccount::SOEquity

Get the account equity at the time of reaching the Stop Out level.

C++
    
    
    double  IMTAccount::SOEquity()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.SOEquity()

### Return Value

The amount of funds ([IMTAccount::Equity](Equity.md)) on the account at the time it reaches the Stop Out level.

# IMTAccount::SOEquity

Set the account equity at the time of reaching the Stop Out level.

C++
    
    
    MTAPIRES  IMTAccount::SOEquity(
       const double  equity      // Equity
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.SOEquity(
       double        equity      // Equity
       )

### Parameters

**equity**  
[in] The amount of funds (IMTAccount::Equity) on the account at the time it reaches the Stop Out level.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
