[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Certificates](../Certificates.md) / UserCertGet

[Previous](UserCertUpdate.md) | [Next](UserCertDelete.md)

# IMTServerAPI::UserCertGet

Get the certificate of a client by the login.
    
    
    MTAPIRES  IMTServerAPI::UserCertGet(
       const UINT64      login,            // Client login
       IMTCertificate*   certificate       // The object of the certificate
       )

### Parameters

**login**  
[in] The login of a client.

**certificate**  
[out] The object of the certificate. The certificate object must be first created using theIMTServerAPI::UserCertCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified login to the certificate object.
