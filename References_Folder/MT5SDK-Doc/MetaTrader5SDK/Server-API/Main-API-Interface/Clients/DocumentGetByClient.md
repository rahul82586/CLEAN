[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentGetByClient

[Previous](DocumentGet.md) | [Next](DocumentGetHistory.md)

# IMTServerAPI::DocumentGetByClient

Get client documents by position.
    
    
    MTAPIRES  IMTServerAPI::DocumentGetByClient(
       const UINT64        client_id,  // Client ID
       const UINT          position,   // Start position
       const UINT          total,      // Number
       IMTDocumnentArray*  documents   // Array of documents
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**position**  
[in] Position in the list of documents, starting with 0. The method returns documents starting with this position.

**total**  
[in] The number of documents which should be received.

**documents**  
[out] An object of an array of documents. The 'documents' object must be previously created using theIMTServerAPI::DocumentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
