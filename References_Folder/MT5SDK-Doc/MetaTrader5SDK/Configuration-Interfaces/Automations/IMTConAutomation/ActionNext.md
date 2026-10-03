[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ActionNext

[Previous](ActionTotal.md) | [Next](../IMTConAutoCondition.md)

# IMTConAutomation::ActionNext

Get an automation task [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) by index.

C++
    
    
    MTAPIRES  IMTConAutomation::ActionNext(
       const UINT            pos,       // Action position
       IMTConAutoAction*     action     // Action object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ActionNext(
       uint                  pos,       // Action position
       CIMTConAutoAction     action     // Action object
       )

Python
    
    
    MTConAutomation.ActionNext(
       pos                   # Action position
       )
    
    
    MTConAutomation.ActionGet()

### Parameters

**pos**  
[in] Action position in the list starting at 0.

**action**  
[out]IMTConAutoActionaction object. The 'action' object must be previously created using theIMTServerAPI::AutomationActionCreateorIMTAdminAPI::AutomationActionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
