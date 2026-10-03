[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / ColumnDelete

[Previous](ColumnAdd.md) | [Next](ColumnTotal.md)

# IMTDataset::ColumnDelete

Delete a column description from a table by index.
    
    
    MTAPIRES  IMTDataset::ColumnDelete(
       const UINT  pos      // column position
       )

### Parameters

**pos**  
[in] Position of the column that should be deleted beginning from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### 
