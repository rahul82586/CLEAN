[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / Close

[Previous](Save.md) | [Next](Raw.md)

# IMTCertificate::Close

Closes (unloads) a certificate that was earlier opened by [IMTCertificate::Open](Open.md) or [IMTCertificate::OpenMemory](OpenMemory.md) method.

C++
    
    
    MTAPIRES  IMTCertificate::Close()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.Close()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
