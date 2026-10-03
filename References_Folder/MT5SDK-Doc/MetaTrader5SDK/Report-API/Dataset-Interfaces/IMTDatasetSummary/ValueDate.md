[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueDate

[Previous](ValueString.md) | [Next](ValueTime.md)

# IMTDatasetSummary::ValueDate

Get a previously specified summary cell value of the date type.
    
    
    INT64  IMTDatasetSummary::ValueDate()  const

### Return Value

Previously specified summary cell value of the date type.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_DATE (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueDate

Set a summary cell value of the date type.
    
    
    MTAPIRES  IMTDatasetSummary::ValueDate(
       const INT64  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value in the YYYY.MM.DD format

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_DATE (#entype)](Enumerations.md#entype).
