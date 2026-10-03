[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [Charts](../Charts.md) / ChartCreateSeries

[Previous](ChartCreate.md) | [Next](ChartWriteHtml.md)

# IMTReportAPI::ChartCreateSeries

Create a data series object for a chart.
    
    
    IMTReportSeries*  IMTReportAPI::ChartCreateSeries()

### Return Value

It returns a pointer to the created object that implements the [IMTReportSeries](../../../Diagram-Interfaces/IMTReportSeries.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTReporSeries::Release](../../../Diagram-Interfaces/IMTReportSeries/Release.md) method of this object.
