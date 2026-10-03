[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / Record

[Previous](Subscription.md) | [Next](Action.md)

# IMTSubscriptionHistory::Record

Get the identifier of the subscription with which the action is performed.

C++
    
    
    UINT64  IMTSubscriptionHistory::Record()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSubscriptionHistory.Record()

### Return Value

Subscription identifier ([IMTSubscription::ID](../IMTSubscription/ID.md)).

# IMTSubscriptionHistory::Record

Set the identifier of the subscription with which the action is performed.

C++
    
    
    MTAPIRES  IMTSubscriptionHistory::Record(
       const UINT64  record_id  // ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistory.Record(
       ulong         record_id  // ID
       )

### Parameters

**record_id**  
[in] Subscription identifier (IMTSubscription::ID).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
