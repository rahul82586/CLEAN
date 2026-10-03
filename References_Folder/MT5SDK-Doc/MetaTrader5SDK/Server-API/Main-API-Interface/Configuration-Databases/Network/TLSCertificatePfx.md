[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificatePfx

[Previous](TLSCertificateNext.md) | [Next](../Plugins.md)

# IMTServerAPI::TLSCertificatePfx

Get the file of a certificate installed for access servers, by index.
    
    
    void*  IMTServerAPI::TLSCertificatePfx(
       const UINT     pos,                  // Certificate position
       UINT&          pfx_certificate_size  // Name
       )

### Return Value

A pointer to a .pfx certificate file. After use, the memory allocated for the certificate must be freed by [IMTServerAPI::Free](../../Common-Functions/Free.md).

### Note

Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../../Web-API/README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../../Web-API/Format-of-Commands.md)" section.
