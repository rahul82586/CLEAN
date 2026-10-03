[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ConditionAdd

[Previous](EventRepeats.md) | [Next](ConditionUpdate.md)

# IMTConAutomation::ConditionAdd

Add an automation task triggering [condition](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition).

C++
    
    
    MTAPIRES  IMTConAutomation::ConditionAdd(
       IMTConAutoCondition*  condition      // Condition object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ConditionAdd(
       CIMTConAutoCondition  condition      // Condition object
       )

Python
    
    
    MTConAutomation.ConditionAdd(
       condition             # Condition object
       )

### Parameters

**condition**  
[in]IMTConAutoConditioncondition object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
