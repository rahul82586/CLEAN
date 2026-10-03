[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserArchiveGet

[Previous](UserArchive.md) | [Next](UserArchiveLogins.md)

# IMTServerAPI::UserArchiveGet

Request a client record from an archive database.
    
    
    MTAPIRES  IMTServerAPI::UserArchiveGet(
       const UINT64  login,     // Login
       IMTUser*      user       // An object of the client record
       )

### Parameters

**login**  
[in] The login of a user.

**user**  
[out] An object of the client login. The user object must first be created using theIMTServerAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
