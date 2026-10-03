[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / MarginLevel

[Previous](MarginFree.md) | [Next](MarginLeverage.md)

# IMTAccount::MarginLevel

Get the margin level as a percentage.

C++
    
    
    double  IMTAccount::MarginLevel()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.MarginLevel()

### Return Value

The margin level, calculated as a percentage of the account equity ([IMTAccount::Equity](Equity.md)) to the amount of margin ([IMTAccount::Margin](Margin.md)).

# IMTAccount::MarginLevel

Set the margin level as a percentage.

C++
    
    
    MTAPIRES  IMTAccount::MarginLevel(
       const double  margin_level      // Margin level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.MarginLevel(
       double        margin_level      // Margin level
       )

### Parameters

**margin_level**  
[in] The margin level as a percentage.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
