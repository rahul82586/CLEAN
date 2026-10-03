[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldUpdate

[Previous](FieldAdd.md) | [Next](FieldDelete.md)

# IMTDatasetRequest::FieldUpdate

Change a field object in the request.
    
    
    MTAPIRES  IMTDatasetRequest::FieldUpdate(
       const UINT              pos,       // Field position
       const IMTDatasetField*  field      // Field object
       )

### Parameters

**pos**  
[in] Field position starting from 0.

**field**  
[in]Fields description object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A database query is performed as a collection of fields and selection conditions. Use this method to change a field (optionally with conditions) in a request.
