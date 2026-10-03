[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTSubscriptionHistory::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTSubscriptionHistory::Assign(
       const IMTSubscription*  obj // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistory.Assign(
       CIMTSubscriptionHistory        obj // Source object
       )

### Parameters

**obj**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
