[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTExposureArray::Delete

Deletes the asset record object from the array by its index.

C++
    
    
    MTAPIRES  IMTExposureArray::Delete(
       const UINT  pos      // Position of the record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.Delete(
       uint        pos      // Position of the record
       )

### Parameters

**pos**  
[in] The position of an asset starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTExposure::Release](../IMTExposure/Release.md) method.
