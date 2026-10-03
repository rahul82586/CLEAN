[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / IsCA

[Previous](IsRoot.md) | [Next](IsEqual.md)

# IMTCertificate::IsCA

Checks the loaded certificate - if it is possible to generate other certificates on its basis.

C++
    
    
    bool  IMTCertificate::IsCA()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTCertificate.IsCA()

### Return Value

A value of 0 means that the generation of other certificates is not possible, 1 - the certificate allows generating other certificates on its basis.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
