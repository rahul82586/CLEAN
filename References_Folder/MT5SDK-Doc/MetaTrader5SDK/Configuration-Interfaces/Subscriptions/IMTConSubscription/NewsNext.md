[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / NewsNext

[Previous](NewsTotal.md) | [Next](../IMTConSubscriptionSymbol.md)

# IMTConSubscription::NewsNext

Get a news category available by subscription, by index.

C++
    
    
    MTAPIRES  IMTConSubscription::NewsNext(
       const UINT                 pos,       // News configuration position
       IMTConSubscriptionNews*    news       // News configuration object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.NewsNext(
       uint                       pos,       // News configuration position
       CIMTConSubscriptionNews    news       // News configuration object
       )

### Parameters

**pos**  
[in] Position of a news setting in the list, starting with 0.

**news**  
[out] News setting positionIMTConSubscriptionNews. The 'news' object must be previously created by methodIMTServerAPI::SubscriptionCfgNewsCreate,IMTManagerAPI::SubscriptionCfgNewsCreateorIMTAdminAPI::SubscriptionCfgNewsCreate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
