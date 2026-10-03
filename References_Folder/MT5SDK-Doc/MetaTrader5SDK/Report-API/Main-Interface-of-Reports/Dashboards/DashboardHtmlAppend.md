[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardHtmlAppend

[Previous](DashboardFlags.md) | [Next](DashboardHtmlClear.md)

# IMTReportAPI::DashboardHtmlAppend

Add a set of HTML data to a dashboard.
    
    
    IMTReportDashboardHtml*  IMTReportAPI::DashboardHtmlAppend()

### Return Value

Pointer to the created [IMTReportDashboardHtml](../../Dashboard-Interfaces/IMTReportDashboardHtml.md) HTML data object.

### Note

The method creates a data set bound to the dashboard and returns a pointer to it. To display a data set, it should be bound to the widget using the [IMTReportDashboardWidget::Html](../../Dashboard-Interfaces/IMTReportDashboardWidget/Html.md) method. The widget in turn should be created by the [IMTReportAPI::DashboardWidgetAppend](DashboardWidgetAppend.md) method.

### 
