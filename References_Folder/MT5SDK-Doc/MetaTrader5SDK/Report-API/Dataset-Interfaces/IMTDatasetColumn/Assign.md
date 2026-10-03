[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDatasetColumn::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTDatasetColumn::Assign(
       const IMTDatasetColumn*  column      // Source object
       )

### Parameters

**column**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
