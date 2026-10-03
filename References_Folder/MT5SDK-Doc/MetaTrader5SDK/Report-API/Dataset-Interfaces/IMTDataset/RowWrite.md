[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / RowWrite

[Previous](RowClear.md) | [Next](RowTotal.md)

# IMTDataset::RowWrite

Add (output) one record to a table.
    
    
    MTAPIRES  IMTDataset::RowWrite(
       const void*  data,     // data pointer
       const UINT   size      // data size
       )

### Parameters

**data**  
[in] Pointer to added entry data.

**size**  
[in] Data size. Size of the passed data is checked for compliance with theIMTDataset::ColumnSizevalue.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Maximum data size is 4 GB. When reaching the maximum size, the IMTReportAPI::TableRowWrite method returns the [MT_RET_REPORT_LIMIT_REPORT](../../../Return-Codes/Report-Generation.md) error.
