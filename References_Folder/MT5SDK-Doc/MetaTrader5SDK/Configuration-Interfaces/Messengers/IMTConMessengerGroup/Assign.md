[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerGroup](../IMTConMessengerGroup.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConMessengerGroup::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConMessengerGroup::Assign(
       const IMTConMessengerGroup*  group  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerGroup.Assign(
       CIMTConMessengerGroup        group  // Source object
       )

### Parameters

**group**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
