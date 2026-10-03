[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon CountryUpdate

[Previous](IMTCon-CountryAdd.md) | [Next](IMTCon-CountryDelete.md)

# IMTConKYC::CountryUpdate

Change the country for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYC::CountryUpdate(
       const UINT               pos,      // Country position
       const IMTConKYCCountry*  country   // Country object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.CountryUpdate(
       uint                     pos,      // Country position
       CIMTConKYCCountry        country   // Country object
       )

### Parameters

**pos**  
[in] The position of the country in the list, starting from 0.

**country**  
[in] TheIMTConKYCCountrycountry object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
