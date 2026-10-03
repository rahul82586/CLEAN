[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon Flags

[Previous](IMTCon-ProviderToken.md) | [Next](IMTCon-CountryAdd.md)

# IMTConKYC::Flags

Get additional settings of the KYC provider.

C++
    
    
    UINT64  IMTConKYC::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConKYC.Flags()

### Return Value

Additional settings as the values of the [IMTConKYC::EnFlags (#enflags)](IMTCon-Enumerations.md#enflags) enumeration.

# IMTConKYC::Flags

Set additional settings of the KYC provider.

C++
    
    
    MTAPIRES  IMTConKYC::Flags(
       const UINT64  flags   // KYC provider settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.Flags(
       EnFlags       flags   // KYC provider settings
       )

### Parameters

**flags**  
[in] Additional settings as the values of theIMTConKYC::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
