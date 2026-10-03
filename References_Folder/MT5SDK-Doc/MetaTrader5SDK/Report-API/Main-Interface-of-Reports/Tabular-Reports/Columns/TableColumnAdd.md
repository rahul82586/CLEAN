[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Columns](../Columns.md) / TableColumnAdd

[Previous](TableColumnClear.md) | [Next](TableColumnDelete.md)

# IMTReportAPI::TableColumnAdd

Add a column description to a table end.
    
    
    MTAPIRES  IMTReportAPI::TableColumnAdd(
       const IMTDatasetColumn  *column      // Column object
       )

### Parameters

***column**  
[in] An object of a table column description.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
