[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardWidgetClear

[Previous](DashboardWidgetAppend.md) | [Next](DashboardWidgetDelete.md)

# IMTReportAPI::DashboardWidgetClear

Remove all widgets from a dashboard.
    
    
    MTAPIRES  IMTReportAPI::DashboardWidgetClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After calling this method, all previously created widgets are deleted ([IMTReportDashboardWidget](../../Dashboard-Interfaces/IMTReportDashboardWidget.md) objects). Data sets ([IMTDataset](../../Dataset-Interfaces/IMTDataset.md) and [IMTReportDashboardHtml](../../Dashboard-Interfaces/IMTReportDashboardHtml.md)) bound to them are not deleted.
