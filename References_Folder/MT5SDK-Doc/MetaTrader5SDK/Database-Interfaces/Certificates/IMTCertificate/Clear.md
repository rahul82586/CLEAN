[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Certificates](../../Certificates.md) / [IMTCertificate](../IMTCertificate.md) / Clear

[Previous](Assign.md) | [Next](Open.md)

# IMTCertificate::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTCertificate::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCertificate.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
