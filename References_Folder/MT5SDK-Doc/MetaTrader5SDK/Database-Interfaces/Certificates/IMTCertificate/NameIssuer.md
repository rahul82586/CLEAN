[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / NameIssuer

[Previous](NameCommon.md) | [Next](NameOrganization.md)

# IMTCertificate::NameIssuer

Get the name of the issuer (vendor) of the loaded certificate.

C++
    
    
    MTAPIRES  IMTCertificate::NameIssuer(
       MTAPISTR&   name     // The name of the issuer
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.NameIssuer(
       out string  name     // The name of the issuer
       )

### Parameters

**name**  
[out] The name of the certificate issuer (provider).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
