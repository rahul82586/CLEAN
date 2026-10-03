[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueInt

[Previous](Digits.md) | [Next](ValueUInt.md)

# IMTDatasetSummary::ValueInt

Get a previously specified cell integer value.
    
    
    INT64  IMTDatasetSummary::ValueInt()  const

### Return Value

Previously specified cell integer value.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_INT64 (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueInt

Set a summary cell integer value.
    
    
    MTAPIRES  IMTDatasetSummary::ValueInt(
       const INT64  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_INT64 (#entype)](Enumerations.md#entype).
