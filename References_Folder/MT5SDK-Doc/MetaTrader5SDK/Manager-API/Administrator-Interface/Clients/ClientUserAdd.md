[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / ClientUserAdd

[Previous](ClientRequestHistory.md) | [Next](ClientUserAddBatch.md)

# IMTAdminAPI::ClientUserAdd

Bind a trading account to a client.

C++
    
    
    MTAPIRES  IMTAdminAPI::ClientUserAdd(
       const UINT64   client_id,  // identifier
       const UINT64   login       // account number
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ClientUserAdd(
       ulong          client_id,  // identifier
       ulong          login       // account number
       )

Python
    
    
    AdminAPI.ClientUserAdd(
       int            client_id,  # identifier
       int            login       # account number
       )

### Parameters

**client_id**  
[in] The ID of the client (IMTClient::RecordID), to which the account should be linked.

**login**  
[in] The login of the account (IMTUser::Login), which should be linked to the client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method does not create a trading account. It binds an existing account to a client.
