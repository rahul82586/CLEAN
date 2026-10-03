[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesNext

[Previous](SeriesTotal.md) | [Next](../../Dataset-Interfaces.md)

# IMTReportChart::SeriesNext

Get an object of a [data series](../IMTReportSeries.md) by its position.
    
    
    IMTReportSeries*  IMTReportChart::SeriesNext(
       const UINT  pos      // Position
       )

### Parameters

**pos**  
[in] Position of a data series, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the data series object at the specified chart object position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current chart object. Thus, when deleting a chart object, the returned pointer will be invalid.
