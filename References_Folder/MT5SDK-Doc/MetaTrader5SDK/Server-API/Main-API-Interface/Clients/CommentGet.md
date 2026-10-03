[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentGet

[Previous](CommentDelete.md) | [Next](CommentGetByClient.md)

# IMTServerAPI::CommentGet

Get a comment by identifier.
    
    
    MTAPIRES  IMTServerAPI::CommentGet(
       const UINT64  comment_id,   // Identifier
       IMTComment*   comment       // Comment object
       )

### Parameters

**comment_id**  
[in] Comment object (IMTComment::RecordID).

**comment**  
[out] Comment object. The 'comment' object must be previously created using theIMTServerAPI::CommentCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies data of a comment with the specified ID, to the 'comment' object.
