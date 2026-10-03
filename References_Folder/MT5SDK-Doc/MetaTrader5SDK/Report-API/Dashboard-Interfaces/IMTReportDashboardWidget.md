[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Dashboard Interfaces](../Dashboard-Interfaces.md) / IMTReportDashboardWidget

[Previous](IMTReportDashboardHtml/TplProcess.md) | [Next](IMTReportDashboardWidget/Enumerations.md)

# IMTReportDashboardWidget

A widget is a separate type of presentation that can be used on a dashboard. It allows presenting data as HTML content, chart and/or table. The IMTReportDashboardWidget interface allows managing its properties and contents.

Method | Purpose  
---|---  
[Assign](IMTReportDashboardWidget/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTReportDashboardWidget/Clear.md) | Clear an object.  
[Title](IMTReportDashboardWidget/Title.md) | Get and set a widget title.  
[Description](IMTReportDashboardWidget/Description.md) | Get and set widget description.  
[Type](IMTReportDashboardWidget/Type.md) | Get and set a default display type for the widget diagram.  
[ChartStackType](IMTReportDashboardWidget/ChartStackType.md) | Get and set a default accumulation type for the widget diagram.  
[ChartValueAxis](IMTReportDashboardWidget/ChartValueAxis.md) | Get and set the type of the value axis for the chart.  
[Flags](IMTReportDashboardWidget/Flags.md) | Get and set widget display flags.  
[Width](IMTReportDashboardWidget/Width.md) | Get and set a widget width.  
[Height](IMTReportDashboardWidget/Height.md) | Get and set a widget height.  
[Left](IMTReportDashboardWidget/Left.md) | Get and set a widget indent from the left dashboard border.  
[Top](IMTReportDashboardWidget/Top.md) | Get and set a widget indent from the upper dashboard border.  
[Html](IMTReportDashboardWidget/Html.md) | Get and add data for displaying in the widget as HTML content.  
[Data](IMTReportDashboardWidget/Data.md) | Get and add data for displaying in the widget as a diagram and/or table.  
[DataColumnTitle](IMTReportDashboardWidget/DataColumnTitle.md) | Get and set an ID of a column containing headers of all the remaining table columns.  
[DataColumnClear](IMTReportDashboardWidget/DataColumnClear.md) | Clear the widget columns display rules.  
[DataColumnAdd](IMTReportDashboardWidget/DataColumnAdd.md) | Add the column to the display rules.  
[DataColumnDelete](IMTReportDashboardWidget/DataColumnDelete.md) | Delete a column from the display rules.  
[DataColumnShift](IMTReportDashboardWidget/DataColumnShift.md) | Change column position in the display rules.  
[DataColumnTotal](IMTReportDashboardWidget/DataColumnTotal.md) | Get the number of columns in the display rules.  
[DataColumnNext](IMTReportDashboardWidget/DataColumnNext.md) | Get column ID by its position in the display rules.  
  
  * Use [IMTReportAPI::DashboardWidgetAppend](../Main-Interface-of-Reports/Dashboards/DashboardWidgetAppend.md) to create a widget object.
  * The IMTReportDashboardWidget::DataColumn* method group defines what columns from the [IMTDataset](../Dataset-Interfaces/IMTDataset.md) data set are to be displayed in the dashboard widget, as well as their display order. If the DataColumn array is empty, all columns are displayed in the order they are added to IMTDataset. The values from the first column are to be used as headers.

  
---  
  
The IMTReportDashboardWidget interface contains the following enumerations:

Interface | Purpose  
---|---  
[EnWidgetType (#enwidgettype)](IMTReportDashboardWidget/Enumerations.md#enwidgettype) | Types of diagrams and widget contents.  
[EnChartStackType (#enchartstacktype)](IMTReportDashboardWidget/Enumerations.md#enchartstacktype) | Accumulation types for widget diagrams.  
[EnWidgetFlags (#enwidgetflags)](IMTReportDashboardWidget/Enumerations.md#enwidgetflags) | Widget display flags.
