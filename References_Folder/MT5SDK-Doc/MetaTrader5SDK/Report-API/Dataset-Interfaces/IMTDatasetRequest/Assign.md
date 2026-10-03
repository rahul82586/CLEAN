[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDatasetRequest::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTDatasetRequest::Assign(
       const IMTDatasetRequest*  request      // Source object
       )

### Parameters

**request**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
