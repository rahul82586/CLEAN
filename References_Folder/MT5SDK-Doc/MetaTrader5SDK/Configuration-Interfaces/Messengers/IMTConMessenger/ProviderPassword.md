[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / ProviderPassword

[Previous](ProviderLogin.md) | [Next](ProviderToken.md)

# IMTConMessenger::ProviderPassword

Get the password of the account which is used for sending messages via the messenger.

C++
    
    
    LPCWSTR  IMTConMessenger::ProviderPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.ProviderPassword()

Python
    
    
    MTConMessenger.ProviderPassword

### Return Value

If successful, the method returns a pointer to a string with the password. Otherwise, NULL is returned.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.

# IMTConMessenger::ProviderPassword

Set the password of the account which is used for sending messages via the messenger.

C++
    
    
    MTAPIRES  IMTConMessenger::ProviderPassword(
       LPCWSTR  password  // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.ProviderPassword(
       srting   password  // Password
       )

Python
    
    
    MTConMessenger.ProviderPassword

### Parameters

**password**  
[in] The password of the account which is used for sending messages via the messenger.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.
