[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueAdd

[Previous](ValueTotal.md) | [Next](ValueAddInt.md)

# IMTReportSeries::ValueAdd

Add a value to a series.
    
    
    MTAPIRES  IMTReportSeries::ValueAdd(
       LPCWSTR  value      // Value
       )

### Parameters

**value**  
[in] Added value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
