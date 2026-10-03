[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ConditionUpdate

[Previous](ConditionAdd.md) | [Next](ConditionDelete.md)

# IMTConAutomation::ConditionUpdate

Edit an automation task triggering [condition](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition) at the specified position.

C++
    
    
    MTAPIRES  IMTConAutomation::ConditionUpdate(
       const UINT                  pos,       // Condition position
       const IMTConAutoCondition*  condition  // Condition object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ConditionUpdate(
       uint                        pos,       // Condition position
       CIMTConAutoCondition        condition  // Condition object
       )

Python
    
    
    MTConAutomation.ConditionUpdate(
       pos,                        # Condition position
       condition                   # Condition object
       )
    
    
    MTConAutomation.ConditionSet(
       condition_list              # List of conditions
       )

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

**condition**  
[in]IMTConAutoConditioncondition object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
