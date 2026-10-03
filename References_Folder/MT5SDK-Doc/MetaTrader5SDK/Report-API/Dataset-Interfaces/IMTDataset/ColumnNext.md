[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / ColumnNext

[Previous](ColumnSize.md) | [Next](RowClear.md)

# IMTDataset::ColumnNext

Get a column description by index.
    
    
    MTAPIRES  IMTDataset::ColumnNext(
       const UINT         pos,       // column position
       IMTDatasetColumn*  column     // column object
       )

### Parameters

**pos**  
[in] Column position beginning from 0.

**column**  
[out]An object of a table column description. The object should first be created using theIMTDataset:ColumnCreateobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
