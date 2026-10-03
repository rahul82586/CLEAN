[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTConParamArray::Detach

Detaches an object of a parameter from an array.

C++
    
    
    IMTConParam*  IMTConParamArray::Detach(
       const UINT  pos      // Position of the parameter
       )

.NET (Gateway/Manager API)
    
    
    CIMTConParam  CIMTConParamArray.Detach(
       uint        pos      // Position of the parameter
       )

### Parameters

**pos**  
[in] The position of a parameter in the array, starting with 0.

### Return Value

Returns a pointer to the detached object of a parameter.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
