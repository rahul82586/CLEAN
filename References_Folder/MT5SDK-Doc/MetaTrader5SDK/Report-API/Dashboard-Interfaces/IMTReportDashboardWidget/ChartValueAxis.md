[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / ChartValueAxis

[Previous](ChartStackType.md) | [Next](Flags.md)

# IMTReportDashboardWidget::ChartValueAxis

Receive the type of the value axis for the chart.
    
    
    UINT  IMTReportDashboardWidget::ChartValueAxis()  const

### Return Value

A value from the [IMTReportDashboardWidget::EnChartValueAxis (#enchartvalueaxis)](Enumerations.md#enchartvalueaxis) enumeration.

# IMTReportDashboardWidget::ChartValueAxis

Set the type of the value axis for the chart.
    
    
    MTAPIRES  IMTReportDashboardWidget::ChartValueAxis(
       const UINT  value_axis  // The axis type
       )

### Parameters

**value_axis**  
[in] The axis type. The type is passed using theIMTReportDashboardWidget::EnChartValueAxisenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
