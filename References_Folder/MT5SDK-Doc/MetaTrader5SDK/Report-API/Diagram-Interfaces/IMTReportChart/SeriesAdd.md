[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesAdd

[Previous](SeriesClear.md) | [Next](SeriesAddCopy.md)

# IMTReportChart::SeriesAdd

Add data series to a chart.
    
    
    MTAPIRES  IMTReportChart::SeriesAdd(
       IMTReportSeries*  series      // Data series object
       )

### Parameters

**series**  
[in]Data seriesobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method places a pointer to a passed object at a chart object. After a successful call of this method, the control over the life time of the series object is passed to the chart object. Thus, when deleting a chart object ([IMTReportChart::Release](Release.md) call), an earlier inserted object will be automatically removed.
