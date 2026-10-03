[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Totals](../Totals.md) / TableSummaryNext

[Previous](TableSummaryDelete.md) | [Next](TableSummaryTotal.md)

# IMTReportAPI::TableSummaryNext

Get the cells of a table totals row by its index.
    
    
    MTAPIRES  IMTReportAPI::TableSummaryNext(
       const UINT          pos,        // Cell position
       IMTDatasetSummary*  summary     // Totals cell object
       )

### Parameters

**pos**  
[in] Totals cell position beginning from 0.

***summary**  
[out] An object of a totals row cell. The object must first be created using theIMTReportAPI::TableSummaryCreateobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
