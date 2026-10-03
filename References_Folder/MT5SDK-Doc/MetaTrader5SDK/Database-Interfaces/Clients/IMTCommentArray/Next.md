[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTCommentArray::Next

Get a comment object by its position.

C++
    
    
    IMTComment*  IMTCommentArray::Next(
       const UINT  pos      // Comment position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTComment  CIMTCommentArray.Next(
       uint        pos      // Comment position
       )

### Parameters

**pos**  
[in] Comment position in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the comment object at the specified position. Otherwise, NULL is returned.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
