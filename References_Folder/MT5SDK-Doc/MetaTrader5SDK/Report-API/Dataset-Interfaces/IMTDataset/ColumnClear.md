[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / ColumnClear

[Previous](ColumnCreate.md) | [Next](ColumnAdd.md)

# IMTDataset::ColumnClear

Clear table columns description.
    
    
    MTAPIRES  IMTDataset::ColumnClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After this method is called, all table contents including all totals rows is deleted.
