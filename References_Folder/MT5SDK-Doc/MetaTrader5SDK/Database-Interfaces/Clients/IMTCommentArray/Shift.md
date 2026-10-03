[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTCommentArray::Shift

Change the position of a comment in an array.

C++
    
    
    MTAPIRES  IMTCommentArray::Shift(
       const UINT  pos,       // Comment position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.Shift(
       uint        pos,       // Comment position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Comment position in an array, starting with 0.

**shift**  
[in] Shift of the comment relative to the current position. A negative value means shift towards the array beginning, a positive value means shift towards its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
