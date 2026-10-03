[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / GroupAdd

[Previous](CountryNext.md) | [Next](GroupUpdate.md)

# IMTConSubscription::GroupAdd

Add a group for which the subscription will be available.

C++
    
    
    MTAPIRES  IMTConSubscription::GroupAdd(
       LPCWSTR  path      // Group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.GroupAdd(
       string   path      // Group
       )

### Parameters

**path**  
[in] Path to group or subgroup. For example, real\stocks or real\*.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
