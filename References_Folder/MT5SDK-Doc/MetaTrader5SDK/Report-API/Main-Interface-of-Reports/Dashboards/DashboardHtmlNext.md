[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardHtmlNext

[Previous](DashboardHtmlTotal.md) | [Next](DashboardWidgetAppend.md)

# IMTReportAPI::DashboardHtmlNext

Get a description of an HTML data set by index.
    
    
    IMTDataset*  IMTReportAPI::DashboardHtmlNext(
       const UINT       pos          // data set position
       )

### Parameters

**pos**  
[in] Data set position beginning with 0.

### Return Value

Pointer to the [IMTReportDashboardHtml](../../Dashboard-Interfaces/IMTReportDashboardHtml.md) HTML data set object.
