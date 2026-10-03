[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Totals](../Totals.md) / TableSummaryDelete

[Previous](TableSummaryAdd.md) | [Next](TableSummaryNext.md)

# IMTReportAPI::TableSummaryDelete

Delete a cell in a table totals row by its index.
    
    
    MTAPIRES  IMTReportAPI::TableSummaryDelete(
       const UINT  pos      // Cell position
       )

### Parameters

**pos**  
[in] Totals cell position beginning from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
