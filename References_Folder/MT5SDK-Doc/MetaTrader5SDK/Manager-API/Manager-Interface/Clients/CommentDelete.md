[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentDelete

[Previous](CommentUpdateBatchArray.md) | [Next](CommentDeleteBatch.md)

# IMTManagerAPI::CommentDelete

Delete a comment from a document or client.

C++
    
    
    MTAPIRES  IMTManagerAPI::CommentDelete(
       IMTComment*  comment  // comment object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.CommentDelete(
       CIMTComment  comment  // comment object
       )

### Parameters

**comment**  
[in]Comment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Comments can only be deleted from the applications connected to the trading server, on which the client has been created ([IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). The [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) response code will be returned for all other applications. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
