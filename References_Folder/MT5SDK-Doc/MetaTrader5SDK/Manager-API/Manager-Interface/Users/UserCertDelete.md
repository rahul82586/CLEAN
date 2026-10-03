[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCertDelete

[Previous](UserCertGet.md) | [Next](UserCertConfirm.md)

# IMTManagerAPI::UserCertDelete

Reset the user certificate.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserCertDelete(
       const UINT64  login      // User's login
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserCertDelete(
       ulong         login      // User's login
       )

Python
    
    
    ManagerAPI.UserCertDelete(
       login         # User's login
       )

### Parameters

**login**  
[in] The login of a user whose certificate needs to be reset.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the extended authorization mode is used for the group to which the account belongs, then using this command the previously issued certificate can be reset. After that, authorization with the certificate will be impossible, and a new certificate will be issued during the next attempt of the account to connect to the server.
