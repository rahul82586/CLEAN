[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / Data

[Previous](Html.md) | [Next](DataColumnTitle.md)

# IMTReportDashboardWidget::Data

Get a data set related to the widget.
    
    
    IMTDataset*  IMTReportDashboardWidget::Data()  const

### Return Value

# IMTReportDashboardWidget::Data

Bind a data set to the widget.
    
    
    MTAPIRES  IMTReportDashboardWidget::Data(
       IMTDataset*  data   // data set object
       )

### Parameters

**chart**  
[in]Data set object. To create an object, useIMTReportAPI::DatasetAppend.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

A data set is displayed in a widget as diagrams or tables.

### 
