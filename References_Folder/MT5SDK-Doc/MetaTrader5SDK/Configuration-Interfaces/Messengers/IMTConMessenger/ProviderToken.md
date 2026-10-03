[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / ProviderToken

[Previous](ProviderPassword.md) | [Next](ProviderSubId.md)

# IMTConMessenger::ProviderToken

Get the authentication token, which is used for sending messages via the messenger.

C++
    
    
    LPCWSTR  IMTConMessenger::ProviderToken()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.ProviderToken()

Python
    
    
    MTConMessenger.ProviderToken

### Return Value

If successful, the method returns a pointer to a string with the token. Otherwise, NULL is returned.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.

# IMTConMessenger::ProviderToken

Set the authentication token, which is used for sending messages via the messenger.

C++
    
    
    MTAPIRES  IMTConMessenger::ProviderToken(
       LPCWSTR  token     // Authentication token
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.ProviderToken(
       srting   token     // Authentication token
       )

Python
    
    
    MTConMessenger.ProviderToken

### Parameters

**token**  
[in] The authentication token, which is used for sending messages via the messenger.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.
