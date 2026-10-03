[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueAddDouble

[Previous](ValueAddInt.md) | [Next](ValueUpdate.md)

# IMTReportSeries::ValueAddDouble

Add a value with a floating point to a series.
    
    
    MTAPIRES  IMTReportSeries::ValueAddDouble(
       const double  value      // Value
       )

### Parameters

**value**  
[in] Value with a floating point.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
