[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCCountry](../IMTConCountry.md) / IMTConCountry Clear

[Previous](IMTConCountry-Assign.md) | [Next](IMTConCountry-CountryCode.md)

# IMTConKYCCountry::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConKYCCountry::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYCCountry.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

This method cleans all fields ​​and removes embedded objects.
