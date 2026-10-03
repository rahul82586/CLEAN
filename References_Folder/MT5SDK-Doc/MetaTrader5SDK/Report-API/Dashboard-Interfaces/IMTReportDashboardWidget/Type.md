[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Type

[Previous](Description.md) | [Next](ChartStackType.md)

# IMTReportDashboardWidget::Type

Get a default display type for the widget diagram.
    
    
    UINT  IMTReportDashboardWidget::Type()  const

### Return Value

[IMTReportDashboardWidget::EnWidgetType (#enwidgettype)](Enumerations.md#enwidgettype) enumeration value.

# IMTReportDashboardWidget::Type

Set a default display type for the widget diagram.
    
    
    MTAPIRES  IMTReportDashboardWidget::Type(
       const UINT  type      // diagram type
       )

### Parameters

**type**  
[in] Diagram type. TheIMTReportDashboardWidget::EnWidgetTypeenumeration is used to pass it.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method sets only a default value. Diagram type can be changed in its context menu in the Manager terminal.
