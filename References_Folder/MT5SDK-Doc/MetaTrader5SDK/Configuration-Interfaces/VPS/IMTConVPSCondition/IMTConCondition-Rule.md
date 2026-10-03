[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition Rule

[Previous](IMTConCondition-Condition.md) | [Next](IMTConCondition-ValueType.md)

# IMTConVPSCondition::Rule

Get a method for comparing a condition with the specified value.

C++
    
    
    UINT  IMTConVPSCondition::Rule()  const

.NET (Gateway/Manager API)
    
    
    EnConditionRule  CIMTConVPSCondition.Rule()

Python
    
    
    MTConVPSCondition.Rule

### Return Value

[IMTConVPSCondition::EnConditionRule (#enconditionrule)](IMTConCondition-Enumerations.md#enconditionrule) enumeration value.

# IMTConVPSCondition::Rule

Set a method for comparing a condition with the specified value.

C++
    
    
    MTAPIRES  IMTConVPSCondition::Rule(
       const UINT       rule  // Comparison method
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.Rule(
       EnConditionRule  rule  // Comparison method
       )

Python
    
    
    MTConVPSCondition.Rule

### Parameters

**rule**  
[in] A method for comparing a condition with the specified value. The method is passed using theIMTConVPSCondition::EnConditionRuleenumeration.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
