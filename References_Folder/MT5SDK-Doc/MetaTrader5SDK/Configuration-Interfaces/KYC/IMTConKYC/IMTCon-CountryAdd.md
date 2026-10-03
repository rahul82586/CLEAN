[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon CountryAdd

[Previous](IMTCon-Flags.md) | [Next](IMTCon-CountryUpdate.md)

# IMTConKYC::CountryAdd

Add a country for which the KYC provider will be used.

C++
    
    
    MTAPIRES  IMTConKYC::CountryAdd(
       IMTConKYCCountry*  country      // Country object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.CountryAdd(
       CIMTConKYCCountry  country      // Country object
       )

### Parameters

**country**  
[in] TheIMTConKYCCountrycountry object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
