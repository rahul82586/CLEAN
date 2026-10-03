[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentDeleteBatch

[Previous](DocumentDelete.md) | [Next](DocumentRequest.md)

# IMTAdminAPI::DocumentDeleteBatch

Delete a document from a client record.

C++
    
    
    MTAPIRES  IMTAdminAPI::DocumentDeleteBatch(
       const UINT64*  document_ids,       // document identifiers
       const UINT     document_ids_total, // number of documents
       MTAPIRES*      results             // results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DocumentDeleteBatch(
       ulong[]        document_ids,       // document identifiers
       MTRetCode[]    retcodes            // results
       )

### Parameters

**document_ids**  
[in] The identifiers of the documents (IMTDocument::RecordId) to be deleted.

**document_ids_total**  
[in] The number of identifiers in the document_ids array.

**results**  
[out] An array with document deletion results. The size of the 'results' array must not be less than that of 'document_ids'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified documents have been deleted. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the documents have been deleted. Analyze the 'results' array for more details of the execution results. The result of deletion of each document from the 'document_ids' array is added to 'results'. The index of a result corresponds to the index of a document in the source array.

### Note

A document can only be deleted from the applications connected to the trading server, on which the client has been created ([IMTDocument::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). The [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) response code will be returned for all other applications. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
