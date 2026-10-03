[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / NewsAdd

[Previous](SymbolNext.md) | [Next](NewsUpdate.md)

# IMTConSubscription::NewsAdd

Add a news category to the news list available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::NewsAdd(
       IMTConSubscriptionNews*    news    // News setting object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.NewsAdd(
       CIMTConSubscriptionNews    news    // News setting object
       )

### Parameters

**news**  
[in] News setting objectIMTConAutoCondition.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
