[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon ProviderType

[Previous](IMTCon-Name.md) | [Next](IMTCon-ProviderAddress.md)

# IMTConKYC::ProviderType

Get the KYC service provider selected in the configuration.

C++
    
    
    UINT  IMTConKYC::ProviderType()  const

.NET (Gateway/Manager API)
    
    
    EnProviderType  CIMTConKYC.ProviderType()

### Return Value

KYC service provider. Passes by the [IMTConKYC::EnProviderType (#enprovidertype)](IMTCon-Enumerations.md#enprovidertype) enumeration value.

# IMTConKYC::Mode

Set the KYC service provider in the configuration.

C++
    
    
    MTAPIRES  IMTConKYC::ProviderType(
       const UINT      provider  // Provider
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.ProviderType(
       EnProviderType  provider  // Provider
       )

### Parameters

**provider**  
[in] KYC service provider. Passes by theIMTConKYC::EnProviderTypeenumeration value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
