[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTConGroupArray::Detach

Detach a group object from an array.

C++
    
    
    IMTConGroup*  IMTConGroupArray::Detach(
       const UINT  pos      // Group position
       )

.NET (Gateway/Manager API)
    
    
    CIMTConGroup  CIMTConGroupArray.Detach(
       uint        pos      // Group position
       )

### Parameters

**pos**  
[in] Group position in the array, starting with 0.

### Return Value

Returns a pointer to the detached [IMTConGroup](../IMTConGroup.md) group object.

### Note

This method removes the object pointer at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
