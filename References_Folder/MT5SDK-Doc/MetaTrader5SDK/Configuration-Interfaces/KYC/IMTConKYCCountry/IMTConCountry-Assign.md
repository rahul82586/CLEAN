[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCCountry](../IMTConCountry.md) / IMTConCountry Assign

[Previous](IMTConCountry-Release.md) | [Next](IMTConCountry-Clear.md)

# IMTConKYCCountry::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConKYCCountry::Assign(
       const IMTConKYCCountry*  country  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYCCountry.Assign(
       CIMTConKYCCountry        country  // Source object
       )

### Parameters

**country**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
