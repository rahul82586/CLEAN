[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentAddBatch

[Previous](DocumentAdd.md) | [Next](DocumentAddBatchArray.md)

# IMTAdminAPI::DocumentAddBatch

Add a document to a client record.

C++
    
    
    MTAPIRES  IMTAdminAPI::DocumentAddBatch(
       IMTDocumentArray*  documents,  // array of documents
       MTAPIRES*          results     // array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DocumentAddBatch(
       CIMTDocumentArray  documents,  // array of documents
       MTRetCode[]        retcodes    // array of results
       )

### Parameters

**documents**  
[in]Document array object.

**results**  
[out] An array with document addition results. The size of the 'results' array must not be less than that of 'documents'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code means that all the specified documents have been added. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the documents have been added. Analyze the 'results' array for more details of the execution results. The result of adding of each document from the 'documents' array is added to 'results'. The index of a result corresponds to the index of a document in the source array.

### Note

A document can only be added from the applications connected to the same trading server on which the client has been created ([IMTDocument::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). The [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) response code will be returned for all other applications. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
