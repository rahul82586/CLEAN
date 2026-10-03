[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueNextDouble

[Previous](ValueNextInt.md) | [Next](ValueShift.md)

# IMTReportSeries::ValueNextDouble

Get the value with a floating point at the indicated series position.
    
    
    MTAPIRES  IMTReportSeries::ValueNextDouble(
       const UINT  pos,       // Position
       double&     value      // Reference to the value
       )  const

### Parameters

**pos**  
[in] Value position, starting with 0.

**value**  
[out] A reference to the value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

In case a requested value is not a figure with a floating point, the method will return 0.
