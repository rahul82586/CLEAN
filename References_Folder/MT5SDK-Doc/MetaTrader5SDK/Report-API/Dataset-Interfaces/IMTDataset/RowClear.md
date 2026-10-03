[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / RowClear

[Previous](ColumnNext.md) | [Next](RowWrite.md)

# IMTDataset::RowClear

Delete the contents of a whole table.
    
    
    MTAPIRES  IMTDataset::RowClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

When this method is called, columns descriptions are not deleted.
