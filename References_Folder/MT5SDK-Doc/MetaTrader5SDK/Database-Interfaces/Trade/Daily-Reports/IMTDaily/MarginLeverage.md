[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / MarginLeverage

[Previous](MarginLevel.md) | [Next](Profit.md)

# IMTDaily::MarginLeverage

Get the margin leverage of a client in the daily report.

C++
    
    
    UINT  IMTDaily::MarginLeverage()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDaily.MarginLeverage()

### Return Value

The margin leverage of a client in the daily report.

# IMTDaily::MarginLeverage

Set the margin leverage of a client in the daily report.

C++
    
    
    MTAPIRES  IMTDaily::MarginLeverage(
       const UINT  leverage      // Leverage
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.MarginLeverage(
       uint        leverage      // Leverage
       )

### Parameters

**leverage**  
[in] The margin leverage of a client in the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
