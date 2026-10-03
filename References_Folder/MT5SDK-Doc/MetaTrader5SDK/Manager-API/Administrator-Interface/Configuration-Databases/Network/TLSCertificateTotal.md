[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificateTotal

[Previous](TLSCertificateShift.md) | [Next](TLSCertificateNext.md)

# IMTAdminAPI::TLSCertificateTotal

The total number of certificates installed for access servers.

C++
    
    
    UINT  IMTAdminAPI::TLSCertificateTotal()

.NET
    
    
    uint  CIMTAdminAPI::TLSCertificateTotal()

### Return Value

The number of installed certificates.

### Note

Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../../Web-API/README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../../Web-API/Format-of-Commands.md)" section.
