[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / GroupUpdate

[Previous](GroupAdd.md) | [Next](GroupDelete.md)

# IMTConSubscription::GroupUpdate

Change a group for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::GroupUpdate(
       const UINT   pos,  // Group position
       LPCWSTR      path  // Group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.GroupUpdate(
       uint         pos,  // Group position
       string       path  // Group
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**path**  
[in] New path to group or subgroup. For example, real\stocks or real\*.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
