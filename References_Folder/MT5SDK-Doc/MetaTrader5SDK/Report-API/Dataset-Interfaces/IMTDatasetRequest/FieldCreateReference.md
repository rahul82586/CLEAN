[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldCreateReference

[Previous](FieldCreate.md) | [Next](FieldAdd.md)

# IMTDatasetRequest::FieldCreateReference

Create a reference to the object of the field at the specified position.
    
    
    IMTDatasetField*  IMTDatasetRequest::FieldCreateReference(
       const UINT  pos      // Field position
       )

### Parameters

**pos**  
[in] Field position starting from 0.

### Return Value

Returns a pointer to the object which implements the [IMTDatasetField](../IMTDatasetField.md) interface.

### Note

The [IMTDatasetRequest](../IMTDatasetRequest.md) request contains an array of [IMTDatasetField](../IMTDatasetField.md) fields. These fields can be quite large as they can contain arrays of parameters ([IMTDatasetField::WhereAdd*Array](../IMTDatasetField/WhereAddIntArray.md)). When the fields are updated via the [IMTDatasetRequest::FieldUpdate](FieldUpdate.md) method, the relevant data is copied. Therefore, frequent updating of large fields requires a lot of resources. By using the new method, you can update large query fields by reference without unnecessary copying.
