[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / IsEqual

[Previous](IsCA.md) | [Next](SerialNumber.md)

# IMTCertificate::IsEqual

Checks if the passed certificate is identical to the loaded one.

C++
    
    
    bool  IMTCertificate::IsEqual(
       const IMTCertificate*  certificate      // Certificate object
       )

.NET (Gateway/Manager API)
    
    
    bool  CIMTCertificate.IsEqual(
       CIMTCertificate        certificate      // Certificate object
       )

### Parameters

**certificate**  
[in] The object of the certificate that you want to compare to the loaded one.

### Return Value

The value of 0 means that the certificate is not identical, 1 - the certificate is identical.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
