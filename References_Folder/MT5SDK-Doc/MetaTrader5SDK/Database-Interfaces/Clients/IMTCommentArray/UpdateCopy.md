[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTCommentArray::UpdateCopy

Change a comment at the specified position of an array by copying the parameters of a passed comment object.

C++
    
    
    MTAPIRES  IMTCommentArray::UpdateCopy(
       const UINT         pos,      // Position
       const IMTComment*  comment   // Comment object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.UpdateCopy(
       uint               pos,     // Position
       CIMTComment        comment  // Comment object
       )

### Parameters

**pos**  
[in] Comment position in an array, starting with 0.

**comment**  
[in]Comment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method copies the 'comment' object parameters to the comment object at the specified position in the array.
