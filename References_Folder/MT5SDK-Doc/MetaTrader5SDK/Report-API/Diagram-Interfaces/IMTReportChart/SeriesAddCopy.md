[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesAddCopy

[Previous](SeriesAdd.md) | [Next](SeriesDelete.md)

# IMTReportChart::SeriesAddCopy

Add a data series copy to a chart.
    
    
    MTAPIRES  IMTReportChart::SeriesAddCopy(
       const IMTReportSeries*  series      // Data series object
       )

### Parameters

**series**  
[in]Data seriesobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method creates a copy of the series object and places it at the chart object.
