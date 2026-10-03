[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardWidgetAppend

[Previous](DashboardHtmlNext.md) | [Next](DashboardWidgetClear.md)

# IMTReportAPI::DashboardWidgetAppend

Add a widget to a dashboard.
    
    
    IMTReportDashboardWidget*  IMTReportAPI::DashboardWidgetAppend()

### Return Value

Pointer to the created [IMTReportDashboardWidget](../../Dashboard-Interfaces/IMTReportDashboardWidget.md) widget object.

### Note

The method creates a widget bound to the dashboard and returns a pointer to it. To display data in the widget, bind a data set to it using the [IMTReportDashboardWidget::Data](../../Dashboard-Interfaces/IMTReportDashboardWidget/Data.md) or [IMTReportDashboardWidget::Html](../../Dashboard-Interfaces/IMTReportDashboardWidget/Html.md) method.

### 
