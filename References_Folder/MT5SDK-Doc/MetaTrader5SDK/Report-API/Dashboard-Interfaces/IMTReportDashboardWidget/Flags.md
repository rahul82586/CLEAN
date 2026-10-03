[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Flags

[Previous](ChartValueAxis.md) | [Next](Width.md)

# IMTReportDashboardWidget::Flags

Get widget display flags.
    
    
    UINT64  IMTReportDashboardWidget::Flags()  const

### Return Value

[IMTReportDashboardWidget::EnWidgetFlags (#enwidgetflags)](Enumerations.md#enwidgetflags) enumeration value.

# IMTReportDashboardWidget::Flags

Set widget display flags.
    
    
    MTAPIRES  IMTReportDashboardWidget::Flags(
       const UINT64  flags      // flags
       )

### Parameters

**flags**  
[in] Widget display flags. TheIMTReportDashboardWidget::EnWidgetFlagsenumeration is used to pass them.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
