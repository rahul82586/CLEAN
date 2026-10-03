[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldClear

[Previous](FieldDelete.md) | [Next](FieldShift.md)

# IMTDatasetRequest::FieldClear

Clear the request description.
    
    
    MTAPIRES  IMTDatasetRequest::FieldClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A database query is performed as a collection of fields and selection conditions. Use this method to delete all fields and conditions from the request.
