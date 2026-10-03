[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / TimeExpire

[Previous](TimeRenewal.md) | [Next](../IMTSubscriptionArray.md)

# IMTSubscription::TimeExpire

Get the subscription expiration time.

C++
    
    
    INT64  IMTSubscription::TimeExpire()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTSubscription.TimeExpire()

### Return Value

Subscription expiration time in seconds since 01.01.1970.

# IMTSubscription::TimeExpire

Set the subscription expiration time.

C++
    
    
    MTAPIRES  IMTSubscription::TimeExpire(
       const INT64   time      // Subscription expiration
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.TimeExpire(
       long          time      // Subscription expiration
       )

### Parameters

**time**  
[in]Subscription expiration time in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
