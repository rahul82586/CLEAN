[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ConditionClear

[Previous](ConditionDelete.md) | [Next](ConditionShift.md)

# IMTConAutomation::ConditionClear

Clear the list of all automation task triggering [conditions](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition).

C++
    
    
    MTAPIRES  IMTConAutomation::ConditionClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ConditionClear()

Python
    
    
    MTConAutomation.ConditionClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method deletes all trigger conditions of an automation task.
