[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / CountryDelete

[Previous](CountryUpdate.md) | [Next](CountryClear.md)

# IMTConSubscription::CountryDelete

Delete a country for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::CountryDelete(
       const UINT  pos      // Country position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.CountryDelete(
       uint        pos      // Country position
       )

### Parameters

**pos**  
[in] The position of a country in the list, starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
