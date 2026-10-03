[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCCountry](../IMTConCountry.md) / IMTConCountry CountryCode

[Previous](IMTConCountry-Clear.md) | [Next](../IMTConGroup.md)

# IMTConKYCCountry::CountryCode

Get the country code specified in the KYC provider configuration.

C++
    
    
    LPCWSTR  IMTConKYCCountry::CountryCode()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYCCountry.CountryCode()

### Return Value

If successful, a pointer to a string with a three-digit [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166) country code is returned. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConKYCCountry](../IMTConCountry.md) object.

# IMTConKYCCountry::CountryCode

Set a country code in the KYC provider settings.

C++
    
    
    MTAPIRES  IMTConKYCCountry::CountryCode(
       LPCWSTR  code      // Country code
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYCCountry.CountryCode(
       srting   code      // Country code
       )

### Parameters

**code**  
[in] Three-digitISO 3166country code.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
