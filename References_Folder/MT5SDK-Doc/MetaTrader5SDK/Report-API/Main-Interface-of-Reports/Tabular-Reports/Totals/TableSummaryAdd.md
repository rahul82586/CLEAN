[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Totals](../Totals.md) / TableSummaryAdd

[Previous](TableSummaryClear.md) | [Next](TableSummaryDelete.md)

# IMTReportAPI::TableSummaryAdd

Add a totals row cell into a table.
    
    
    MTAPIRES  IMTReportAPI::TableSummaryAdd(
       const IMTDatasetSummary  *summary      // Totals cell object
       )

### Parameters

***summary**  
[in] An object of a totals row cell.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
