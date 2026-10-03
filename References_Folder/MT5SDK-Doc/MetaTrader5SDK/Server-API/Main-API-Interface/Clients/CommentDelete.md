[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentDelete

[Previous](CommentUpdate.md) | [Next](CommentGet.md)

# IMTServerAPI::CommentDelete

Delete a comment from a document or client.
    
    
    MTAPIRES  IMTServerAPI::CommentDelete(
       IMTComment*   comment,   // Comment object
       const UINT64  author     // Author
       )

### Parameters

**comment**  
[in]Comment object.

**author**  
[in] The login of the manager account, on whose behalf the comment is being deleted. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A comment can only be deleted from plugins running on the same trade server where the client was created ([IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md)). For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
