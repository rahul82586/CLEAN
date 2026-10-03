[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldShift

[Previous](FieldClear.md) | [Next](FieldTotal.md)

# IMTDatasetRequest::FieldShift

Change the position of the [field description](../IMTDatasetField.md) in the request.
    
    
    MTAPIRES  IMTDatasetRequest::FieldShift(
       const UINT  pos,       
       const int   shift      
       )

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The order of fields in a request determines the order of filtering by these fields when performing a database query.
