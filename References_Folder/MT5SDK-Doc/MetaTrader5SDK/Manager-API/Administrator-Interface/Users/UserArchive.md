[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserArchive

[Previous](UserCertConfirm.md) | [Next](UserArchiveBatch.md)

# IMTAdminAPI::UserArchive

Move a user to an archive database.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserArchive(
       const UINT64  login      // Login
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserArchive(
       ulong         login      // Login
       )

Python
    
    
    AdminAPI.UserArchive(
       login         # Login
       )

### Parameters

**login**  
[in] The login of a user that will be moved to an archive.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
