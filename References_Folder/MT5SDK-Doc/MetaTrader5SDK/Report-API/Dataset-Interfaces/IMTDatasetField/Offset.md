[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Offset

[Previous](Type.md) | [Next](Size.md)

# IMTDatasetField::Offset

Get the offset within one entry defining the data beginning.
    
    
    UINT  IMTDatasetField::Offset()  const

### Return Value

The offset within one entry defining the data beginning.

# IMTDatasetField::Offset

Set the offset within one entry defining the data beginning.
    
    
    MTAPIRES  IMTDatasetField::Offset(
       const UINT  offset      // Offset
       )

### Parameters

**offset**  
[in] Offset within one entry defining the data beginning.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is used for all field types. The offset must be set for fields with [IMTDatasetField::FLAG_SELECT (#enfieldflags)](Enumerations.md#enfieldflags).
