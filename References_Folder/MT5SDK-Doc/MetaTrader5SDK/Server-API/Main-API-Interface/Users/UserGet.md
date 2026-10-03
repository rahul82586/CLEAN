[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserGet

[Previous](UserTotal.md) | [Next](UserGroup.md)

# IMTServerAPI::UserGet

Get a client record by the login.
    
    
    MTAPIRES  IMTServerAPI::UserGet(
       const UINT64  login,     // Client login
       IMTUser*      user       // An object of the client record
       )

### Parameters

**login**  
[in] The login of a client.

**user**  
[out] An object of the client login. The user object must first be created using theIMTServerAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified login to the user object.
