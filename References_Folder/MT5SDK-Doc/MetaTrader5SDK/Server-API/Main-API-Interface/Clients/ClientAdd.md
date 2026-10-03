[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientAdd

[Previous](ClientUnsubscribe.md) | [Next](ClientUpdate.md)

# IMTServerAPI::ClientAdd

Add a client to the server database.
    
    
    MTAPIRES  IMTServerAPI::ClientAdd(
       IMTClient*    client,  // Client object
       const UINT64  author   // Author
       )

### Parameters

**client**  
[in]Client object.

**author**  
[in] The login of the manager account, on whose behalf the client is being added. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A client can only be added to the database of the server, on which the plugin is running.
