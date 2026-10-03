[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / OpenMemory

[Previous](Open.md) | [Next](Save.md)

# IMTCertificate::OpenMemory

Loads certificate description from the memory.

C++
    
    
    MTAPIRES  IMTCertificate::OpenMemory(
       const void  *data,     // A pointer to memory
       const UINT  size       // Data size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.OpenMemory(
       byte[]      data       // Data array
       )

### Parameters

***data**  
[in] A pointer to memory, from which the certificate description should be loaded.

**size**  
[in] Amount of loaded data in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
