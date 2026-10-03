[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Flags

[Previous](Size.md) | [Next](WhereAddInt.md)

# IMTDatasetField::Flags

Get the field flags.
    
    
    UINT64  IMTDatasetColumn::Flags()  const

### Return Value

A value of the [IMTDataseField::EnFieldFlags (#enfieldflags)](Enumerations.md#enfieldflags) enumeration.

# IMTDatasetField::Flags

Set the field flags.
    
    
    MTAPIRES  IMTDatasetColumn::Flags(
       const UINT64  flags      // Field flags
       )

### Parameters

**flags**  
[in] Field flags. TheIMTDatasetField::EnFieldFlagsenumeration is used to pass flags.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
