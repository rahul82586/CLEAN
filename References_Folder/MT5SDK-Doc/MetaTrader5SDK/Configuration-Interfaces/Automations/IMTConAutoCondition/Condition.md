[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / Condition

[Previous](Clear.md) | [Next](Rule.md)

# IMTConAutoCondition::Condition

Get automation task triggering [condition type](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition).

C++
    
    
    UINT  IMTConAutoCondition::Condition()  const

.NET (Gateway/Manager API)
    
    
    EnConditions  CIMTConAutoCondition.Condition()

Python
    
    
    MTConAutoCondition.Condition

### Return Value

[IMTConAutoCondition::EnConditions (#enconditions)](Enumerations.md#enconditions) enumeration value.

# IMTConAutoCondition::Condition

Set automation task triggering [condition type](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition).

C++
    
    
    MTAPIRES  IMTConAutoCondition::Condition(
       const UINT        condition  // Condition type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.Condition(
       EnConditions      condition  // Condition type
       )

Python
    
    
    MTConAutoCondition.Condition

### Parameters

**condition**  
[in] Type of condition for automation task triggering. The value is passed using theIMTConAutoCondition::EnConditionsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
