[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldCreate

[Previous](Clear.md) | [Next](FieldCreateReference.md)

# IMTDatasetRequest::FieldCreate

Create a field object.
    
    
    IMTDatasetField*  IMTDatasetRequest::FieldCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTDatasetField](../IMTDatasetField.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDatasetField::Release](../IMTDatasetField/Release.md) method of this object.
