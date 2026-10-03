[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTConGroupArray::Next

Get a group object by position.

C++
    
    
    IMTConGroup*  IMTConGroupArray::Next(
       const UINT  index      // Group position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTConGroup  CIMTConGroupArray.Next(
       uint        index      // Group position
       )

### Parameters

**index**  
[in] Group position in the array, starting with 0.

### Return Value

If successful, the method returns a pointer to the [IMTConGroup](../IMTConGroup.md) group object at the corresponding array position. Otherwise, NULL is returned.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when an array object is deleted, the returned pointer becomes invalid.
