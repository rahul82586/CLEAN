[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / SerialNumber

[Previous](IsEqual.md) | [Next](ValidFrom.md)

# IMTCertificate::SerialNumber

Gets the serial number of the loaded certificate.

C++
    
    
    UINT64  IMTCertificate::SerialNumber()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTCertificate.SerialNumber()

### Return Value

The serial number of the loaded certificate.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
