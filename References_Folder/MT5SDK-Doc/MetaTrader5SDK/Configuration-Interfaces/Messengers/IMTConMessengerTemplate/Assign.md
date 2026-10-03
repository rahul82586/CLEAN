[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerTemplate](../IMTConMessengerTemplate.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConMessengerTemplate::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConMessengerTemplate::Assign(
       const IMTConMessengerTemplate*  tpl  // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerGroup.Assign(
       CIMTConMessengerTemplate        tpl  // source object
       )

### Parameters

**group**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.
