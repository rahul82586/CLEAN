[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / Color

[Previous](MergeColumn.md) | [Next](Flags.md)

# IMTDatasetSummary::Color

Get a text color in the totals cell.
    
    
    UINT  IMTDatasetSummary::Color()  const

### Return Value

Text color in the totals cell.

# IMTDatasetSummary::Color

Set a text color in the totals cell.
    
    
    MTAPIRES  IMTDatasetSummary::Color(
       const UINT  color      // Text color
       )

### Parameters

**color**  
[in] Text color in the totals cell.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
