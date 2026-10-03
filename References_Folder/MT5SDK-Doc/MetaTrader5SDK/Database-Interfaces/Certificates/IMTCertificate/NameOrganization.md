[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / NameOrganization

[Previous](NameIssuer.md) | [Next](NameOrganizationUnit.md)

# IMTCertificate::NameOrganization

Gets the name of the organization (O), to which the loaded certificate has been issued.

C++
    
    
    MTAPIRES  IMTCertificate::NameOrganization(
       MTAPISTR&   name     // The name of the organization
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.NameOrganization(
       out string  name     // The name of the organization
       )

### Parameters

**name**  
[out] A reference to the name of the organization (O), to which the certificate has been issued.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
