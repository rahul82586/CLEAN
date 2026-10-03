[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldAdd

[Previous](FieldCreateReference.md) | [Next](FieldUpdate.md)

# IMTDatasetRequest::FieldAdd

Add a field object to the request.
    
    
    MTAPIRES  IMTDatasetRequest::FieldAdd(
       const IMTDatasetField*  field      // Field object
       )

### Parameters

**field**  
[in]Fields description object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A database query is performed as a collection of fields and selection conditions. Use this method to add a field (optionally with conditions) to the request.
