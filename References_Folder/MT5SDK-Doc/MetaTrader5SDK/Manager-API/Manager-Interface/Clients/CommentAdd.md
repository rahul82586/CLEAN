[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentAdd

[Previous](CommentCreateArray.md) | [Next](CommentAddBatch.md)

# IMTManagerAPI::CommentAdd

Add a comment to a document or client.

C++
    
    
    MTAPIRES  IMTManagerAPI::CommentAdd(
       IMTComment*   comment   // comment object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.CommentAdd(
       CIMTComment   comment   // comment object
       )

### Parameters

**document**  
[in]Comment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To add a comment to a client, specify the client ID in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md). To add a comment to a document, specify appropriate identifiers both in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md) and in [IMTComment::RelatedDocument](../../../Database-Interfaces/Clients/IMTComment/RelatedDocument.md).
