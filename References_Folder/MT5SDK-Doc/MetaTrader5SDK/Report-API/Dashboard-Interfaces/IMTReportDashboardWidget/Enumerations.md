[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Enumerations

[Previous](../IMTReportDashboardWidget.md) | [Next](Assign.md)

<a id="imtreportdashboardwidget"></a>
# IMTReportDashboardWidget (#imtreportdashboardwidget)

The [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) interface contains the following enumerations:

  * [IMTReportDashboardWidget::EnWidgetType (#enwidgettype)](Enumerations.md#enwidgettype)
  * [IMTReportDashboardWidget::EnChartStackType (#enchartstacktype)](Enumerations.md#enchartstacktype)
  * [IMTReportDashboardWidget::EnWidgetFlags (#enwidgetflags)](Enumerations.md#enwidgetflags)
  * [IMTReportDashboardWidget::EnChartValueAxis (#enchartvalueaxis)](Enumerations.md#enchartvalueaxis)



<a id="enwidgettype"></a>
## IMTReportDashboardWidget::EnWidgetType (#enwidgettype)

IMTReportDashboardWidget::EnWidgetType lists the types of widget diagrams and contents:

ID | Value | Description  
WIDGET_TYPE_CHART_BAR | 0 | Histogram.  
WIDGET_TYPE_CHART_LINE | 1 | Linear diagram.  
WIDGET_TYPE_CHART_AREA | 2 | Pie chart.  
WIDGET_TYPE_CHART_PIE | 3 | Concentric diagram.  
WIDGET_TYPE_CHART_SPLINE | 4 | Spline chart.  
WIDGET_TYPE_CHART_AREA_SPLINE | 5 | Spline chart with areas.  
WIDGET_TYPE_CHART_GEO | 6 | Geographical distribution on an interactive map.  
WIDGET_TYPE_VALUE | 100 | Single value.  
WIDGET_TYPE_TABLE | 101 | Table.  
WIDGET_TYPE_HTML | 102 | HTML content. Currently not supported.  
WIDGET_TYPE_FIRST |  | Enumeration beginning. Corresponds to WIDGET_TYPE_CHART_BAR.  
WIDGET_TYPE_LAST |  | End of enumeration. Corresponds to WIDGET_TYPE_HTML.  
  
The enumeration is used in the [IMTReportDashboardWidget::Type](Type.md) method.

<a id="enchartstacktype"></a>
## IMTReportDashboardWidget::EnChartStackType (#enchartstacktype)

IMTReportDashboardWidget::EnChartStackType lists accumulation types for widget diagrams:

ID | Value | Description  
CHART_STACK_NONE | 0 | Data series are displayed separately  
CHART_STACK_SIMPLE | 1 | Data series are combined, values are summed up  
CHART_STACK_ACCUMULATION | 2 | Data series are combined, values are summed up  
CHART_STACK_NORMALIZED | 3 | Rows are combined, the general contribution of each series to the total value in percentage is shown  
CHART_STACK_FIRST |  | Enumeration beginning. Corresponds to CHART_STACK_NONE.  
CHART_STACK_LAST |  | End of enumeration. Corresponds to CHART_STACK_NORMALIZED.  
  
The enumeration is used in the [IMTReportDashboardWidget::Type](ChartStackType.md) method.

<a id="enwidgetflags"></a>
## IMTReportDashboardWidget::EnWidgetFlags (#enwidgetflags)

IMTReportDashboardWidget::EnWidgetFlags lists widget display flags:

ID | Value | Description  
WIDGET_FLAG_NONE | 0x00000000 | No flags.  
WIDGET_FLAG_AUTO_WIDTH | 0x00000001 | Widget width is specified automatically according to the [dashboard width](../../Main-Interface-of-Reports/Dashboards/DashboardWidth.md).  
WIDGET_FLAG_AUTO_HEIGHT | 0x00000002 | Widget height is specified automatically according to the [dashboard height](../../Main-Interface-of-Reports/Dashboards/DashboardHeight.md).  
WIDGET_FLAG_AUTO_TOP | 0x00000004 | The dashboard widget is aligned to the the dashboard upper border.  
WIDGET_FLAG_AUTO_LEFT | 0x00000008 | The dashboard widget is aligned to the the dashboard left border.  
WIDGET_FLAG_HIDE_ZEROES | 0x00000100 | Zero values are hidden from the dashboard widget.  
  
The enumeration is used in the [IMTReportDashboardWidget::Flags](Flags.md) method.

<a id="enchartvalueaxis"></a>
## IMTReportDashboardWidget::EnChartValueAxis (#enchartvalueaxis)

Chart value axis types are enumerated in IMTReportDashboardWidget::EnChartValueAxis.

Identifier | Value | Description  
CHART_VALUE_AXIS_ABSOLUTE | 0 | Axis with absolute values.  
CHART_VALUE_AXIS_RELATIVE | 1 | Axis with relative values.  
CHART_VALUE_AXIS_FIRST |  | Enumeration beginning. Corresponds to CHART_VALUE_AXIS_ABSOLUTE.  
CHART_VALUE_AXIS_LAST |  | End of enumeration. Corresponds to CHART_VALUE_AXIS_RELATIVE.  
  
The enumeration is used in the [IMTReportDashboardWidget::ChartValueAxis](ChartValueAxis.md) method.
