[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition Condition

[Previous](IMTConCondition-Clear.md) | [Next](IMTConCondition-Rule.md)

# IMTConVPSCondition::Condition

Get the condition type in the VPS allocation rule.

C++
    
    
    UINT  IMTConVPSCondition::Condition()  const

.NET (Gateway/Manager API)
    
    
    EnConditions  CIMTConVPSCondition.Condition()

Python
    
    
    MTConVPSCondition.Condition

### Return Value

[IMTConVPSCondition::EnCondition (#encondition)](IMTConCondition-Enumerations.md#encondition) enumeration value.

# IMTConVPSCondition::Condition

Set the condition type in the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSCondition::Condition(
       const UINT        condition  // Condition type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.Condition(
       EnConditions      condition  // Condition type
       )

Python
    
    
    MTConVPSCondition.Condition

### Parameters

**condition**  
[in] Condition type in the VPS allocation rule. The type is passed using theIMTConVPSCondition::EnConditionenumeration.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
