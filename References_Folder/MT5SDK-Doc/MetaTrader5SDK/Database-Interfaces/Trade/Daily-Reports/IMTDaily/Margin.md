[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Margin

[Previous](EquityPrevMonth.md) | [Next](MarginFree.md)

# IMTDaily::Margin

Get the size of a client's margin in a daily report.

C++
    
    
    double  IMTDaily::Margin()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.Margin()

### Return Value

The size of a client's margin in a daily report.

# IMTDaily::Margin

Set the size of a client's margin in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Margin(
       const double  margin      // Margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Margin(
       double        margin      // Margin
       )

### Parameters

**margin**  
[in] The size of a client's margin in a daily report.

### Return Value

An indication of successful completion is the MT_RET_OK response code. Otherwise, an error has occurred that corresponds to the response code.
