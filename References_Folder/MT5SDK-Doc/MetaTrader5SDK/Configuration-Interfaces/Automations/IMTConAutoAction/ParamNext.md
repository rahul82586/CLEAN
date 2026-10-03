[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / ParamNext

[Previous](ParamTotal.md) | [Next](../IMTConAutoParam.md)

# IMTConAutoAction::ParamNext

Get the action parameter by index.

C++
    
    
    MTAPIRES  IMTConAutoAction::ParamNext(
       const UINT            pos,       // Parameter position
       IMTConAutoParam*      param      // Parameter object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.ParamNext(
       uint                  pos,       // Parameter position
       CIMTConAutoParam      param      // Parameter object
       )

Python
    
    
    MTConAutoAction.ParamNext(
       pos                   # Parameter position
       )
    
    
    MTConAutoAction.ParamGet()

### Parameters

**pos**  
[in] The position of the parameter in the list starting at 0.

**param**  
[out]IMTConAutoParamparameter object. The 'param' object must be previously created using theIMTServerAPI::AutomationParamCreateorIMTAdminAPI::AutomationParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
