[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Height

[Previous](Width.md) | [Next](Left.md)

# IMTReportDashboardWidget::Height

Get a widget height.
    
    
    UINT  IMTReportDashboardWidget::Height()  const

### Return Value

Widget height in pixels.

# IMTReportDashboardWidget::Height

Set a widget width.
    
    
    MTAPIRES  IMTReportDashboardWidget::Height(
       const UINT  height      // height
       )

### Parameters

**height**  
[in] Widget height in pixels.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To adjust a height according to the dashboard size, use the [IMTReportDashboardWidget::WIDGET_FLAG_AUTO_HEIGHT (#enwidgetflags)](Enumerations.md#enwidgetflags) flag.
