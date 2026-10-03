[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserArchive

[Previous](UserDepositChangeRaw.md) | [Next](UserArchiveGet.md)

# IMTServerAPI::UserArchive

Move a client record to an archive database.
    
    
    MTAPIRES  IMTServerAPI::UserArchive(
       const UINT64  login,              // User's login
       )

### Parameters

**login**  
[in] The login of a user that will be moved to an archive.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
