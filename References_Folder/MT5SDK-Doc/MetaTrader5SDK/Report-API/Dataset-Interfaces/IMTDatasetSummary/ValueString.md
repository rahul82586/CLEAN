[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueString

[Previous](ValueMoney.md) | [Next](ValueDate.md)

# IMTDatasetSummary::ValueString

Get a previously specified summary cell string value.
    
    
    LPCWSTR  IMTDatasetSummary::ValueString()  const

### Return Value

Previously specified summary cell string value.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_STRING (#entype)](Enumerations.md#entype) type. Otherwise, the method returns an empty string.

# IMTDatasetSummary::ValueString

Set a summary cell string value.
    
    
    MTAPIRES  IMTDatasetSummary::ValueString(
       LPCWSTR  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_STRING (#entype)](Enumerations.md#entype).
