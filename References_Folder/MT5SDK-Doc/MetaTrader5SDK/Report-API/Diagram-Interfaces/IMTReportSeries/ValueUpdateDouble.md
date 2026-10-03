[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueUpdateDouble

[Previous](ValueUpdateInt.md) | [Next](ValueNext.md)

# IMTReportSeries::ValueUpdateDouble

Change the value with a floating point at the indicated series position.
    
    
    MTAPIRES  IMTReportSeries::ValueUpdateDouble(
       const UINT    pos,       // Position
       const double  value      // Value
       )

### Parameters

**pos**  
[in] Changed value position, starting with 0.

**value**  
[in] Changed value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
