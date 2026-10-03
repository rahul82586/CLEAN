[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueShift

[Previous](ValueNextDouble.md) | [Next](ValueDelete.md)

# IMTReportSeries::ValueShift

Shift a value in a series.
    
    
    MTAPIRES  IMTReportSeries::ValueShift(
       const UINT  pos,       // Position
       const int   shift      // Shift
       )

### Parameters

**pos**  
[in] Shifted value position, starting with 0.

**shift**  
Shift from its current position. A negative value means the shift to the top, a positive value - to the series end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
