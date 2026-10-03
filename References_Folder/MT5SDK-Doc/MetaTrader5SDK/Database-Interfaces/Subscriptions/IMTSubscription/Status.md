[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Status

[Previous](Subscription.md) | [Next](Flags.md)

# IMTSubscription::Status

Get the subscription status.

C++
    
    
    UINT  IMTSubscription::Status()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTSubscription.Status()

### Return Value

[IMTSubscription::EnStatus (#enstatus)](Enumerations.md#enstatus) enumeration values.

# IMTSubscription::Status

Set the subscription status.

C++
    
    
    MTAPIRES  IMTSubscription::Status(
       const UINT  state     // Subscription status
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.Status(
       uint        state     // Subscription status
       )

### Parameters

**state**  
[in] Subscription status. To pass the status, use theIMTSubscription::EnStatusenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
