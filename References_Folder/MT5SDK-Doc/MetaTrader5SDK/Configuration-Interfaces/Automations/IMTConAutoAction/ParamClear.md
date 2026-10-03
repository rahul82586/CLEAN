[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / ParamClear

[Previous](ParamDelete.md) | [Next](ParamShift.md)

# IMTConAutoAction::ParamClear

Clear the list of all parameters for an automation task action.

C++
    
    
    MTAPIRES  IMTConAutoAction::ParamClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.ParamClear()

Python
    
    
    MTConAutoAction.ParamClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all parameters from the automation task action.
