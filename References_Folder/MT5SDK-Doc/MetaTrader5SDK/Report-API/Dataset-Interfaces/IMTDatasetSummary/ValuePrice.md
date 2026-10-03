[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValuePrice

[Previous](ValueDateTime.md) | [Next](ValuePricesBid.md)

# IMTDatasetSummary::ValuePrice

Get a previously specified summary cell price value.
    
    
    double  IMTDatasetSummary::ValuePrice()  const

### Return Value

Previously specified summary cell price value.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_PRICE (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValuePrice

Set a summary cell price value.
    
    
    MTAPIRES  IMTDatasetSummary::ValuePrice(
       const double  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_PRICE (#entype)](Enumerations.md#entype).
