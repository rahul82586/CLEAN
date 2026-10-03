[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardWidgetNext

[Previous](DashboardWidgetTotal.md) | [Next](../Configuration-Databases.md)

# IMTReportAPI::DashboardWidgetNext

Get a widget description by index.
    
    
    IMTReportDashboardWidget*  IMTReportAPI::DashboardWidgetNext(
       const UINT       pos          // widget position
       )

### Parameters

**pos**  
[in] Widget position beginning with 0.

### Return Value

Pointer to the widget object [IMTReportDashboardWidget](../../Dashboard-Interfaces/IMTReportDashboardWidget.md).
