[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / ProviderCurrency

[Previous](ProviderSubId.md) | [Next](ProviderCurrencyRate.md)

# IMTConMessenger::ProviderCurrency

Get the currency which is used for service provider pricing.

C++
    
    
    LPCWSTR  IMTConMessenger::ProviderCurrency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.ProviderCurrency()

Python
    
    
    MTConMessenger.ProviderCurrency

### Return Value

If successful, the method returns a pointer to a string with the currency name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConMessenger](../IMTConMessenger.md) object.

# IMTConMessenger::ProviderCurrency

Set the currency for service provider's pricing.

C++
    
    
    MTAPIRES  IMTConMessenger::ProviderCurrency(
       LPCWSTR  currency  // Currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.ProviderCurrency(
       srting   currency  // Currency
       )

Python
    
    
    MTConMessenger.ProviderCurrency

### Parameters

**currency**  
[in] The currency for service provider's pricing.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
