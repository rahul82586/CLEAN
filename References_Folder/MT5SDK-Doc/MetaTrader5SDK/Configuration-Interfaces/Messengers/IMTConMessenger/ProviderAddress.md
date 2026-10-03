[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / ProviderAddress

[Previous](ProviderType.md) | [Next](ProviderLogin.md)

# IMTConMessenger::ProviderAddress

Get the messaging service provider's server address from a messenger configuration.

C++
    
    
    LPCWSTR  IMTConMessenger::ProviderAddress()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.ProviderAddress()

Python
    
    
    MTConMessenger.ProviderAddress

### Return Value

If successful, it returns a pointer to a string with the server address. Otherwise, NULL is returned.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.

# IMTConMessenger::ProviderAddress

Set the messaging service provider's server address in a messenger configuration.

C++
    
    
    MTAPIRES  IMTConMessenger::ProviderAddress(
       LPCWSTR  address   // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.ProviderAddress(
       srting   address   // Server address
       )

Python
    
    
    MTConMessenger.ProviderAddress

### Parameters

**name**  
[in] Provider's server address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.
