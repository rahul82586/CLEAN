[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Main Interface of Reports](../Main-Interface-of-Reports.md) / Dashboards

[Previous](Tabular-Reports/Totals/TableSummaryTotal.md) | [Next](Dashboards/DashboardWidth.md)

# Dashboards

Dashboards form a separate type of reports that allow combining different data and their presentation on one sheet.

A dashboard consists of widgets representing data either in the form of HTML content, or in the form of a diagram and/or table. A set of tabular data ([IMTDataset](../Dataset-Interfaces/IMTDataset.md)) or HTML data ([IMTReportDashboardHtml](../Dashboard-Interfaces/IMTReportDashboardHtml.md)) can be used as a data source. The data set is bound to the widget using the [IMTReportDashboardWidget::Html](../Dashboard-Interfaces/IMTReportDashboardWidget/Html.md) or [IMTReportDashboardWidget::Data](../Dashboard-Interfaces/IMTReportDashboardWidget/Data.md) method depending on its type. The same data set can be used in different widgets, for example for displaying the same data in different ways or displaying different parts of data sets in separate tables.

The following functions are provided for managing dashboards:

Function | Purpose  
---|---  
[DashboardWidth](Dashboards/DashboardWidth.md) | Get and set a dashboard width.  
[DashboardHeight](Dashboards/DashboardHeight.md) | Get and set a dashboard height.  
[DashboardTitle](Dashboards/DashboardTitle.md) | Get and set a dashboard title.  
[DashboardFlags](Dashboards/DashboardFlags.md) | Get and set dashboard display flags.  
[DashboardHtmlAppend](Dashboards/DashboardHtmlAppend.md) | Add a set of HTML data to a dashboard.  
[DashboardHtmlClear](Dashboards/DashboardHtmlClear.md) | Delete all dashboard HTML data.  
[DashboardHtmlDelete](Dashboards/DashboardHtmlDelete.md) | Delete a set of HTML data from a dashboard.  
[DashboardHtmlTotal](Dashboards/DashboardHtmlTotal.md) | Get a number of HTML data sets in a dashboard.  
[DashboardHtmlNext](Dashboards/DashboardHtmlNext.md) | Get a description of an HTML data set by index.  
[DashboardWidgetAppend](Dashboards/DashboardWidgetAppend.md) | Add a widget to a dashboard.  
[DashboardWidgetClear](Dashboards/DashboardWidgetClear.md) | Remove all widgets from a dashboard.  
[DashboardWidgetDelete](Dashboards/DashboardWidgetDelete.md) | Remove a widget from a dashboard.  
[DashboardWidgetTotal](Dashboards/DashboardWidgetTotal.md) | Get a number of widgets in a dashboard.  
[DashboardWidgetNext](Dashboards/DashboardWidgetNext.md) | Get a widget description by index.
