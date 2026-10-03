[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Left

[Previous](Height.md) | [Next](Top.md)

# IMTReportDashboardWidget::Left

Get a widget indent from the left dashboard border.
    
    
    UINT  IMTReportDashboardWidget::Left()  const

### Return Value

Offset from the left border in pixels.

# IMTReportDashboardWidget::Left

Set a widget indent from the left dashboard border.
    
    
    MTAPIRES  IMTReportDashboardWidget::Left(
       const UINT  left       // offset from the left border
       )

### Parameters

**height**  
[in] Offset from the left border in pixels.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

For dashboard auto left alignment, use the [IMTReportDashboardWidget::WIDGET_FLAG_AUTO_LEFT (#enwidgetflags)](Enumerations.md#enwidgetflags) flag.
