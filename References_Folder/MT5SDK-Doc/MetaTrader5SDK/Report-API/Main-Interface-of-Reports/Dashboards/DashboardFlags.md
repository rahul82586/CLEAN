[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardFlags

[Previous](DashboardTitle.md) | [Next](DashboardHtmlAppend.md)

# IMTReportDashboardWidget::Flags

Get dashboard display flags.
    
    
    UINT64  IMTReportDashboardWidget::Flags()  const

### Return Value

[IMTReportDashboardWidget::EnWidgetFlags (#enwidgetflags)](../../Dashboard-Interfaces/IMTReportDashboardWidget/Enumerations.md#enwidgetflags) enumeration value.

### Note

The method is reserved for future use.

# IMTReportDashboardWidget::Flags

Set dashboard display flags.
    
    
    MTAPIRES  IMTReportDashboardWidget::Flags(
       const UINT64  flags      // flags
       )

### Parameters

**flags**  
[in] Dashboard display flags. TheIMTReportAPI::EnDashboardFlagsenumeration is used to pass them.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is reserved for future use.
