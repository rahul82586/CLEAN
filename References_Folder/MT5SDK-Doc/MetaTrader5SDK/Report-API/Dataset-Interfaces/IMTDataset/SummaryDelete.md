[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / SummaryDelete

[Previous](SummaryAdd.md) | [Next](SummaryNext.md)

# IMTDataset::SummaryDelete

Delete a cell in a table totals row by its index.
    
    
    MTAPIRES  IMTDataset::SummaryDelete(
       const UINT  pos      // cell position
       )

### Parameters

**pos**  
[in] Totals cell position beginning from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
