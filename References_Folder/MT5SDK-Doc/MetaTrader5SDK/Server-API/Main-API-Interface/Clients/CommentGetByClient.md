[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentGetByClient

[Previous](CommentGet.md) | [Next](CommentGetByDocument.md)

# IMTServerAPI::CommentGetByClient

Get comments on a client by position.
    
    
    MTAPIRES  IMTServerAPI::CommentGetByClient(
       const UINT64        client_id,  // Client ID
       const UINT          position,   // Start position
       const UINT          total,      // Number
       IMTCommentArray*    comments    // Array of comments
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**position**  
[in] Position in the list of comments, starting with 0. The method returns comments starting with this position.

**total**  
[in] The number of comments which should be received.

**comments**  
[out] An object of an array of comments. The 'comments' object must be previously created using theIMTServerAPI::CommentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
