[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / CommentResult

[Previous](CommentType.md) | [Next](AttachmentsAdd.md)

# CommentResult

Get a call result from a comment.

C++
    
    
    UINT  IMTComment::CommentType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTComment.CommentType()

### Return Value

A value of the [IMTComment::EnCommentResult (#encommentresult)](Enumerations.md#encommentresult) enumeration.

# IMTComment::CommentType

Set a call result for a comment.

C++
    
    
    MTAPIRES  IMTComment::CommentType(
       const UINT  result    // Result
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.CommentType(
       uint        result    // Result
       )

### Parameters

**result**  
[in] Call result. The value is passed using theIMTComment::EnCommentResultenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This field is used to indicate additional information when adding a comment to a clients history after making a call.
