[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Subscription

[Previous](Login.md) | [Next](Status.md)

# IMTSubscription::Subscription

Get the subscription configuration identifier.

C++
    
    
    UINT64  IMTSubscription::Subscription()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSubscription.Subscription()

### Return Value

Subscription configuration identifier ([IMTConSubscription::ID](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ID.md)).

### Note

This property identifies the service the client is subscribed to.

# IMTSubscription::Subscription

Set the subscription configuration identifier.

C++
    
    
    MTAPIRES  IMTSubscription::Subscription(
       const UINT64  subscription_id  // ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.Subscription(
       ulong         subscription_id  // ID
       )

### Parameters

**subscription_id**  
[in] Subscription configuration identifier (IMTConSubscription::ID).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This property identifies the service the client is subscribed to.
