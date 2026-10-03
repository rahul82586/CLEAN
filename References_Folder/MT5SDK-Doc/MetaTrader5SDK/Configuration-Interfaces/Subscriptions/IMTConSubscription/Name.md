[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Name

[Previous](DependsID.md) | [Next](Type.md)

# IMTConSubscription::Name

Get a subscription name.

C++
    
    
    LPCWSTR  IMTConSubscription::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.Name()

### Return Value

If successful, it returns a pointer to a string with the configuration name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscription](../IMTConSubscription.md) object.

# IMTConSubscription::Name

Set a subscription name.

C++
    
    
    MTAPIRES  IMTConSubscription::Name(
       LPCWSTR  name      // Subscription name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Name(
       srting   name      // Subscription name
       )

### Parameters

**name**  
[in] Subscription name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
