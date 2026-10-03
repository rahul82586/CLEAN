[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTUserArray::Detach

Detach a client record object from an array.

C++
    
    
    IMTUser*  IMTUserArray::Detach(
       const UINT  pos      // The position of a client record
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTUser  CIMTUserArray.Detach(
       uint        pos      // The position of a client record
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of the client record.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
