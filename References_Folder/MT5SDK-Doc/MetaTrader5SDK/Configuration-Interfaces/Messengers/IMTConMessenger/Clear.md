[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConMessenger::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConMessenger::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
