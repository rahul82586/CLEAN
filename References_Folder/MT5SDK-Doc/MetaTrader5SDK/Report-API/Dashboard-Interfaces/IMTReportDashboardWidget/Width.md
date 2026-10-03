[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Width

[Previous](Flags.md) | [Next](Height.md)

# IMTReportDashboardWidget::Width

Get the widget width.
    
    
    UINT  IMTReportDashboardWidget::Width()  const

### Return Value

Widget width in pixels.

# IMTReportDashboardWidget::Width

Set widget width.
    
    
    MTAPIRES  IMTReportDashboardWidget::Width(
       const UINT  width      // width
       )

### Parameters

**width**  
[in] Widget width in pixels.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To adjust a width according to the dashboard size, use the [IMTReportDashboardWidget::WIDGET_FLAG_AUTO_WIDTH (#enwidgetflags)](Enumerations.md#enwidgetflags) flag.
