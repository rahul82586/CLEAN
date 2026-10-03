[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserCertUpdate

[Previous](UserCertCreate.md) | [Next](UserCertGet.md)

# IMTAdminAPI::UserCertUpdate

Add or update a client certificate.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserCertUpdate(
       const UINT64     login            // Login
       IMTCertificate*  certificate      // The object of the certificate
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserCertUpdate(
       ulong            login            // Login
       CIMTCertificate  certificate      // The object of the certificate
       )

Python
    
    
    AdminAPI.UserCertUpdate(
       login            # Login
       certificate      # The object of the certificate
       )

### Parameters

**login**  
[in] The login of the client whose certificate needs to be replaced.

**certificate**  
[in]The object of the certificatethat will replace the current certificate of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If a client already has a certificate, it is updated, otherwise a new certificate is added.
