[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Flags

[Previous](Status.md) | [Next](TimeSubscribe.md)

# IMTSubscription::Flags

Get additional subscription properties.

C++
    
    
    UINT  IMTSubscription::Flags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTSubscription.Flags()

### Return Value

Additional properties as flags from the [IMTSubscription::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTSubscription::Flags

Set additional subscription properties.

C++
    
    
    MTAPIRES  IMTSubscription::Flags(
       const UINT  flags     // Flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.Flags(
       uint        flags     // Flags
       )

### Parameters

**flags**  
[in] Additional subscription properties as flags from theIMTSubscription::EnStatusenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
