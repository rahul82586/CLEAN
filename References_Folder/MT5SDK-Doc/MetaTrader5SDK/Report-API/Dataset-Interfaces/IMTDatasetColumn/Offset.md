[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Offset

[Previous](Flags.md) | [Next](Size.md)

# IMTDatasetColumn::Offset

Get the shift inside the one entry specifying the beginning of a column data.
    
    
    UINT  IMTDatasetColumn::Offset()  const

### Return Value

Shift inside the one entry specifying the beginning of a column data.

# IMTDatasetColumn::Offset

Set the shift inside the one entry specifying the beginning of a column data.
    
    
    MTAPIRES  IMTDatasetColumn::Offset(
       const UINT  offset      // Shift
       )

### Parameters

**offset**  
[in] Shift inside the one entry specifying the beginning of a column data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
