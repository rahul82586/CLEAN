[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / CommentDeleteBatch

[Previous](CommentDelete.md) | [Next](CommentRequest.md)

# IMTAdminAPI::CommentDeleteBatch

Delete a batch of comments from a document or client.

C++
    
    
    MTAPIRES  IMTAdminAPI::CommentDeleteBatch(
       const UINT64*  comment_ids,        // document identifiers
       const UINT     comment_ids_total,  // number of documents
       MTAPIRES*      results             // results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CommentDeleteBatch(
       ulong[]        comment_ids,        // document identifiers
       MTRetCode[]    retcodes            // results
       )

### Parameters

**comment_ids**  
[in] The identifiers of the documents (IMTDocument::RecordId) to be deleted.

**comment_ids_total**  
[in] The number of identifiers in the comment_ids array.

**results**  
[out] An array with document deletion results. The size of the 'results' array must not be less than that of 'comment_ids'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified documents have been deleted. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the documents have been deleted. Analyze the 'results' array for more details of the execution results. The result of deletion of each document from the 'comment_ids' array is added to 'results'. The index of a result corresponds to the index of a document in the source array.

### Note

Documents can only be deleted from the applications connected to the trading server, on which the client has been created ([IMTComment::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). The [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) response code will be returned for all other applications. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
