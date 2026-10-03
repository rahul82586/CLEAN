[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentGetByDocument

[Previous](CommentGetByClient.md) | [Next](AttachmentCreate.md)

# IMTServerAPI::CommentGetByClient

Get comments on client documents by position.
    
    
    MTAPIRES  IMTServerAPI::CommentGetByClient(
       const UINT64        document_id,  // Document identifier
       const UINT          position,     // Start position
       const UINT          total,        // Number
       IMTCommentArray*    comments      // Array of documents
       )

### Parameters

**document_id**  
[in] Document ID (IMTDocument::RecordID).

**position**  
[in] Position in the list of comments, starting with 0. The method returns comments starting with this position.

**total**  
[in] The number of comments which should be received.

**comments**  
[out] An object of an array of comments. The 'comments' object must be previously created using theIMTServerAPI::CommentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
