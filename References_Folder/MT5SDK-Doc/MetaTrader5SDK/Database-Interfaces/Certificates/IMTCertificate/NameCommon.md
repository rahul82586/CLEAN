[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / NameCommon

[Previous](ValidTo.md) | [Next](NameIssuer.md)

# IMTCertificate::NameCommon

Gets the common name of the loaded certificate.

C++
    
    
    MTAPIRES  IMTCertificate::NameCommon(
       MTAPISTR&   name     // Common name
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.NameCommon(
       out string  name     // Common name
       )

### Parameters

**name**  
[out] A reference to the common name (CN) of the certificate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
