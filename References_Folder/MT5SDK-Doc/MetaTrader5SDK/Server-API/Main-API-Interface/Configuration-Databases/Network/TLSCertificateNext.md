[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificateNext

[Previous](TLSCertificateTotal.md) | [Next](TLSCertificatePfx.md)

# IMTServerAPI::TLSCertificateNext

Get the data of a certificate installed for access servers, by index.
    
    
    MTAPIRES  IMTServerAPI::TLSCertificateNext(
       const UINT     pos,        // Certificate position
       MTAPISTR&      name,       // Name
       MTAPISTR&      thumbprint  // Thumbprint
       )

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../../Web-API/README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../../Web-API/Format-of-Commands.md)" section.
