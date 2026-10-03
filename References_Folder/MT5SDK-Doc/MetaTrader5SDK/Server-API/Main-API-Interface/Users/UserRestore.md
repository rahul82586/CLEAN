[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserRestore

[Previous](UserArchiveLogins.md) | [Next](NotificationsSend.md)

# IMTServerAPI::UserRestore

Restore a client record from an archive or a backup database.
    
    
    MTAPIRES  IMTServerAPI::UserRestore(
       IMTUser*  user      // A client base to restore
       )

### Parameters

**user**  
[in] An object of the client record to restore.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Restored users are not deleted from the archive.
