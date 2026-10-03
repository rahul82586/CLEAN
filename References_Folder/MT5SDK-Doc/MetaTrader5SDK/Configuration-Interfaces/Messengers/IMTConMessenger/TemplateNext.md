[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / TemplateNext

[Previous](TemplateTotal.md) | [Next](../IMTConMessengerCountry.md)

# IMTConMessenger::TemplateNext

Get a message template used by the messenger by its index in the list.

C++
    
    
    MTAPIRES  IMTConMessenger::TemplateNext(
       const UINT                pos,    // template position
       IMTConMessengerTemplate*  tpl     // template object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.TemplateNext(
       uint                      pos,    // template position
       CIMTConMessengerTemplate  tpl     // template object
       )

Python
    
    
    MTConMessenger.TemplateNext(
       pos                       # template position
       )
    
    
    MTConMessenger.TemplateGet()

### Parameters

**pos**  
[in] The position of the template in the list, starting from 0.

**tpl**  
[out] Template object. The 'tpl' object must be created in advance using theIMTServerAPI::MessengerGroupCreateorIMTAdminAPI::MessengerGroupCreatemethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.
