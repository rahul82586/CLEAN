[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Type

[Previous](Name.md) | [Next](Image.md)

# IMTConSubscription::Type

Get a subscription configuration type.

C++
    
    
    UINT  IMTConSubscription::Type()  const

.NET (Gateway/Manager API)
    
    
    EnType  CIMTConSubscription.Type()

### Return Value

Subscription configuration type. The type is passed as a value of the [IMTConSubscription::EnType (#entype)](Enumerations.md#entype) enumeration.

# IMTConSubscription::Type

Set a subscription configuration type.

C++
    
    
    MTAPIRES  IMTConSubscription::Type(
       const UINT      type     // Type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Type(
       EnType          type     // Type
       )

### Parameters

**type**  
[in] Subscription configuration type. The type is passed as a value of theIMTConSubscription::EnTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
