[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Assign

[Previous](Enumerations.md) | [Next](Clear.md)

# IMTReportDashboardWidget::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTReportDashboardWidget::Assign(
       const IMTReportDashboardWidget*  data  // source object
       )

### Parameters

**data**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
