[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / ColumnAdd

[Previous](ColumnClear.md) | [Next](ColumnDelete.md)

# IMTDataset::ColumnAdd

Add a column description to a table end.
    
    
    MTAPIRES  IMTDataset::ColumnAdd(
       const IMTDatasetColumn  *column      // column object
       )

### Parameters

**column**  
[in]Table column description object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

By default, the values from the first column are used as headers for all other columns.
