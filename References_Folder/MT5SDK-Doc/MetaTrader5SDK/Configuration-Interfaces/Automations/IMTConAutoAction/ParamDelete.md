[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / ParamDelete

[Previous](ParamUpdate.md) | [Next](ParamClear.md)

# IMTConAutoAction::ParamDelete

Delete a parameter from an automation task action.

C++
    
    
    MTAPIRES  IMTConAutoAction::ParamDelete(
       const UINT  pos      // Parameter position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.ParamDelete(
       uint        pos      // Parameter position
       )

Python
    
    
    MTConAutoAction.ParamDelete(
       pos         # Parameter position
       )

### Parameters

**pos**  
[in] The position of the parameter in the list starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
