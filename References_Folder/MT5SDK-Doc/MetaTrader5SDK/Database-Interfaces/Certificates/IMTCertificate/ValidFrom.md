[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / ValidFrom

[Previous](SerialNumber.md) | [Next](ValidTo.md)

# IMTCertificate::ValidFrom

Gets date since which the loaded certificate is valid.

C++
    
    
    INT64  IMTCertificate::ValidFrom()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTCertificate.ValidFrom()

### Return Value

The date since which the loaded certificate is valid. The date is passed as a number of seconds that have elapsed since 01.01.1970.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
