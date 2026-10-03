[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerTemplate](../IMTConMessengerTemplate.md) / Clear

[Previous](Assign.md) | [Next](Type.md)

# IMTConMessengerTemplate::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConMessengerTemplate::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerTemplate.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.

### Note

This method completely clears field values ​and deletes nested objects.
