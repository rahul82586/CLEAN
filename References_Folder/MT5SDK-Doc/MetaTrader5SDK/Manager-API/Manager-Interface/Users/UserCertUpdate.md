[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCertUpdate

[Previous](UserCertCreate.md) | [Next](UserCertGet.md)

# IMTManagerAPI::UserCertUpdate

Add or update a client certificate.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserCertUpdate(
       const UINT       login            // Login
       IMTCertificate*  certificate      // The object of the certificate
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserCertUpdate(
       ulong            login            // Login
       CIMTCertificate  obj              // The object of the certificate
       )

Python
    
    
    ManagerAPI.UserCertUpdate(
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

A certificate can be updated only from the applications that are connected to the same trade server where the client account was created. If the client with the specified login is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
