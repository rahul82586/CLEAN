[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTReportSeries::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTReportSeries::Assign(
       const IMTReportSeries  *series      // Source object
       )

### Parameters

***series**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
