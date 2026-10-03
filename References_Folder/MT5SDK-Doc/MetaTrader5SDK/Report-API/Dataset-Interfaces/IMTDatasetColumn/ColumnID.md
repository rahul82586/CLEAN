[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / ColumnID

[Previous](Name.md) | [Next](Type.md)

# IMTDatasetColumn::ColumnID

Get a column ID.
    
    
    UINT  IMTDatasetColumn::ColumnID()  const

### Return Value

Column ID.

### Note

ID is used in the following methods:

  * [IMTDatasetColumn::DigitsColumn](DigitsColumn.md)
  * [IMTDatasetSummary::MergeColumn](../IMTDatasetSummary/MergeColumn.md)
  * [IMTDatasetSummary::ColumnID](../IMTDatasetSummary/ColumnID.md)



# IMTDatasetColumn::ColumnID

Set a column ID.
    
    
    MTAPIRES  IMTDatasetColumn::ColumnID(
       const UINT  column_id      // Column ID
       )

### Parameters

**column_id**  
[in] Column ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

ID must be unique and must not be equal to 0. ID is used in the following methods:

  * [IMTDatasetColumn::DigitsColumn](DigitsColumn.md)
  * [IMTDatasetSummary::MergeColumn](../IMTDatasetSummary/MergeColumn.md)
  * [IMTDatasetSummary::ColumnID](../IMTDatasetSummary/ColumnID.md)


