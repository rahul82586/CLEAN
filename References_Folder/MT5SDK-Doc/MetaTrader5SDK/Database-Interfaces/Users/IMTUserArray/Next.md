[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTUserArray::Next

Get a client record object by its position.

C++
    
    
    IMTUser*  IMTUserArray::Next(
       const UINT  pos      // The position of a client record
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTUser  CIMTUserArray.Next(
       uint        pos      // The position of a client record
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the client position object at the appropriate array position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
