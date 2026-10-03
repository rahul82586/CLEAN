[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / CountryUpdate

[Previous](CountryAdd.md) | [Next](CountryDelete.md)

# IMTConSubscription::CountryUpdate

Change a country for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::CountryUpdate(
       const UINT   pos,  // Country position
       LPCWSTR      path  // Country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.CountryUpdate(
       uint         pos,  // Country position
       string       path  // Country
       )

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

**path**  
[in] The name of the new country.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
