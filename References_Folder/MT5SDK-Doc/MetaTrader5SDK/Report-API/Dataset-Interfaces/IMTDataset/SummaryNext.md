[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / SummaryNext

[Previous](SummaryDelete.md) | [Next](SummaryTotal.md)

# IMTDataset::SummaryNext

Get the cells of a table totals row by its index.
    
    
    MTAPIRES  IMTDataset::SummaryNext(
       const UINT          pos,        // cell position
       IMTDatasetSummary*  summary     // totals cell object
       )

### Parameters

**pos**  
[in] Totals cell position beginning from 0.

**summary**  
[out]An object of a totals row cell. The object should first be created usingIMTDataset::SummaryCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
