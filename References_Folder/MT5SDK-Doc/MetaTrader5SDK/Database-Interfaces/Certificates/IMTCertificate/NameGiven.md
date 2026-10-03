[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / NameGiven

[Previous](NameOrganizationUnit.md) | [Next](../../Price-Data.md)

# IMTCertificate::NameGiven

Gets the name of the person (G), to whom the loaded certificate has been issued.

C++
    
    
    MTAPIRES  IMTCertificate::NameGiven(
       MTAPISTR&   name     // person name
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.NameGiven(
       out string  name     // person name
       )

### Parameters

**name**  
[out] A reference to the name of the person (G), to whom the loaded certificate has been issued.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Certificates ate opened (loaded) using the [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) methods.
