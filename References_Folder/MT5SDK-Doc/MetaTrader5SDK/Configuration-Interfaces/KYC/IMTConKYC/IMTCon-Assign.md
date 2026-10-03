[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon Assign

[Previous](IMTCon-Release.md) | [Next](IMTCon-Clear.md)

# IMTConKYC::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConKYC::Assign(
       const IMTConKYC*  config  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Assign(
       CIMTConKYC        config  // Source object
       )

### Parameters

**config**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
