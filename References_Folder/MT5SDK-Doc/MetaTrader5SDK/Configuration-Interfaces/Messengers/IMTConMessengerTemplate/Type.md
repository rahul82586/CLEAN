[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerTemplate](../IMTConMessengerTemplate.md) / Type

[Previous](Clear.md) | [Next](Id.md)

# IMTConMessengerTemplate::Type

Get the template type.

C++
    
    
    uint32_t  IMTConMessengerTemplate::Type()  const

.NET (Gateway/Manager API)
    
    
    EnMessengerTemplateTypes  CIMTConMessengerTemplate.Type()

Python
    
    
    MTConMessengerTemplate.Type

### Return Value

Messaging service provider. Passed by [IMTConMessengerTemplate::EnMessengerTemplateTypes (#enmessengertemplatetypes)](Перечисления.md#enmessengertemplatetypes) enumeration value.

# IMTConMessenger::Type

Set the template type.

C++
    
    
    MTAPIRES  IMTConMessengerTemplate::Type(
       const uint32_t            type  // template type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerTemplate.Type(
       EnMessengerTemplateTypes  type  // template type
       )

Python
    
    
    MTConMessengerTemplate.Type

### Parameters

**type**  
[in] Тип шаблона сообщений. Passed byIMTConMessengerTemplate::EnMessengerTemplateTypesenumeration value.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.
