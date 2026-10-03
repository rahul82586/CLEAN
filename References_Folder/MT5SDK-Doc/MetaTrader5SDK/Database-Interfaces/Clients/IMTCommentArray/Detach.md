[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTCommentArray::Detach

Detach a comment object from an array.

C++
    
    
    IMTComment*  IMTCommentArray::Detach(
       const UINT  pos      // Comment position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTComment  CIMTCommentArray.Detach(
       uint        pos      // Comment position
       )

### Parameters

**pos**  
[in] Comment position in an array, starting with 0.

### Return Value

Returns a pointer to the detached comment object.

### Note

This method removes a pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
