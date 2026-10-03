[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTClientArray::Next

Get a client object by its position.

C++
    
    
    IMTClient*  IMTClientArray::Next(
       const UINT  pos      // Client position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTClient  CIMTClientArray.Next(
       uint        pos      // Client position
       )

### Parameters

**pos**  
[in] Position of a client in the array, starting with 0.

### Return Value

If successful, it returns a pointer to the client object at the specified position. Otherwise, NULL is returned.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
