[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserCertGet

[Previous](UserCertUpdate.md) | [Next](UserCertDelete.md)

# IMTAdminAPI::UserCertGet

Get the certificate of a client by the login.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserCertGet(
       const UINT64      login,            // Client login
       IMTUCertificate*  certificate       // The object of the certificate
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserCertGet(
       ulong             login,            // Client login
       CIMTUCertificate  certificate       // The object of the certificate
       )

Python
    
    
    AdminAPI.UserCertGet(
       login,            # Client login
       certificate       # The object of the certificate
       )

### Parameters

**login**  
[in] The login of a client.

**certificate**  
[out] The object of the certificate. The certificate object must be first created using theIMTAdminAPI::UserCertCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified login to the certificate object.
