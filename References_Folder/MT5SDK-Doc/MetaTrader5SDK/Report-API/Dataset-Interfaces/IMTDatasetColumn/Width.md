[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Width

[Previous](Type.md) | [Next](WidthMax.md)

# IMTDatasetColumn::Width

Get the column relative width, while displaying in the manager terminal.
    
    
    UINT  IMTDatasetColumn::Width()  const

### Return Value

The column relative width, while displaying in the manager terminal.

### Note

The columns width is specified relative to each other. E.g., if the column 1 width is equal to 40 standard units and the column 2 width is 2 - 10 standard units, the column 1 will occupy 3/4 of the available space and the column 2 - 1/4 of the available space.

# IMTDatasetColumn::Width

Set the column relative width, while displaying in the manager terminal.
    
    
    MTAPIRES  IMTDatasetColumn::Width(
       const UINT  width      // Column width
       )

### Parameters

**width**  
[in] Column relative width.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The columns width is specified relative to each other. E.g., if the column 1 width is equal to 40 standard units and the column 2 width is 2 - 10 standard units, the column 1 will occupy 3/4 of the available space and the column 2 - 1/4 of the available space.
