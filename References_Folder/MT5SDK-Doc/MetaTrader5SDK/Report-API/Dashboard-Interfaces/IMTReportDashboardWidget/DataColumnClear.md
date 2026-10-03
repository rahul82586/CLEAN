[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / DataColumnClear

[Previous](DataColumnTitle.md) | [Next](DataColumnAdd.md)

# IMTReportDashboardWidget::DataColumnClear

Clear the widget column display rules.
    
    
    MTAPIRES  IMTReportDashboardWidget::DataColumnClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The DataColumn array displays the order of displaying columns from [IMTDataset](../../Dataset-Interfaces/IMTDataset.md) in the widget. If the array is empty, all columns are displayed. The first one is used as the header.
