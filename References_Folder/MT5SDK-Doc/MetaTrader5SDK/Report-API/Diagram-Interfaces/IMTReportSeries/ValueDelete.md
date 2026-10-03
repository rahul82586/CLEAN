[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueDelete

[Previous](ValueShift.md) | [Next](ValueDescription.md)

# IMTReportSeries::ValueDelete

Delete the value at the indicated series position.
    
    
    MTAPIRES  IMTReportSeries::ValueDelete(
       const UINT  pos      // Position
       )

### Parameters

**pos**  
[in] Deleted value position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
