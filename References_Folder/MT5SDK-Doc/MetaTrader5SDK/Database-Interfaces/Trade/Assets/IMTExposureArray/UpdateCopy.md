[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTExposureArray::UpdateCopy

Changes the asset record at the specified position of an array by copying the parameters of the passed asset object.

C++
    
    
    MTAPIRES  IMTExposureArray::UpdateCopy(
       const UINT           pos,         // Position
       const IMTExposure*   exposure     // The asset object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.UpdateCopy(
       uint                 pos,         // Position
       CIMTExposure         exposure     // The asset object
       )

### Parameters

**pos**  
[in] The position of an asset record in an array, starting with 0.

**order**  
[in] The object of the asset record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the 'exposure' object into an asset record object at the specified position of an array.
