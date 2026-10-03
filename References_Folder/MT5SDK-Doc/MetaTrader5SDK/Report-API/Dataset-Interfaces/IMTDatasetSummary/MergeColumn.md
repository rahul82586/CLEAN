[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / MergeColumn

[Previous](Line.md) | [Next](Color.md)

# IMTDatasetSummary::MergeColumn

Get the ID of the column, to which the joining of summary cells is performed.
    
    
    UINT  IMTDatasetSummary::MergeColumn()  const

### Return Value

The ID of the column, to which the joining of summary cells is performed.

### Note

A summary cell is a result of the joining of cells from the current [IMTDatasetSummary::ColumnID](ColumnID.md) column up to the MergeColumn column.

# IMTDatasetSummary::MergeColumn

Set the ID of the column, to which the joining of summary cells must be performed.
    
    
    MTAPIRES  IMTDatasetSummary::MergeColumn(
       const UINT  column_id      // Column ID
       )

### Parameters

**column_id**  
[in] Column ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The [IMTDatasetColumn::ColumnId](../IMTDatasetColumn/ColumnID.md) value is used as the identifier.
