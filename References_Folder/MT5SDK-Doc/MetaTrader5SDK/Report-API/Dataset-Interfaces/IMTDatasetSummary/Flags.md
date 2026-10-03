[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / Flags

[Previous](Color.md) | [Next](Type.md)

# IMTDatasetSummary::Flags

Get summary cell flags.
    
    
    UINT64  IMTDatasetSummary::Flags()  const

### Return Value

A value of the [IMTDatasetSummary::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

### Note

This method is reserved for future use.

# IMTDatasetSummary::Flags

Set summary cell flags.
    
    
    MTAPIRES  IMTDatasetSummary::Flags(
       const UINT64  flags      // flags
       )

### Parameters

**flags**  
[in] Summary cell flags. To pass the options, theIMTDatasetSummary::EnFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method is reserved for future use.
