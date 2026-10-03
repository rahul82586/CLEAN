[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / CountryNext

[Previous](CountryTotal.md) | [Next](GroupAdd.md)

# IMTConSubscription::CountryNext

Get a country, for which the subscription is available, by index.

C++
    
    
    LPCWSTR  IMTConSubscription::CountryNext(
       const UINT   pos   // Country position
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.CountryNext(
       uint         pos,  // Country position
       )

### Parameters

**pos**  
[in] The position of a country in the list.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
