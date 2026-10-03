[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentRequestByDocument

[Previous](CommentRequestByClient.md) | [Next](AttachmentCreate.md)

# IMTManagerAPI::CommentRequestByDocument

Get comments on client documents by position.

C++
    
    
    MTAPIRES  IMTManagerAPI::CommentRequestByDocument(
       const UINT64        document_id,  // document identifier
       cost UINT          position,     // initial position
       const UINT          total,        // number
       IMTCommentArray*    comments      // array of documents
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.CommentRequestByDocument(
       ulong               document_id,  // document identifier
       uint                position,     // initial position
       uint                total,        // number
       CIMTCommentArray    comments      // array of documents
       )

### Parameters

**document_id**  
[in] Document ID (IMTDocument::RecordID).

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
