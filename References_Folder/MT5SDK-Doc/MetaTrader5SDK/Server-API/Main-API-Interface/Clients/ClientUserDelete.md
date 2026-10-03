[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientUserDelete

[Previous](ClientUserAdd.md) | [Next](ClientUserLogins.md)

# IMTServerAPI::ClientUserDelete

Unbind a trading account from a client.
    
    
    MTAPIRES  IMTServerAPI::ClientUserDelete(
       const UINT64   client_id,  // Identifier
       const UINT64   login       // Account number
       )

### Parameters

**client_id**  
[in] The ID of the client (IMTClient::RecordID), from which the account should be unbound.

**login**  
[in] The login of the account (IMTUser::Login), which is unbound from the client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method does not delete the trading account. It unbinds the account from the client.
