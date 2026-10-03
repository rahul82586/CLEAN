[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Html

[Previous](Top.md) | [Next](Data.md)

# IMTReportDashboardWidget::Html

Get data displayed in the widget as HTML content.
    
    
    IMTReportDashboardHtml*  IMTReportDashboardWidget::Html()  const

### Return Value

# IMTReportDashboardWidget::Html

Add data to be displayed in the widget as HTML content.
    
    
    MTAPIRES  IMTReportDashboardWidget::Html(
       IMTReportDashboardHtml*  html   // HTML content object
       )

### Parameters

**chart**  
[in]HTML content object. To create an object, useIMTReportAPI::DashboardHtmlAppend

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

HTML data can be displayed only in the widgets of [IMTReportDashboardWidget::WIDGET_TYPE_HTML](Html.md) type.
