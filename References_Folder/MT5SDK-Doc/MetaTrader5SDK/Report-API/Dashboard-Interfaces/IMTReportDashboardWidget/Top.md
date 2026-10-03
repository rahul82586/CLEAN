[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Top

[Previous](Left.md) | [Next](Html.md)

# IMTReportDashboardWidget::Top

Get a widget indent from the upper dashboard border.
    
    
    UINT  IMTReportDashboardWidget::Top()  const

### Return Value

Offset from the upper border in pixels.

# IMTReportDashboardWidget::Top

Set a widget indent from the upper dashboard border.
    
    
    MTAPIRES  IMTReportDashboardWidget::Top(
       const UINT  left       // offset from the right border
       )

### Parameters

**height**  
[in] Offset from the upper border in pixels.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

For dashboard auto top alignment, use the [IMTReportDashboardWidget::WIDGET_FLAG_AUTO_TOP (#enwidgetflags)](Enumerations.md#enwidgetflags) flag.
