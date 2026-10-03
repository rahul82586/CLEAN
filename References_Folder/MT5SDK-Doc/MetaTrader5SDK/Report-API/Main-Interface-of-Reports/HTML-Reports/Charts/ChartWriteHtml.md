[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [Charts](../Charts.md) / ChartWriteHtml

[Previous](ChartCreateSeries.md) | [Next](../../Tabular-Reports.md)

# IMTReportAPI::ChartWriteHtml

Output of a chart to an HTML report.
    
    
    MTAPIRES  IMTReportAPI::ChartWriteHtml(
       const IMTReportChart*  chart      // the chart object
       )

### Parameters

**chart**  
[in]The chart object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method can be used only for HTML reports ([MTReportInfo::TYPE_HTML) (#entypes)](../../../../Structures/MTReportInfo.md#entypes).
