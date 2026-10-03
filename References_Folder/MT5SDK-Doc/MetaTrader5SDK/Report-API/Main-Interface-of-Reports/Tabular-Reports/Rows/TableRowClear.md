[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Rows](../Rows.md) / TableRowClear

[Previous](../Rows.md) | [Next](TableRowWrite.md)

# IMTReportAPI::TableRowClear

Delete the contents of a whole table.
    
    
    MTAPIRES  IMTReportAPI::TableRowClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When this method is called, columns descriptions are not deleted.
