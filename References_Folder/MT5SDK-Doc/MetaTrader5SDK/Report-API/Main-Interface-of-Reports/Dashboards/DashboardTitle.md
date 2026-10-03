[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardTitle

[Previous](DashboardHeight.md) | [Next](DashboardFlags.md)

# IMTReportDashboardWidget::Title

Get a dashboard title.
    
    
    LPCWSTR  IMTReportDashboardWidget::Title()  const

### Return Value

If successful, it returns a pointer to the string with the chart name. Otherwise, it returns NULL.

# IMTReportDashboardWidget::Title

Set a dashboard title.
    
    
    MTAPIRES  IMTReportDashboardWidget::Title(
       LPCWSTR  title      // title
       )

### Parameters

**title**  
[in] Dashboard title.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum title length is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
