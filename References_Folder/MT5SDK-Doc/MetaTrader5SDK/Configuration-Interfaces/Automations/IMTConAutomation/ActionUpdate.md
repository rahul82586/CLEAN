[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ActionUpdate

[Previous](ActionAdd.md) | [Next](ActionDelete.md)

# IMTConAutomation::ActionUpdate

Edit an automation task [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) at the specified position.

C++
    
    
    MTAPIRES  IMTConAutomation::ActionUpdate(
       const UINT                  pos,       // Action position
       const IMTConAutoAction*     action     // Action object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ActionUpdate(
       uint                        pos,       // Action position
       CIMTConAutoAction           action     // Action object
       )

Python
    
    
    MTConAutomation.ActionUpdate(
       pos,                        # Action position
       action                      # Action object
       )
    
    
    MTConAutomation.ActionSet(
       action_list                 # List of actions
       )

### Parameters

**pos**  
[in] Action position in the list starting at 0.

**action**  
[in]IMTConAutoActionaction object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
