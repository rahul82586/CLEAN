[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / TemplateDelete

[Previous](TemplateUpdate.md) | [Next](TemplateClear.md)

# IMTConMessenger::TemplateDelete

Delete the group of accounts for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::TemplateDelete(
       const UINT  pos      // template position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.TemplateDelete(
       uint        pos      // template position
       )

Python
    
    
    MTConMessenger.TemplateDelete(
       pos         # template position
       )

### Parameters

**pos**  
[in] The position of the template in the list, starting from 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.
