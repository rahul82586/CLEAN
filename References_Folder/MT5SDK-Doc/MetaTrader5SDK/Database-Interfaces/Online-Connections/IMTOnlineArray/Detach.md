[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTOnlineArray::Detach

Detach connection record object from an array.

C++
    
    
    IMTOnline*  IMTOnlineArray::Detach(
       const UINT  pos      // Connection record position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTOnline  CIMTOnlineArray.Detach(
       uint        pos      // Connection record position
       )

### Parameters

**pos**  
[in] Position of a connection record in an array, starting with 0.

### Return Value

Returns a pointer to the detached connection record object.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
