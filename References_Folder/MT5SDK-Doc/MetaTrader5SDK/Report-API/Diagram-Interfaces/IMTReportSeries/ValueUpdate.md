[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueUpdate

[Previous](ValueAddDouble.md) | [Next](ValueUpdateInt.md)

# IMTReportSeries::ValueUpdate

Change the value at the indicated series position.
    
    
    MTAPIRES  IMTReportSeries::ValueUpdate(
       const UINT  pos,       // Position
       LPCWSTR     value      // Value
       )

### Parameters

**pos**  
[in] Changed value position, starting with 0.

**value**  
[in] Changed value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
