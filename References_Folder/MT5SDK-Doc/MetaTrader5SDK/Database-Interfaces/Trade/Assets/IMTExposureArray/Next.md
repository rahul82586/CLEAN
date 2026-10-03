[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTExposureArray::Next

Gets an asset record object by its index.

C++
    
    
    IMTExposure*  IMTExposureArray::Next(
       const UINT  index      // Position of the record
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTExposure  CIMTExposureArray.Next(
       uint        index      // Position of the record
       )

### Parameters

**index**  
[in] The position of an asset record in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the asset record object at the specified position in the array. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
