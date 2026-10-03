[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionNews](../IMTConSubscriptionNews.md) / Language

[Previous](Category.md) | [Next](../IMTConSubscriptionSink.md)

# IMTConSubscriptionNews::Language

Get the language of news available by subscription.

C++
    
    
    UINT  IMTConSubscriptionNews::Language()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSubscriptionNews.Language()

### Return Value

News language.

# IMTConSubscriptionNews::Language

Set the language of news available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscriptionNews::Language(
       const UINT  language      // News language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscriptionNews.Language(
       uint        language      // News language
       )

### Parameters

**language**  
[in] The language in the LANGID format used inMS Windowssystems (a value from Prim.lang.identifier).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
