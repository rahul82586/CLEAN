[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientUpdate

[Previous](ClientAdd.md) | [Next](ClientDelete.md)

# IMTServerAPI::ClientUpdate

Update a client in the server database.
    
    
    MTAPIRES  IMTServerAPI::ClientUpdate(
       IMTClient*    client,  // Client object
       const UINT64  author   // Author
       )

### Parameters

**client**  
[in]Client object.

**author**  
[in] The login of the manager account, on whose behalf the client is being updated. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A client can only be updated from the plugins running on the same trade server where the client was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
