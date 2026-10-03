[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / URLDescription

[Previous](Description.md) | [Next](URLAgreement.md)

# IMTConSubscription::URLDescription

Get a link to an additional subscription description.

C++
    
    
    LPCWSTR  IMTConSubscription::URLDescription()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.URLDescription()

### Return Value

If successful, a pointer to the string with the link is returned. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscription](../IMTConSubscription.md) object.

# IMTConSubscription::URLDescription

Set a link to an additional subscription description.

C++
    
    
    MTAPIRES  IMTConSubscription::URLDescription(
       LPCWSTR  url       // Description link
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.URLDescription(
       srting   url       // Description link
       )

### Parameters

**url**  
[in] Description link.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The link length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
