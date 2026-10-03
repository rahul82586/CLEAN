[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Type

[Previous](ColumnID.md) | [Next](Width.md)

# IMTDatasetColumn::Type

Get a column type.
    
    
    UINT  IMTDatasetColumn::Type()  const

### Return Value

A value of the [IMTDatasetColumn::EnType (#entype)](Enumerations.md#entype) enumeration.

### Note

The type specifies the size and the format of displaying an appropriate field in an entry's structure.

# IMTDatasetColumn::Type

Set a column type.
    
    
    MTAPIRES  IMTDatasetColumn::Type(
       const UINT  type      // Type of a column
       )

### Parameters

**type**  
[in] Type of a column. To pass the options, theIMTDatasetColumn::EnTypeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The type specifies the size and the format of displaying an appropriate field in an entry's structure.
