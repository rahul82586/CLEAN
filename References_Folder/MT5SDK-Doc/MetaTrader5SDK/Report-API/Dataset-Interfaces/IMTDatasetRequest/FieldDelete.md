[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldDelete

[Previous](FieldUpdate.md) | [Next](FieldClear.md)

# IMTDatasetRequest::FieldDelete

Delete a field object from the request.
    
    
    MTAPIRES  IMTDatasetRequest::FieldDelete(
       const UINT  pos      // Field position
       )

### Parameters

**pos**  
[in] Field position starting from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A database query is performed as a collection of fields and selection conditions. Use this method to delete a field (optionally with conditions) from the request.
