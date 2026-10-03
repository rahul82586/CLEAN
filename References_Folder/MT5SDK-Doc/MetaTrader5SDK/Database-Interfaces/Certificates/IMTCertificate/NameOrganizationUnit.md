[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / NameOrganizationUnit

[Previous](NameOrganization.md) | [Next](NameGiven.md)

# IMTCertificate::NameOrganizationUnit

Gets the name of the organization unit (OU), to which the loaded certificate has been issued.

C++
    
    
    MTAPIRES  IMTCertificate::NameOrganizationUnit(
       MTAPISTR&   name     // The name of the organizational unit
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.NameOrganizationUnit(
       out string  name     // The name of the organizational unit
       )

### Parameters

**name**  
[out] A reference to the name of the organization unit (OU), to which the certificate has been issued.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
