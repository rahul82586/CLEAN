[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientUserLogins

[Previous](ClientUserDelete.md) | [Next](DocumentCreate.md)

# IMTServerAPI::ClientUserLogins

Get the list of client's trading accounts.
    
    
    MTAPIRES  IMTServerAPI::ClientUserLogins(
       const UINT64   client_id,    // ID
       UINT64*&       logins,       // Array of accounts
       UINT&          logins_total  // Number of accounts
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**logins**  
[out] Array with account logins. The login is equal toIMTUser::Login.

**logins_total**  
[out] The number of accounts in the 'logins' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method allocates and fills an array of accounts. A pointer to the passed block is placed to the 'logins' parameter. After use, the array placed in the 'logins' variable must be released using the [IMTServerAPI::Free](../Common-Functions/Free.md) Server API method.
