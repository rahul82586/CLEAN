[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / GroupDelete

[Previous](GroupUpdate.md) | [Next](GroupClear.md)

# IMTConSubscription::GroupDelete

Delete a group for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::GroupDelete(
       const UINT  pos      // Group position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.GroupDelete(
       uint        pos      // Group position
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
