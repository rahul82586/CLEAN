[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentGet

[Previous](DocumentDelete.md) | [Next](DocumentGetByClient.md)

# IMTServerAPI::DocumentGet

Get a document by identifier.
    
    
    MTAPIRES  IMTServerAPI::DocumentGet(
       const UINT64  document_id,  // Identifier
       IMTDocument*  document      // Document object
       )

### Parameters

**document_id**  
[in] Document ID (IMTDocument::RecordID).

**document**  
[out] Document object. The 'document' object must be previously created using theIMTServerAPI::DocumentCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies data of a document with the specified ID, to the 'document' object.
