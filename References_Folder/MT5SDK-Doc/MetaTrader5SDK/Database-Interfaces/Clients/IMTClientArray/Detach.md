[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTClientArray::Detach

Detach a client object from an array.

C++
    
    
    IMTClient*  IMTClientArray::Detach(
       const UINT  pos      // Client position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTClient  CIMTClientArray.Detach(
       uint        pos      // Client position
       )

### Parameters

**pos**  
[in] Position of a client in the array, starting with 0.

### Return Value

Returns a pointer to the detached client object.

### Note

This method removes a pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
