[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueDouble

[Previous](ValueUInt.md) | [Next](ValueMoney.md)

# IMTDatasetSummary::ValueDouble

Get a previously specified cell value of the double type.
    
    
    double  IMTDatasetSummary::ValueDouble()  const

### Return Value

Previously specified cell value of the double type.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_DOUBLE (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueDouble

Set a summary cell value of the double type.
    
    
    MTAPIRES  IMTDatasetSummary::ValueDouble(
       const double  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_DOUBLE (#entype)](Enumerations.md#entype).
