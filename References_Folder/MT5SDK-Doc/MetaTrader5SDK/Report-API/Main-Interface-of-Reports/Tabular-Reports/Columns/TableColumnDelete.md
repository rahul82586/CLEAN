[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Columns](../Columns.md) / TableColumnDelete

[Previous](TableColumnAdd.md) | [Next](TableColumnTotal.md)

# IMTReportAPI::TableColumnDelete

Delete a column description from a table by index.
    
    
    MTAPIRES  IMTReportAPI::TableColumnDelete(
       const UINT  pos      // Column position
       )

### Parameters

**pos**  
[in] Position of the column that must be deleted beginning from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
