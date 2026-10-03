[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionNews](../IMTConSubscriptionNews.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConSubscriptionNews::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConSubscriptionNews::Assign(
       const IMTConSubscriptionNews*  news  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscriptionNews.Assign(
       CIMTConSubscriptionNews        news  // Source object
       )

### Parameters

**news**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
