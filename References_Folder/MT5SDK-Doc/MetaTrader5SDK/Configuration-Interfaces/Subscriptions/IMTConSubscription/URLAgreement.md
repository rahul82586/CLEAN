[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / URLAgreement

[Previous](URLDescription.md) | [Next](ControlMode.md)

# IMTConSubscription::URLAgreement

Get a link to a subscription agreement.

C++
    
    
    LPCWSTR  IMTConSubscription::URLAgreement()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.URLAgreement()

### Return Value

If successful, a pointer to the string with the link is returned. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscription](../IMTConSubscription.md) object.

# IMTConSubscription::URLAgreement

Set a link to a subscription agreement.

C++
    
    
    MTAPIRES  IMTConSubscription::URLAgreement(
       LPCWSTR  url       // Agreement link
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.URLAgreement(
       srting   url       // Agreement link
       )

### Parameters

**url**  
[in] Agreement link.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The link length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
