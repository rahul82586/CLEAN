[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / Flags

[Previous](ProviderCurrencyRate.md) | [Next](MessageTemplate.md)

# IMTConMessenger::Flags

Get additional messenger settings.

C++
    
    
    UINT64  IMTConMessenger::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConMessenger.Flags()

Python
    
    
    MTConMessenger.Flags

### Return Value

Additional settings as the values of the [IMTConMessenger::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTConMessenger::Flags

Set additional messenger settings.

C++
    
    
    MTAPIRES  IMTConMessenger::Flags(
       const UINT64  flags   // Messenger settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Flags(
       EnFlags       flags   // Messenger settings
       )

Python
    
    
    MTConMessenger.Flags

### Parameters

**flags**  
[in] Additional settings as the values of theIMTConMessenger::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
