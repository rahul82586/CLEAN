[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / ProviderSubId

[Previous](ProviderToken.md) | [Next](ProviderCurrency.md)

# IMTConMessenger::ProviderSubId

Get the sender identifier, which is used for sending messages via the messenger.

C++
    
    
    LPCWSTR  IMTConMessenger::ProviderSubId()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.ProviderSubId()

Python
    
    
    MTConMessenger.ProviderSubId

### Return Value

If successful, the method returns a pointer to the string with the identifier. Otherwise, NULL is returned.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.

# IMTConMessenger::ProviderSubId

Set the sender identifier, which is used for sending messages via the messenger.

C++
    
    
    MTAPIRES  IMTConMessenger::ProviderSubId(
       LPCWSTR  subid     // Sender ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.ProviderSubId(
       srting   subid     // Sender ID
       )

Python
    
    
    MTConMessenger.ProviderSubId

### Parameters

**subid**  
[in] The sender identifier, which is used for sending messages via the messenger.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The availability (the need to fill) of this parameter depends on the selected messaging service provider ([IMTConMessenger::ProviderType](ProviderType.md)). Please contact the provider for details.
