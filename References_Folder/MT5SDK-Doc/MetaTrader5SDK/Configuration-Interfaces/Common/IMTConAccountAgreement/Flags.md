[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAgreement](../IMTConAccountAgreement.md) / Flags

[Previous](URL.md) | [Next](../IMTConSink.md)

# IMTConAccountAgreement::Flags

Get additional agreement settings.

C++
    
    
    UINT  IMTConAccountAgreement::Flags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAccountAgreement.Flags()

### Return Value

[IMTConAccountAgreement::EnFlags (#enflags)](Enumerations.md#enflags) enumeration value.

# IMTConAccountAgreement::Flags

Set additional agreement settings.

C++
    
    
    MTAPIRES  IMTConAccountAgreement::Flags(
       const UINT  flags     // Agreement settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAgreement.Flags(
       uint        flags     // Agreement settings
       )

### Parameters

**flags**  
[in] Agreement settings are passed using theIMTConAccountAgreement::EnFlagsenumeration.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
