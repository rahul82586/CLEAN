[🏠 Document Start](../README.md) / [Report API](README.md) / Dashboard Interfaces

[Previous](Main-Interface-of-Reports/Geo-Services/GeoResolveBatch.md) | [Next](Dashboard-Interfaces/IMTReportDashboardHtml.md)

# Interfaces of dashboards

Dashboards form a separate type of reports that allow combining different data and their presentation on one sheet.

A dashboard consists of widgets representing data either in the form of HTML content, or in the form of a diagram and/or table. A set of tabular data ([IMTDataset](Dataset-Interfaces/IMTDataset.md)) or HTML data ([IMTReportDashboardHtml](Dashboard-Interfaces/IMTReportDashboardHtml.md)) can be used as a data source. The data set is bound to the widget using the [IMTReportDashboardWidget::Html](Dashboard-Interfaces/IMTReportDashboardWidget/Html.md) or [IMTReportDashboardWidget::Data](Dashboard-Interfaces/IMTReportDashboardWidget/Data.md) method depending on its type. The same data set can be used in different widgets, for example for displaying the same data in different ways or displaying different parts of data sets in separate tables.

Three interfaces are provided for working with data and widget representation:

  * [IMTDataset](Dataset-Interfaces/IMTDataset.md) — methods for using a data set for widgets displaying diagrams and tables.
  * [IMTReportDashboardHtml](Dashboard-Interfaces/IMTReportDashboardHtml.md) — methods for working with data for widgets displaying HTML content.
  * [IMTReportDashboardWidget](Dashboard-Interfaces/IMTReportDashboardWidget.md) — methods for working with widget settings: general parameters, alignment and content presentation.


