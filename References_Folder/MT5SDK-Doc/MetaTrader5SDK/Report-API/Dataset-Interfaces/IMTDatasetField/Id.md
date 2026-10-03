[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Id

[Previous](Clear.md) | [Next](Type.md)

# IMTDatasetField::Id

Get the field ID.
    
    
    UINT  IMTDatasetField::Id()  const

### Return Value

A value from [IMTDatasetField::EnFieldId (#enfieldid)](Enumerations.md#enfieldid).

### Note

The identifier determines the type of information stored in the field: a certain property of a trading account, client or deal.

# IMTDatasetField::Id

Set the field ID.
    
    
    MTAPIRES  IMTDatasetField::Id(
       const UINT  id      // Field ID
       )

### Parameters

**id**  
[in] Field identifier. The ID value is passed using theIMTDatasetField::EnFieldIdenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The identifier determines the type of information stored in the field: a certain property of a trading account, client or deal.
