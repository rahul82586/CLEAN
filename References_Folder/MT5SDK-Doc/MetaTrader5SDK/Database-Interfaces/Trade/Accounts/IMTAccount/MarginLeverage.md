[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / MarginLeverage

[Previous](MarginLevel.md) | [Next](MarginInitial.md)

# IMTAccount::MarginLeverage

Get the margin leverage.

C++
    
    
    UINT  IMTAccount::MarginLeverage()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTAccount.MarginLeverage()

### Return Value

Margin leverage.

# IMTAccount::MarginLeverage

Set the margin leverage.

C++
    
    
    MTAPIRES  IMTAccount::MarginLeverage(
       const UINT  leverage      // Leverage
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.MarginLeverage(
       uint        leverage      // Leverage
       )

### Parameters

**leverage**  
[in] Margin leverage.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
