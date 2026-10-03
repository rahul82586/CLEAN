[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentRequestByClient

[Previous](CommentRequest.md) | [Next](CommentRequestByDocument.md)

# IMTManagerAPI::CommentRequestByClient

Get comments on a client by position.

C++
    
    
    MTAPIRES  IMTManagerAPI::CommentGetByClient(
       const UINT64        client_id,  // client identifier
       const UINT          position,   // initial position
       const UINT          total,      // number
       IMTCommentArray*    comments    // array of comments
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.CommentGetByClient(
       ulong               client_id,  // client identifier
       uint                position,   // initial position
       uint                total,      // number
       CIMTCommentArray    comments    // array of comments
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**position**  
[in] Position in the list of comments, starting with 0. The method returns comments starting with this position.

**total**  
[in] The number of comments which should be received.

**comments**  
[out] An object of an array of comments. The 'comments' object must be previously created using theIMTManagerAPI::CommentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
