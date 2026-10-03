[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / ClientUserDelete

[Previous](ClientUserAddBatch.md) | [Next](ClientUserDeleteBatch.md)

# IMTAdminAPI::ClientUserDelete

Unbind a trading account from a client.

C++
    
    
    MTAPIRES  IMTAdminAPI::ClientUserDelete(
       const UINT64   client_id,  // identifier
       const UINT64   login       // account number
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ClientUserDelete(
       ulong          client_id,  // identifier
       ulong          login       // account number
       )

Python
    
    
    AdminAPI.ClientUserDelete(
       int            client_id,  # identifier
       int            login       # account number
       )

### Parameters

**client_id**  
[in] The ID of the client (IMTClient::RecordID), from which the account should be unbound.

**login**  
[in] The login of the account (IMTUser::Login), which is unbound from the client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The request does not delete the trading account. It unbinds the account from the client.
