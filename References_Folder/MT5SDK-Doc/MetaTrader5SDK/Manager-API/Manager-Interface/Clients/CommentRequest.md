[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentRequest

[Previous](CommentDeleteBatch.md) | [Next](CommentRequestByClient.md)

# IMTManagerAPI::CommentRequest

Get a comment by identifier.

C++
    
    
    MTAPIRES  IMTManagerAPI::CommentRequest(
       const UINT64  comment_id,   // identifier
       IMTComment*   comment       // comment object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.CommentRequest(
       ulong         comment_id,   // identifier
       CIMTComment   comment       // Comment object
       )

### Parameters

**comment_id**  
[in] Comment object (IMTComment::RecordID).

**comment**  
[out] Comment object. The 'comment' object must be previously created using theIMTManagerAPI::CommentCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method copies data of a comment with the specified ID, to the 'comment' object.
