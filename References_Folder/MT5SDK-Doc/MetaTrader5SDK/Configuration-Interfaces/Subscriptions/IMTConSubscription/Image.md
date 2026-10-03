[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Image

[Previous](Type.md) | [Next](Description.md)

# IMTConSubscription::Image

Get a subscription logo.

C++
    
    
    UINT  IMTConSubscription::Image()  const

.NET (Gateway/Manager API)
    
    
    EnImageType  CIMTConSubscription.Image()

### Return Value

Subscription logo. The logo is passed as a value of the [IMTConSubscription::EnImageType (#enimagetype)](Enumerations.md#enimagetype) enumeration.

# IMTConSubscription::Image

Set a subscription logo.

C++
    
    
    MTAPIRES  IMTConSubscription::Image(
       const UINT      image    // Logo
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Image(
       EnImageType     image    // Logo
       )

### Parameters

**image**  
[in] Subscription configuration type. The logo is passed as a value of theIMTConSubscription::EnImageTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
