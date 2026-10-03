[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Title

[Previous](Clear.md) | [Next](Description.md)

# IMTReportDashboardWidget::Title

Get a widget title.
    
    
    LPCWSTR  IMTReportDashboardWidget::Title()  const

### Return Value

If successful, it returns a pointer to the string with the chart name. Otherwise, it returns NULL.

# IMTReportDashboardWidget::Title

Set a widget title.
    
    
    MTAPIRES  IMTReportDashboardWidget::Title(
       LPCWSTR  title      // title
       )

### Parameters

**title**  
[in] Widget title.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum header length is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it is cut to this length.
