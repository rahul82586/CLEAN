[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificateUpdate

[Previous](NetServerGet.md) | [Next](TLSCertificateDelete.md)

# IMTServerAPI::TLSCertificateUpdate

Add or update an SSL certificate on access servers.
    
    
    MTAPIRES  IMTServerAPI::TLSCertificateUpdate(
       const void*    pfx_certificate,       // Certificate
       const UINT     pfx_certificate_size,  // Certificate size
       LPCWSTR        password               // Certificate password
       )

### Parameters

**pfx_certificate**  
[in] A pointer to a file containing a certificate with a private key. If the file contains multiple certificates (for example a chain), only the first of them will be installed.

**pfx_certificate_size**  
[in] Certificate size in bytes.

**password**  
[in] The certificate cane be protected by a password. In this case, pass it in the 'password' parameter. Otherwise the certificate will not be installed and the method will return theMT_RET_AUTH_CERTIFICATE_BADerror.

  * The parameter is optional.
  * This password is only used for certificate installation on the local computer and is not transmitted anywhere.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When you call the method, the existence of the certificate to be added is checked. If it exists, the certificate is updated. Otherwise a new certificate is installed. The check is based on the "Thumbprint" certificate field.
