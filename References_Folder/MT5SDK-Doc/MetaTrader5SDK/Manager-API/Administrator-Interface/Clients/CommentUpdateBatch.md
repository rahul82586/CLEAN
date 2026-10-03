[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / CommentUpdateBatch

[Previous](CommentUpdate.md) | [Next](CommentUpdateBatchArray.md)

# IMTAdminAPI::CommentUpdateBatch

Update a batch of comments to a document or client.

C++
    
    
    MTAPIRES  IMTAdminAPI::CommentUpdateBatch(
       IMTCommentArray*  comments,   // array of comments
       MTAPIRES*         results     // array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CommentUpdateBatch(
       CIMTCommentArray  comments,   // array of comments
       MTRetCode[]       retcodes    // array of results
       )

### Parameters

**comments**  
[in]Object of the comments array.

**results**  
[out] An array with the results of updating of comments. The size of the 'results' array must not be less than that of 'comments'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code means that all the specified comments have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the comments have been updated. Analyze the 'results' array for more details of the execution results. The result of update of each comment from the 'comments' array is added to 'results'. The index of a result corresponds to the index of a comment in the source array.

### Note

To update a comment to a client, specify the client ID in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md). To edit a comment to a document, specify appropriate identifiers both in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md) and in [IMTComment::RelatedDocument](../../../Database-Interfaces/Clients/IMTComment/RelatedDocument.md).
