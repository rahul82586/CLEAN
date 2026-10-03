[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / CountryAdd

[Previous](PriceCurrency.md) | [Next](CountryUpdate.md)

# IMTConSubscription::CountryAdd

Add a country for which the subscription will be available.

C++
    
    
    MTAPIRES  IMTConSubscription::CountryAdd(
       LPCWSTR  path      // Country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.CountryAdd(
       string   path      // Country
       )

### Parameters

**path**  
[in] Country name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
