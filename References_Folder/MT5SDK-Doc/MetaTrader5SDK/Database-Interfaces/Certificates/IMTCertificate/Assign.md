[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTCertificate::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTCertificate::Assign(
       const IMTCertificate*  certificate      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.Assign(
       CIMTCertificate        certificate      // Source object
       )

### Parameters

**certificate**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
