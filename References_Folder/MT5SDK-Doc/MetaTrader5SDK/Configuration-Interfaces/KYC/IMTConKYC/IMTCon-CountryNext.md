[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon CountryNext

[Previous](IMTCon-CountryTotal.md) | [Next](IMTCon-GroupAdd.md)

# IMTConKYC::CountryNext

Get the country for which the KYC provider is used by its index in the list.

C++
    
    
    MTAPIRES  IMTConKYC::CountryNext(
       const UINT         pos,      // Country position
       IMTConKYCCountry*  country   // Country object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.CountryNext(
       uint               pos,      // Country position
       CIMTConKYCCountry  country   // Country object
       )

### Parameters

**pos**  
[in] The position of the country in the list, starting from 0.

**country**  
[out] Country object. The 'country' object must be created in advance using theIMTServerAPI::KYCCountryCreateorIMTAdminAPI::KYCCountryCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
