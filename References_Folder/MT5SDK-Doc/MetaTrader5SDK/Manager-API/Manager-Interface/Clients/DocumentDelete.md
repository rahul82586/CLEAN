[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / DocumentDelete

[Previous](DocumentUpdateBatchArray.md) | [Next](DocumentDeleteBatch.md)

# IMTManagerAPI::DocumentDelete

Delete a document from a client record.

C++
    
    
    MTAPIRES  IMTManagerAPI::DocumentDelete(
       const UINT64  document_id  // document identifier
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DocumentDelete(
       ulong         document_id  // document identifier
       )

### Parameters

**document**  
[in] The identifier of the document (IMTDocument::RecordId) to be deleted.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

A document can only be deleted from the applications connected to the trading server, on which the client has been created ([IMTDocument::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). The [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) response code will be returned for all other applications. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
