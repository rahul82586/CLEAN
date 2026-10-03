[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / IsRoot

[Previous](IsOpened.md) | [Next](IsCA.md)

# IMTCertificate::IsRoot

Checks if the loaded certificate is the root one.

C++
    
    
    bool  IMTCertificate::IsRoot()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTCertificate.IsRoot()

### Return Value

The value of 0 means that the certificate is not a root one, 1 - this is a root certificate.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
