[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / DataColumnTitle

[Previous](Data.md) | [Next](DataColumnClear.md)

# IMTReportDashboardWidget::DataColumnTitle

Get an ID of a column containing headers of all the remaining table columns.
    
    
    UINT  IMTReportDashboardWidget::DataColumnTitle()  const

### Return Value

Offset from the left border in pixels.

### Note

The [IMTDatasetColumn::ColumnId](../../Dataset-Interfaces/IMTDatasetColumn/ColumnID.md) value is used as the ID.

# IMTReportDashboardWidget::DataColumnTitle

Set a column containing the values to be used as headers of the remaining table columns.
    
    
    MTAPIRES  IMTReportDashboardWidget::DataColumnTitle(
       const UINT  column_id     // column ID
       )

### Parameters

**column_id**  
[in] Column ID containing the values to be used as headers of the remaining columns. TheIMTDatasetColumn::ColumnIdvalue is used as the ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If a header column is not explicitly defined, the first column from [IMTDataset](../../Dataset-Interfaces/IMTDataset.md) is used by default.
