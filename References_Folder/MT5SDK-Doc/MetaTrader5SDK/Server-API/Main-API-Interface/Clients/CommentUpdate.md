[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentUpdate

[Previous](CommentAdd.md) | [Next](CommentDelete.md)

# IMTServerAPI::CommentUpdate

Change a comment to a document or client.
    
    
    MTAPIRES  IMTServerAPI::CommentUpdate(
       IMTComment*   comment,   // Comment object
       const UINT64  author     // Author
       )

### Parameters

**comment**  
[in]Comment object.

**author**  
[in] The login of the manager account, on whose behalf the comment is being updated. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To update a comment to a client, specify the client ID in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md). To update a comment to a document, specify appropriate IDs both in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md) and in [IMTComment::RelatedDocument](../../../Database-Interfaces/Clients/IMTComment/RelatedDocument.md).
