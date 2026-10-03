[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDatasetField::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTDatasetField::Assign(
       const IMTDatasetField*  field    // Source object
       )

### Parameters

**field**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
