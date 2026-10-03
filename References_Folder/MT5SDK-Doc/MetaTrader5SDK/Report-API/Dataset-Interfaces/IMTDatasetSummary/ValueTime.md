[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueTime

[Previous](ValueDate.md) | [Next](ValueDateTime.md)

# IMTDatasetSummary::ValueTime

Get a previously specified summary cell value of the time type.
    
    
    INT64  IMTDatasetSummary::ValueTime()  const

### Return Value

Previously specified summary cell value of the time type.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_TIME (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueTime

Set a summary cell value of the time type.
    
    
    MTAPIRES  IMTDatasetSummary::ValueTime(
       const INT64  value      // Value
       )

### Parameters

**value**  
[in] Summary cell value in the HH:MM:SS format.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_TIME (#entype)](Enumerations.md#entype).
