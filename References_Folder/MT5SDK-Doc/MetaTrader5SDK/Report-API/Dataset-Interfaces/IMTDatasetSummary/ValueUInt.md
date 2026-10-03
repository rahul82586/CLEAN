[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueUInt

[Previous](ValueInt.md) | [Next](ValueDouble.md)

# IMTDatasetSummary::ValueUInt

Get a previously specified cell unsigned integer value.
    
    
    UINT64  IMTDatasetSummary::ValueUInt()  const

### Return Value

A previously specified cell unsigned integer value.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_UINT64 (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueUInt

Set a summary cell unsigned integer value.
    
    
    MTAPIRES  IMTDatasetSummary::ValueUInt(
       const UINT64  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_UINT64 (#entype)](Enumerations.md#entype).
