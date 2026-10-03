[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTConParamArray::Next

Gets an object of a parameter at the specified position.

C++
    
    
    IMTDaily*  IMTConParamArray::Next(
       const UINT  index      // The position of a parameter
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTDaily  CIMTConParamArray.Next(
       uint        index      // The position of a parameter
       )

### Parameters

**index**  
[in] The position of a parameter in the array, starting with 0.

### Return Value

If successful, it returns a pointer to the object of a parameter at the specified position in the array. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
