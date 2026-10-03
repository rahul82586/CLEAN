[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / ChartStackType

[Previous](Type.md) | [Next](ChartValueAxis.md)

# IMTReportDashboardWidget::ChartStackType

Get a default accumulation type for the widget diagram.
    
    
    UINT  IMTReportDashboardWidget::ChartStackType()  const

### Return Value

The [IMTReportDashboardWidget::EnChartStackType (#enchartstacktype)](Enumerations.md#enchartstacktype) enumeration value.

# IMTReportDashboardWidget::ChartStackType

Set a default accumulation type for the widget diagram.
    
    
    MTAPIRES  IMTReportDashboardWidget::ChartStackType(
       const UINT  stack_type  // accumulation types
       )

### Parameters

**type**  
[in] Accumulation type. TheIMTReportDashboardWidget::EnChartStackTypeenumeration is used to pass it.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method sets only a default value. Diagram accumulation type can be changed in its context menu in the Manager terminal.
