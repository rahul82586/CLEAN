[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentUpdateBatchArray

[Previous](CommentUpdateBatch.md) | [Next](CommentDelete.md)

# IMTManagerAPI::CommentUpdateBatchArray

Update a batch of comments to a document or client.

C++
    
    
    MTAPIRES  IMTManagerAPI::CommentUpdateBatchArray(
       IMTComment**   comments,        // array of documents
       const UINT     comments_total,  // number of documents in the array
       MTAPIRES*      results          // array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.CommentUpdateBatchArray(
       CIMTComment[]  comments,        // array of documents
       MTRetCode[]    retcodes         // array of results
       )

### Parameters

**comments**  
[in] Array ofcomment objects.

**comments_total**  
[in] The number of comments in the 'comments' object.

**results**  
[out] An array with the results of updating of comments. The size of the 'results' array must not be less than that of 'comments'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code means that all the specified comments have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the comments have been updated. Analyze the 'results' array for more details of the execution results. The result of update of each comment from the 'comments' array is added to 'results'. The index of a result corresponds to the index of a comment in the source array.

### Note

To update a comment to a client, specify the client ID in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md). To edit a comment to a document, specify appropriate identifiers both in [IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTComment/RelatedClient.md) and in [IMTComment::RelatedDocument](../../../Database-Interfaces/Clients/IMTComment/RelatedDocument.md).
