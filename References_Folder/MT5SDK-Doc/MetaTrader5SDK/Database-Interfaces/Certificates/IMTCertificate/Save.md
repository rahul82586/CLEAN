[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / Save

[Previous](OpenMemory.md) | [Next](Close.md)

# IMTCertificate::Save

Saves the certificate to a file.

C++
    
    
    MTAPIRES  IMTCertificate::Save(
       LPCWSTR  filename      // Path to the file
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.Save(
       string   filename      // Path to the file
       )

### Parameters

**filename**  
[in] The path to the file, to which the certificate should be saved.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
