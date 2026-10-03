[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTSubscription::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTSubscription::Assign(
       const IMTSubscription*  obj // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.Assign(
       CIMTSubscription        obj // Source object
       )

### Parameters

**obj**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
