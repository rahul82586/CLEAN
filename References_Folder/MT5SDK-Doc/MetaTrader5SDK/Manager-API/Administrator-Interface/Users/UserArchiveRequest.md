[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserArchiveRequest

[Previous](UserArchiveBatch.md) | [Next](UserArchiveRequestArray.md)

# IMTAdminAPI::UserArchiveRequest

Request a client record from an archive database.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserArchiveRequest(
       const UINT64  login,     // Login
       IMTUser*      user       // An object of the client record
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserArchiveRequest(
       ulong         login,     // Login
       CIMTUser      user       // An object of the client record
       )

Python
    
    
    AdminAPI.UserArchiveRequest(
       login         # Login
       )

### Parameters

**login**  
[in] The login of a user.

**user**  
[out] An object of the client login. The user object must first be created using theIMTAdminAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).
