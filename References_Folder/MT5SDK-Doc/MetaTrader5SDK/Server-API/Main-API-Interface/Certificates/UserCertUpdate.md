[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Certificates](../Certificates.md) / UserCertUpdate

[Previous](UserCertCreate.md) | [Next](UserCertGet.md)

# IMTServerAPI::UserCertUpdate

Add or update a client certificate.
    
    
    MTAPIRES  IMTServerAPI::UserCertUpdate(
       const UINT64     login            // Login
       IMTCertificate*  certificate      // The object of the certificate
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
