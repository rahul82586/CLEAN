[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / DataColumnShift

[Previous](DataColumnDelete.md) | [Next](DataColumnTotal.md)

# IMTDataset::DataColumnDelete

Change column position in the display rules.
    
    
    MTAPIRES  IMTDataset::DataColumnDelete(
       const UINT  pos,       // column position
       const int   shift      // shift
       )

### Parameters

**pos**  
[in] Column position beginning from 0.

**shift**  
[in] Shift of a column relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Columns from [IMTDataset](../../Dataset-Interfaces/IMTDataset.md) are displayed in a widget in the order specified in the DataColumn array.
