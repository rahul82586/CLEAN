[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ConditionDelete

[Previous](ConditionUpdate.md) | [Next](ConditionClear.md)

# IMTConAutomation::ConditionDelete

Delete an automation task triggering [condition](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition) at the specified position.

C++
    
    
    MTAPIRES  IMTConAutomation::ConditionDelete(
       const UINT  pos      // Condition position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ConditionDelete(
       uint        pos      // Condition position
       )

Python
    
    
    MTConAutomation.ConditionDelete(
       pos         # Condition position
       )

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
