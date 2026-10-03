[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTCommentArray::Delete

Delete a comment object by its position.

C++
    
    
    MTAPIRES  IMTCommentArray::Delete(
       const UINT  pos      // Comment position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.Delete(
       uint        pos      // Comment position
       )

### Parameters

**pos**  
[in] Comment position in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by calling the [IMTComment::Release](../IMTComment/Release.md) method.
