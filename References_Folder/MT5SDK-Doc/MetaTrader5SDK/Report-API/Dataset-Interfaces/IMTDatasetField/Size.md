[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Size

[Previous](Offset.md) | [Next](Flags.md)

# IMTDatasetField::Size

Get the size of the field data in bytes.
    
    
    UINT  IMTDatasetField::Size()  const

### Return Value

The size of the field data in bytes.

### Note

In all cases except strings data size is specified by its type ([IMTDatasetField::EnFieldType (#enfieldtype)](Enumerations.md#enfieldtype)).

# IMTDatasetField::Size

Set the size of the field data in bytes.
    
    
    MTAPIRES  IMTDatasetField::Size(
       const UINT  size      // Size
       )

### Parameters

**size**  
[in] Size in bytes.

### Note

This method can be used only for strings. In all other cases the size is specified by data type ([IMTDatasetField::EnFieldType (#enfieldtype)](Enumerations.md#enfieldtype)).
