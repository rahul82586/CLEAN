[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ColumnID

[Previous](Clear.md) | [Next](Line.md)

# IMTDatasetSummary::ColumnID

Get the ID of the column, under which a summary is specified.
    
    
    UINT  IMTDatasetSummary::ColumnID()  const

### Return Value

The ID of the column, under which a summary is specified.

### Note

Column ID is specified by the [IMTDatasetColumn::ColumnID](../IMTDatasetColumn/ColumnID.md) method.

# IMTDatasetSummary::ColumnID

Set the ID of the column, under which a summary is specified.
    
    
    MTAPIRES  IMTDatasetSummary::ColumnID(
       const UINT  column_id      // Column ID
       )

### Parameters

**column_id**  
[in] Column ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Column ID is specified by the [IMTDatasetColumn::ColumnID](../IMTDatasetColumn/ColumnID.md) method.
