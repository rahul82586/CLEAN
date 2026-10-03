[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ConditionNext

[Previous](ConditionTotal.md) | [Next](ActionAdd.md)

# IMTConAutomation::ConditionNext

Get an automation task triggering [condition](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition) by index.

C++
    
    
    MTAPIRES  IMTConAutomation::ConditionNext(
       const UINT            pos,       // Condition position
       IMTConAutoCondition*  condition  // Condition object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ConditionNext(
       uint                  pos,       // Condition position
       CIMTConCondition      condition  // Condition object
       )

Python
    
    
    MTConAutomation.ConditionNext(
       pos                   # Condition position
       )
    
    
    MTConAutomation.ConditionGet()

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

**condition**  
[out] TheIMTConAutoConditioncondition object. The 'condition' object must be previously created using theIMTServerAPI::AutomationConditionCreateorIMTAdminAPI::AutomationConditionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
