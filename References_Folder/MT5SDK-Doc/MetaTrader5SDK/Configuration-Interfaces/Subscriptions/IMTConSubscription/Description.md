[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Description

[Previous](Image.md) | [Next](URLDescription.md)

# IMTConSubscription::Description

Get a subscription description.

C++
    
    
    LPCWSTR  IMTConSubscription::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.Description()

### Return Value

If successful, it returns a pointer to the string with the description. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscription](../IMTConSubscription.md) object.

# IMTConSubscription::Description

Set a subscription description.

C++
    
    
    MTAPIRES  IMTConSubscription::Description(
       LPCWSTR  description  // Description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Description(
       srting   description  // Description
       )

### Parameters

**description**  
[in] Subscription description.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The length of the description is not limited.
