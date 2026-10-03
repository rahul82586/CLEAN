[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificateDelete

[Previous](TLSCertificateUpdate.md) | [Next](TLSCertificateShift.md)

# IMTServerAPI::TLSCertificateDelete

Delete an SSL certificate from access servers by position.
    
    
    MTAPIRES  IMTServerAPI::TLSCertificateDelete(
       const UINT     pos         // Certificate position
       )

### Parameters

**pos**  
[in] Certificate position starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Certificates can only be deleted from plugins running on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
