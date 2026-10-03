[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dataset](../Dataset.md) / Append

[Previous](../Dataset.md) | [Next](Clear.md)

# IMTReportAPI::DatasetAppend

Add a data set to a dashboard.
    
    
    IMTDataset*  IMTReportAPI::DatasetAppend()

### Return Value

Pointer to the created [IMTDataset](../../Dataset-Interfaces/IMTDataset.md) tabular data set object.

### Note

The method creates a data set bound to the dashboard and returns a pointer to it. To display a data set, it should be bound to the widget using the [IMTReportDashboardWidget::Data](../../Dashboard-Interfaces/IMTReportDashboardWidget/Data.md) method. The widget in turn should be created by the [IMTReportAPI::DashboardWidgetAppend](../Dashboards/DashboardWidgetAppend.md) method.

### 
