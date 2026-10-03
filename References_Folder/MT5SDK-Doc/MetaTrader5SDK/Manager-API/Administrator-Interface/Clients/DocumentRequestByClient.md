[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentRequestByClient

[Previous](DocumentRequest.md) | [Next](DocumentRequestHistory.md)

# IMTAdminAPI::DocumentRequestByClient

Get client documents.

C++
    
    
    MTAPIRES  IMTAdminAPI::DocumentRequestByClient(
       const UINT64        client_id,  // client identifier
       IMTDocumnentArray*  documents   // array of documents
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DocumentRequestByClient(
       ulong               client_id,  // client identifier
       CIMTDocumnentArray  documents   // array of documents
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**documents**  
[out] An object of an array of documents. The documents object must be previously created using theIMTAdminAPI::DocumentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
