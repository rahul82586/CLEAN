[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueNextInt

[Previous](ValueNext.md) | [Next](ValueNextDouble.md)

# IMTReportSeries::ValueNextInt

Get the integer value at the indicated series position.
    
    
    MTAPIRES  IMTReportSeries::ValueNextInt(
       const UINT  pos,       // Position
       INT64&      value      // Reference to the value
       )  const

### Parameters

**pos**  
[in] Value position, starting with 0.

**value**  
[out] A reference to the value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

In case a requested value is not an integer figure, the method will return 0.
