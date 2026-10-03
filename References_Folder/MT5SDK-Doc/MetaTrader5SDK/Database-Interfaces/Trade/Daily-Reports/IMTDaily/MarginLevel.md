[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / MarginLevel

[Previous](MarginFree.md) | [Next](MarginLeverage.md)

# IMTDaily::MarginLevel

Get a client's margin level in the daily report.

C++
    
    
    double  IMTDaily::MarginLevel()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.MarginLevel()

### Return Value

The margin level of a client in the daily report.

# IMTDaily::MarginLevel

Set a client's margin level in the daily report.

C++
    
    
    MTAPIRES  IMTDaily::MarginLevel(
       const double  margin_level      // Margin level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.MarginLevel(
       double        margin_level      // Margin level
       )

### Parameters

**margin_level**  
[in] The margin level of a client in the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
