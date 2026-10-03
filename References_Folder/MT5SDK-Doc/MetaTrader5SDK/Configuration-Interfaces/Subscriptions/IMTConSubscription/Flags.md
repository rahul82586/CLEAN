[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Flags

[Previous](PeriodFreeCustom.md) | [Next](Price.md)

# IMTConSubscription::Flags

Get additional subscription settings.

C++
    
    
    UINT  IMTConSubscription::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnProviderType  CIMTConSubscription.Flags()

### Return Value

Additional subscription settings. The settings are passed by the [IMTConSubscription::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTConSubscription::Flags

Set additional subscription settings.

C++
    
    
    MTAPIRES  IMTConSubscription::Flags(
       const UINT      flags    // Settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Flags(
       EnFlags         flags    // Settings
       )

### Parameters

**flags**  
[in] Additional subscription settings. The settings are passed by theIMTConSubscription::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
