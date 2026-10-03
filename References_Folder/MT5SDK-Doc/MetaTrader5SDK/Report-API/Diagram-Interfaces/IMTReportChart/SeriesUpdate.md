[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesUpdate

[Previous](SeriesDetach.md) | [Next](SeriesShift.md)

# IMTReportChart::SeriesUpdate

Change a data series at the specified position of a chart.
    
    
    MTAPIRES  IMTReportChart::SeriesUpdate(
       const UINT        pos,        // Series position
       IMTReportSeries*  series      // Series object
       )

### Parameters

**pos**  
[in] Position of a data series, starting with 0.

**series**  
[in]Data seriesobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The Update method deletes the previous element (call of [IMTReportSeries::Release](../IMTReportSeries/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by a chart object. Thus, when deleting a chart object ([IMTReportChart::Release](Release.md) call), an earlier inserted object will be automatically removed.
