[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ActionClear

[Previous](ActionDelete.md) | [Next](ActionShift.md)

# IMTConAutomation::ActionClear

Clear the list of all automation task [actions](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action).

C++
    
    
    MTAPIRES  IMTConAutomation::ActionClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ActionClear()

Python
    
    
    MTConAutomation.ActionClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method deletes all actions of an automation task.
