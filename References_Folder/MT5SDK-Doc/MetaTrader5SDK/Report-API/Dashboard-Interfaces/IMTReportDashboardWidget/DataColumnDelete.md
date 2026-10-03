[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / DataColumnDelete

[Previous](DataColumnAdd.md) | [Next](DataColumnShift.md)

# IMTDataset::DataColumnDelete

Delete a column from the display rules.
    
    
    MTAPIRES  IMTDataset::DataColumnDelete(
       const UINT  *column_id      // column ID
       )

### Parameters

**column_id**  
[in] Column ID. TheIMTDatasetColumn::ColumnIdvalue is used as an ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Columns from [IMTDataset](../../Dataset-Interfaces/IMTDataset.md) are displayed in a widget in the order specified in the DataColumn array.
