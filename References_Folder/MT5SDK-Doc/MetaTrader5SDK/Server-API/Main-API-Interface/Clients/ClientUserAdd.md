[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientUserAdd

[Previous](ClientIdsByManager.md) | [Next](ClientUserDelete.md)

# IMTServerAPI::ClientUserAdd

Bind a trading account to a client.
    
    
    MTAPIRES  IMTServerAPI::ClientUserAdd(
       const UINT64   client_id,  // Identifier
       const UINT64   login       // Account number
       )

### Parameters

**client_id**  
[in] The ID of the client (IMTClient::RecordID), to which the account should be linked.

**login**  
[in] The login of the account (IMTUser::Login), which should be linked to the client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method does not create a trading account. It binds an existing account to a client.
