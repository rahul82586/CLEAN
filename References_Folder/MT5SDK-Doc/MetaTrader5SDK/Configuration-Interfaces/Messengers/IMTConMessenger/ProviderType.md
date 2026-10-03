[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / ProviderType

[Previous](Sender.md) | [Next](ProviderAddress.md)

# IMTConMessenger::ProviderType

Get the messaging service provider in the messenger configuration.

C++
    
    
    UINT  IMTConMessenger::ProviderType()  const

.NET (Gateway/Manager API)
    
    
    EnProviderType  CIMTConMessenger.ProviderType()

Python
    
    
    MTConMessenger.ProviderType

### Return Value

messaging provider. Passed as a value of the [IMTConMessenger::EnProviderType (#enprovidertype)](Enumerations.md#enprovidertype) enumeration.

# IMTConMessenger::Mode

Set the messaging service provider in the messenger configuration.

C++
    
    
    MTAPIRES  IMTConMessenger::ProviderType(
       const UINT      provider  // Provider
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.ProviderType(
       EnProviderType  provider  // Provider
       )

Python
    
    
    MTConMessenger.ProviderType

### Parameters

**provider**  
[in] Messaging service provider. Passed as a value of theIMTConMessenger::EnProviderTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
