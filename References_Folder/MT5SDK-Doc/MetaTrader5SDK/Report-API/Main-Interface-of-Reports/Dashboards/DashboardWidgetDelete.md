[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardWidgetDelete

[Previous](DashboardWidgetClear.md) | [Next](DashboardWidgetTotal.md)

# IMTReportAPI::DashboardWidgetDelete

Remove a widget from a dashboard.
    
    
    MTAPIRES  IMTReportAPI::DashboardWidgetDelete(
       const UINT  pos      // widget position
       )

### Parameters

**pos**  
[in] Position of a widget that should be removed beginning with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When removing a widget, a data set ([IMTDataset](../../Dataset-Interfaces/IMTDataset.md) or [IMTReportDashboardHtml](../../Dashboard-Interfaces/IMTReportDashboardHtml.md)) bound to it is not deleted.
