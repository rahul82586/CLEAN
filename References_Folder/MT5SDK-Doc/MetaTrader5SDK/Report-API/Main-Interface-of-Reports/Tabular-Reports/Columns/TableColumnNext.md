[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Columns](../Columns.md) / TableColumnNext

[Previous](TableColumnSize.md) | [Next](../Rows.md)

# IMTReportAPI::TableColumnNext

Get a column description by index.
    
    
    MTAPIRES  IMTReportAPI::TableColumnNext(
       const UINT         pos,        // Column position
       IMTDatasetColumn  *column      // Column object
       )

### Parameters

**pos**  
[in] Column position beginning from 0.

***column**  
[out] An object of a table column description. The object must first be created using theIMTReportAPI::TableColumnCreateobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
