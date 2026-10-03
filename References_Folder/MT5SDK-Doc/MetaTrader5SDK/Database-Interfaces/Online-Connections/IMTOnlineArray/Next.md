[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTOnlineArray::Next

Get connection record object by its position.

C++
    
    
    IMTOnline*  IMTOnlineArray::Next(
       const UINT  pos      // Connection record position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTOnline  CIMTOnlineArray.Next(
       uint        pos      // Connection record position
       )

### Parameters

**pos**  
[in] Position of a connection record in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the connection record object at the appropriate array position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
