[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueMoney

[Previous](ValueDouble.md) | [Next](ValueString.md)

# IMTDatasetSummary::ValueMoney

Get a previously specified summary cell monetary value.
    
    
    double  IMTDatasetSummary::ValueMoney()  const

### Return Value

Previously specified summary cell monetary value.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_MONEY (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueMoney

Set a summary cell monetary value.
    
    
    MTAPIRES  IMTDatasetSummary::ValueMoney(
       const double  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_MONEY (#entype)](Enumerations.md#entype).
