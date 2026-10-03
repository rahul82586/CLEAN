[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardWidget](../IMTReportDashboardWidget.md) / DataColumnNext

[Previous](DataColumnTotal.md) | [Next](../../Diagram-Interfaces.md)

# IMTReportDashboardWidget::DataColumnNext

Get column ID by its position in the display rules.
    
    
    UINT*  IMTReportDashboardWidget::DataColumnNext(
       const UINT  pos        // column position
       )

### Parameters

**pos**  
[in] Column position beginning from 0.

### Return Value

Column ID. The [IMTDatasetColumn::ColumnId](../../Dataset-Interfaces/IMTDatasetColumn/ColumnID.md) value is used as an ID.
