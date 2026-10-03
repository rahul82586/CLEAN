[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / Subscription

[Previous](Login.md) | [Next](Record.md)

# IMTSubscriptionHistory::Subscription

Get the subscription configuration identifier.

C++
    
    
    UINT64  IMTSubscriptionHistory::Subscription()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSubscriptionHistory.Subscription()

### Return Value

Subscription configuration identifier ([IMTConSubscription::ID](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ID.md)).

### Note

This property identifies the service the client is subscribed to.

# IMTSubscriptionHistory::Subscription

Set the subscription configuration identifier.

C++
    
    
    MTAPIRES  IMTSubscriptionHistory::Subscription(
       const UINT64  subscription_id  // ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistory.Subscription(
       ulong         subscription_id  // ID
       )

### Parameters

**subscription_id**  
[in] Subscription configuration identifier (IMTConSubscription::ID).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This property identifies the service the client is subscribed to.
