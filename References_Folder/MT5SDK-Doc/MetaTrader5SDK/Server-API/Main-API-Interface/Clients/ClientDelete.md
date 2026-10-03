[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientDelete

[Previous](ClientUpdate.md) | [Next](ClientGet.md)

# IMTServerAPI::ClientDelete

Delete a client from the server database.
    
    
    MTAPIRES  IMTServerAPI::ClientDelete(
       const UINT64  client_id,  // Identifier
       const UINT64  author      // Author
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**author**  
[in] The login of the manager account, on whose behalf the client is being deleted. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A client can only be deleted from the plugins running on the same trade server where the client was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
