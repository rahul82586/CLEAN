[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [Charts](../Charts.md) / ChartCreate

[Previous](../Charts.md) | [Next](ChartCreateSeries.md)

# IMTReportAPI::ChartCreate

Create a chart object.
    
    
    IMTReportChart*  IMTReportAPI::ChartCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTReportChart](../../../Diagram-Interfaces/IMTReportChart.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTReportChart::Release](../../../Diagram-Interfaces/IMTReportChart/Release.md) method of this object.
