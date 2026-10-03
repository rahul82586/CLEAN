[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / ValidTo

[Previous](ValidFrom.md) | [Next](NameCommon.md)

# IMTCertificate::ValidTo

Gets date until which the loaded certificate is valid.

C++
    
    
    INT64  IMTCertificate::ValidTo()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTCertificate.ValidTo()

### Return Value

The date until which the loaded certificate is valid. The date is passed as a number of seconds that have elapsed since 01.01.1970.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
