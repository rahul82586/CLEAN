[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / CountryClear

[Previous](CountryDelete.md) | [Next](CountryShift.md)

# IMTConSubscription::CountryClear

Clear the list of countries for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::CountryClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.CountryClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method deletes all countries from the list.
