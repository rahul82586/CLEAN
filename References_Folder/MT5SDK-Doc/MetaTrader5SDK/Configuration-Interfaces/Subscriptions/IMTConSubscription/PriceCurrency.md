[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PriceCurrency

[Previous](PriceCost.md) | [Next](CountryAdd.md)

# IMTConSubscription::PriceCurrency

Get the currency in which the subscription price is specified.

C++
    
    
    LPCWSTR  IMTConSubscription::PriceCurrency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.PriceCurrency()

### Return Value

If successful, the method returns a pointer to a string with the currency name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscription](../IMTConSubscription.md) object.

# IMTConSubscription::PriceCurrency

Set the currency in which the subscription price is specified.

C++
    
    
    MTAPIRES  IMTConSubscription::PriceCurrency(
       LPCWSTR  currency  // Currency name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PriceCurrency(
       srting   currency  // Currency name
       )

### Parameters

**currency**  
[in] Three-letter currency name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The name length is limited to 16 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
