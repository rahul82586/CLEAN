[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentRequest

[Previous](DocumentDeleteBatch.md) | [Next](DocumentRequestByClient.md)

# IMTAdminAPI::DocumentRequest

Get a document by identifier.

C++
    
    
    MTAPIRES  IMTAdminAPI::DocumentRequest(
       const UINT64  document_id,  // identifier
       IMTDocument*  document      // document object
       )

.NET
    
    
    MTRetCode  IMTAdminAPI::DocumentRequest(
       ulong         document_id,  // identifier
       CIMTDocument  document      // document object
       )

### Parameters

**document_id**  
[in] Document ID (IMTDocument::RecordID).

**document**  
[out] Document object. The 'document' object must be previously created using theIMTAdminAPI::DocumentCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method copies data of a document with the specified ID, to the 'document' object.
