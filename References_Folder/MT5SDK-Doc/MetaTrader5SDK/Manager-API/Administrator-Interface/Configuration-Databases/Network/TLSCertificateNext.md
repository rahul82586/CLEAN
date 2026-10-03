[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificateNext

[Previous](TLSCertificateTotal.md) | [Next](../Plugins.md)

# IMTAdminAPI::TLSCertificateNext

Get the data of a certificate installed for access servers, by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::TLSCertificateNext(
       const UINT     pos,        // Certificate position
       MTAPISTR&      name,       // Name
       MTAPISTR&      thumbprint  // Thumbprint
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI::TLSCertificateNext(
       uint           pos,        // Certificate position
    0   out string     name,       // Name
       out string     thumbprint  // Thumbprint
       )

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../../Web-API/README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../../Web-API/Format-of-Commands.md)" section.
