[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ActionAdd

[Previous](ConditionNext.md) | [Next](ActionUpdate.md)

# IMTConAutomation::ActionAdd

Add an automation task [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action).

C++
    
    
    MTAPIRES  IMTConAutomation::ActionAdd(
       IMTConAutoAction*  action      // Action object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ActionAdd(
       CIMTConAutoAction  action      // Action object
       )

Python
    
    
    MTConAutomation.ActionAdd(
       action             # Action object
       )

### Parameters

**action**  
[in]IMTConAutoActionaction object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
