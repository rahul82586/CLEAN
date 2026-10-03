[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDataset::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTDataset::Assign(
       const IMTDataset*  data  // source object
       )

### Parameters

**data**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
