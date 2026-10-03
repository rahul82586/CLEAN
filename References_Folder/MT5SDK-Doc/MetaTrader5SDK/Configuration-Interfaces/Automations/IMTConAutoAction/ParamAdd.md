[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / ParamAdd

[Previous](Name.md) | [Next](ParamUpdate.md)

# IMTConAutoAction::ParamAdd

Add a parameter for an automation task action.

C++
    
    
    MTAPIRES  IMTConAutoAction::ParamAdd(
       IMTConAutoParam*   param      // Action object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.ParamAdd(
       CIMTConAutoParam   param      // Action object
       )

Python
    
    
    MTConAutoAction.ParamAdd(
       param              # Action object
       )

### Parameters

**param**  
[in]IMTConAutoParamparameter object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
