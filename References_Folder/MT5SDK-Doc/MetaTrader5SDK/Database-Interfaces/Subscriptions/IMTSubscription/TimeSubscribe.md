[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / TimeSubscribe

[Previous](Flags.md) | [Next](TimeRenewal.md)

# IMTSubscription::TimeSubscribe

Get the subscription start time.

C++
    
    
    INT64  IMTSubscription::TimeSubscribe()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTSubscription.TimeSubscribe()

### Return Value

Subscription start time in seconds since 01.01.1970.

# IMTSubscription::TimeSubscribe

Set the subscription start time.

C++
    
    
    MTAPIRES  IMTSubscription::TimeSubscribe(
       const INT64   time      // Subscription start
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.TimeSubscribe(
       long          time      // Subscription start
       )

### Parameters

**time**  
[in]Subscription start time in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
