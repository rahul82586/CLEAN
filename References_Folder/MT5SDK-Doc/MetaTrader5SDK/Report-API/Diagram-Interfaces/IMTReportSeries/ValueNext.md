[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueNext

[Previous](ValueUpdateDouble.md) | [Next](ValueNextInt.md)

# IMTReportSeries::ValueNext

Get the value at the indicated series position.
    
    
    LPCWSTR  IMTReportSeries::ValueNext(
       const UINT  pos      // Position
       )  const

### Parameters

**pos**  
[in] Value position, starting with 0.

### Return Value

If successful, it returns a pointer to the string with the value. Otherwise, it returns NULL.
