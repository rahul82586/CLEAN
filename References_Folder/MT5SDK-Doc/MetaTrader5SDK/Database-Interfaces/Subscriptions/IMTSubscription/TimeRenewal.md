[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / TimeRenewal

[Previous](TimeSubscribe.md) | [Next](TimeExpire.md)

# IMTSubscription::TimeRenewal

Get the last subscription renewal time.

C++
    
    
    INT64  IMTSubscription::TimeRenewal()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTSubscription.TimeRenewal()

### Return Value

The last subscription renewal time in seconds since 01.01.1970.

# IMTSubscription::TimeRenewal

Set the last subscription renewal time.

C++
    
    
    MTAPIRES  IMTSubscription::TimeRenewal(
       const INT64   time      // Last subscription renewal
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.TimeRenewal(
       long          time      // Last subscription renewal
       )

### Parameters

**time**  
[in]The last subscription renewal time in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
