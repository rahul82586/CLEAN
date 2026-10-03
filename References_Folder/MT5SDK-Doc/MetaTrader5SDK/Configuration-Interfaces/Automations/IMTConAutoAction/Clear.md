[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / Clear

[Previous](Assign.md) | [Next](Action.md)

# IMTConAutoAction::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConAutoAction::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.Clear()

Python
    
    
    MTConAutoAction.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
