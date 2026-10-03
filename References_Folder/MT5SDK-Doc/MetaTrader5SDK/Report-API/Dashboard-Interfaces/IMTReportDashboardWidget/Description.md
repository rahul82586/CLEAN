[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Description

[Previous](Title.md) | [Next](Type.md)

# IMTReportDashboardWidget::Description

Get the widget description.
    
    
    LPCWSTR  IMTReportDashboardWidget::Description()  const

### Return Value

If successful, it returns a pointer to the string with the description. Otherwise, NULL is returned.

# IMTReportDashboardWidget::Description

Set the widget description.
    
    
    MTAPIRES  IMTReportDashboardWidget::Description(
       LPCWSTR  description   // Description
       )

### Parameters

**description**  
[in] The widget description.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum description length is 256 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
