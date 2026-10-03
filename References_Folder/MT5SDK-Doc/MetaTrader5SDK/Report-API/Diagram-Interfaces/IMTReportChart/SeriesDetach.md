[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesDetach

[Previous](SeriesDelete.md) | [Next](SeriesUpdate.md)

# IMTReportChart::SeriesDetach

Detach a data series object from a chart.
    
    
    IMTReportSeries*  IMTReportChart::SeriesDetach(
       const UINT  pos      // Series position
       )

### Parameters

**pos**  
[in] Position of a data series, starting with 0.

### Return Value

A pointer to the detached object of the [data series](../IMTReportSeries.md).

### Note

This method removes the pointer to the object at the given position of a chart object and returns it. The deleted object is not freed.
