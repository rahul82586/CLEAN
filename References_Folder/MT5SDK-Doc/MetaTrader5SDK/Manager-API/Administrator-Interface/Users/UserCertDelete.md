[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserCertDelete

[Previous](UserCertGet.md) | [Next](UserCertConfirm.md)

# IMTAdminAPI::UserCertDelete

Reset the user certificate.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserCertDelete(
       const UINT64  login      // User's login
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserCertDelete(
       ulong         login      // User's login
       )

Python
    
    
    AdminAPI.UserCertDelete(
       login         # User's login
       )

### Parameters

**login**  
[in] The login of a user whose certificate needs to be reset.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the extended authorization mode is used for the group to which the account belongs, then using this command the previously issued certificate can be reset. After that, authorization with the certificate will be impossible, and a new certificate will be issued during the next attempt of the account to connect to the server.
