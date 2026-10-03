[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / TemplateClear

[Previous](TemplateDelete.md) | [Next](TemplateShift.md)

# IMTConMessenger::TemplateClear

Clear the list of message templates used by the messenger.

C++
    
    
    MTAPIRES  IMTConMessenger::TemplateClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.TemplateClear()

Python
    
    
    MTConMessenger.TemplateClear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.

### Note

This method removes from the list all templates used by the messenger.
