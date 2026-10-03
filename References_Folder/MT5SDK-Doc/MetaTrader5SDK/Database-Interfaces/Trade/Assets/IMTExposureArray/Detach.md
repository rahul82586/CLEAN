[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTExposureArray::Detach

Detaches the asset record object from an array.

C++
    
    
    IMTExposure*  IMTExposureArray::Detach(
       const UINT  pos      // The position of an asset
       )

.NET (Gateway/Manager API)
    
    
    CIMTExposure  CIMTExposureArray.Detach(
       uint        pos      // The position of an asset
       )

### Parameters

**pos**  
[in] The position of an asset record in an array, starting with 0.

### Return Value

Returns a pointer to the detached [asset record object](../IMTExposure.md).

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
