[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerGroup](../IMTConMessengerGroup.md) / Clear

[Previous](Assign.md) | [Next](Group.md)

# IMTConMessengerGroup::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConMessengerGroup::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerGroup.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
