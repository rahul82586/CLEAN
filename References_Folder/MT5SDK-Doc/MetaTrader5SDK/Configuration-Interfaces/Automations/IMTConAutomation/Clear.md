[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / Clear

[Previous](Assign.md) | [Next](ID.md)

# IMTConAutomation::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConAutomation::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
