[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Columns](../Columns.md) / TableColumnClear

[Previous](TableColumnCreate.md) | [Next](TableColumnAdd.md)

# IMTReportAPI::TableColumnClear

Clear table columns description.
    
    
    MTAPIRES  IMTReportAPI::TableColumnClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After this method is called, all table contents including all totals rows is deleted.
