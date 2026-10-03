[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldNext

[Previous](FieldTotal.md) | [Next](../IMTDatasetColumn.md)

# IMTDatasetRequest::FieldNext

Get a field description in a request based on its index.
    
    
    MTAPIRES  IMTDatasetRequest::FieldNext(
       const UINT       pos,        
       IMTDatasetField  *field      
       )

### Parameters

**pos**  
[in] Field position starting from 0.

**field**  
[in]Field description object. The object must be previously created using theIMTDatasetRequest::FieldCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A database query is performed as a collection of fields and selection conditions. Use this method to receive request field description (optionally with conditions).
