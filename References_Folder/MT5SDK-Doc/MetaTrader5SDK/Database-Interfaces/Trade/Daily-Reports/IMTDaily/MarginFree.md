[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / MarginFree

[Previous](Margin.md) | [Next](MarginLevel.md)

# IMTDaily::MarginFree

Get a client's free margin in a daily report.

C++
    
    
    double  IMTDaily::MarginFree()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.MarginFree()

### Return Value

A client's free margin in a daily report.

# IMTDaily::MarginFree

Set a client's free margin in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::MarginFree(
       const double  margin_free      // Free margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.MarginFree(
       double        margin_free      // Free margin
       )

### Parameters

**margin_free**  
[in] A client's free margin in the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
