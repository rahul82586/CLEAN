[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserGroup

[Previous](UserGet.md) | [Next](UserLogins.md)

# IMTServerAPI::UserGroup

Get the group of a client by the login.
    
    
    MTAPIRES  IMTServerAPI::UserGroup(
       const UINT64  login,     // Client login
       MTAPISTR&     group      // Client group
       )

### Parameters

**login**  
[in] The login of a client.

**group**  
[out] The name of a user group to which the client belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
