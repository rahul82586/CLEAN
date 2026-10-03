[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / SummaryAdd

[Previous](SummaryClear.md) | [Next](SummaryDelete.md)

# IMTDataset::SummaryAdd

Add a totals row cell into a table.
    
    
    MTAPIRES  IMTDataset::SummaryAdd(
       const IMTDatasetSummary  *summary      // Totals cell object
       )

### Parameters

**summary**  
[in]An object of a totals row cell.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
