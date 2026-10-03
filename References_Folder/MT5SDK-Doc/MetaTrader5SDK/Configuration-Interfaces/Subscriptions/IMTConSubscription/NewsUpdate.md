[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / NewsUpdate

[Previous](NewsAdd.md) | [Next](NewsDelete.md)

# IMTConSubscription::NewsUpdate

Edit a news category in the news list available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::NewsUpdate(
       const UINT                       pos,       // News configuration position
       const IMTConSubscriptionNews*    news       // News configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.NewsUpdate(
       uint                             pos,       // News configuration position
       CIMTConSubscriptionSymbol        news       // News configuration object
       )

### Parameters

**pos**  
[in] Position of a news setting in the list, starting with 0.

**news**  
[in] News configuration objectIMTConSubscriptionNews.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
