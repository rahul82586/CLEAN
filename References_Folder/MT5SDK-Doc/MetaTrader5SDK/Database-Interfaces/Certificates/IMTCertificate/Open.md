[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / Open

[Previous](Clear.md) | [Next](OpenMemory.md)

# IMTCertificate::Open

Loads certificate description from a specified file.

C++
    
    
    MTAPIRES  IMTCertificate::Open(
       LPCWSTR  filename      // Path to the file
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.Open(
       string   filename      // Path to the file
       )

### Parameters

**filename**  
[in] The path to the file, from which the certificate should be loaded.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Certificate description is loaded in th binary format DER.
