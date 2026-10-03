[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueAddInt

[Previous](ValueAdd.md) | [Next](ValueAddDouble.md)

# IMTReportSeries::ValueAddInt

Add integer value to a series.
    
    
    MTAPIRES  IMTReportSeries::ValueAddInt(
       const INT64  value      // Value
       )

### Parameters

**value**  
[in] Integer value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
