[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / CountryShift

[Previous](CountryClear.md) | [Next](CountryTotal.md)

# IMTConSubscription::CountryShift

Shift a country for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::CountryShift(
       const UINT  pos,       // Country position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.CountryShift(
       uint        pos,       // Country position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] The position of a country in the list, starting at 0.

**shift**  
[in] The shift of the country relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
