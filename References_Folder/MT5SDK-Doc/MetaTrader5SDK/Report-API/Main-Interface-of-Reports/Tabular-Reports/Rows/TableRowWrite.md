[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Rows](../Rows.md) / TableRowWrite

[Previous](TableRowClear.md) | [Next](TableRowTotal.md)

# IMTReportAPI::TableRowWrite

Add (output) one record to a table.
    
    
    MTAPIRES  IMTReportAPI::TableRowWrite(
       const void  *data,     // a pointer to the data
       const UINT  size       // Data size
       )

### Parameters

***data**  
[in] A pointer to the data of a record to add.

**size**  
[in] Data size. The size of the submitted data is checked for its compliance with theIMTReportAPI::TableColumnSizevalue.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Maximum allowed size of a tabular report is 4GB. If this limit is reached, IMTReportAPI::TableRowWrite will return error [MT_RET_REPORT_LIMIT_REPORT](../../../../Return-Codes/Report-Generation.md).
