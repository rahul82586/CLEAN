[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / TemplateAdd

[Previous](GroupNext.md) | [Next](TemplateUpdate.md)

# IMTConMessenger::TemplateAdd

Add a message template that the messenger will use.

C++
    
    
    MTAPIRES  IMTConMessenger::TemplateAdd(
       IMTConMessengerTemplate*  tpl      // template object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.TemplateAdd(
       CIMTConMessengerTemplate  tpl      // template object
       )

Python
    
    
    MTConMessenger.GroupAdd(
       tpl                  # template object
       )

### Parameters

**group**  
[in] Template objectIMTConMessengerTemplate.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.
