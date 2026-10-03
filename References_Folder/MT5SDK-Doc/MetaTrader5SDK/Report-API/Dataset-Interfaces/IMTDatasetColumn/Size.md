[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Size

[Previous](Offset.md) | [Next](../IMTDatasetSummary.md)

# IMTDatasetColumn::Size

Get the size of the column data in bytes.
    
    
    UINT  IMTDatasetColumn::Size()  const

### Return Value

Size of the column data in bytes.

### Note

In all cases except strings data size is specified by its type ([IMTDatasetColumn::EnType (#entype)](Enumerations.md#entype)).

# IMTDatasetColumn::Size

Set the size of the column data in bytes.
    
    
    MTAPIRES  IMTDatasetColumn::Size(
       const UINT  size      // Size
       )

### Parameters

**size**  
[in] Size in bytes.

### Note

This method can be used only for strings. In all other cases the size is specified by data type ([IMTDatasetColumn::EnType (#entype)](Enumerations.md#entype)).
