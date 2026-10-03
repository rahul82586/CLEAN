[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / IsOpened

[Previous](RawSize.md) | [Next](IsRoot.md)

# IMTCertificate::IsOpened

Checks whether an object interface has an open certificate.

C++
    
    
    bool  IMTCertificate::IsOpened()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTCertificate.IsOpened()

### Return Value

0 means there is no open certificate, 1 0 there is an open certificate.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
