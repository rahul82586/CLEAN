[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Flags

[Previous](DigitsColumn.md) | [Next](Offset.md)

# IMTDatasetColumn::Flags

Get column flags.
    
    
    UINT64  IMTDatasetColumn::Flags()  const

### Return Value

A value of the [IMTDatasetColumn::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTDatasetColumn::Flags

Set column flags.
    
    
    MTAPIRES  IMTDatasetColumn::Flags(
       const UINT64  flags      // Column flags
       )

### Parameters

**flags**  
[in] Column flags. To pass the options, theIMTDatasetColumn::EnFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
