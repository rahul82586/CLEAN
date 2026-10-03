[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientGet

[Previous](ClientDelete.md) | [Next](ClientGetHistory.md)

# IMTServerAPI::ClientGet

Get a client by identifier.
    
    
    MTAPIRES  IMTServerAPI::ClientGet(
       const UINT64  client_id,  // Identifier
       IMTClient*    client      // Client object
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**client**  
[out] Client object. The 'client' object must be previously created using theIMTServerAPI::ClientCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies data of a client with the specified ID, to the 'client' object.
