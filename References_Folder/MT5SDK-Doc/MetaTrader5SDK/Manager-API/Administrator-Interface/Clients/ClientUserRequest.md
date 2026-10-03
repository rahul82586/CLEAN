[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / ClientUserRequest

[Previous](ClientUserDeleteBatch.md) | [Next](DocumentCreate.md)

# IMTAdminAPI::ClientUserRequest

Get the list of client's trading accounts.

C++
    
    
    MTAPIRES  IMTAdminAPI::ClientUserRequest(
       const UINT64   client_id,    // identifier
       UINT64*&       logins,       // array of accounts
       UINT&          logins_total  // number of accounts
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ClientUserRequest(
       ulong          client_id,    // identifier
       ulong[]        logins        // array of accounts
       )

Python
    
    
    AdminAPI.ClientUserRequest(
       int            client_id     # identifier
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**logins**  
[out] Array with account logins. The login is equal toIMTUser::Login.

**logins_total**  
[out] The number of accounts in the 'logins' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method allocates and fills an array of accounts. A pointer to the passed block is placed to the 'logins' parameter. After use, the array placed in the 'logins' variable must be released using the [IMTAdminAPI::Free](../Common-Functions/Free.md) method.
