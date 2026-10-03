[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / CommentType

[Previous](Text.md) | [Next](CommentResult.md)

# IMTComment::CommentType

Get the comment type.

C++
    
    
    UINT  IMTComment::CommentType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTComment.CommentType()

### Return Value

A value of the [IMTComment::EnCommentType (#encommenttype)](Enumerations.md#encommenttype) enumeration.

# IMTComment::CommentType

Set the comment type.

C++
    
    
    MTAPIRES  IMTComment::CommentType(
       const UINT  type       // Comment type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.CommentType(
       uint        type      // Comment type
       )

### Parameters

**type**  
[in] Comment type. The comment type is passed using theIMTComment::EnCommentTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
