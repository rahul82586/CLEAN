[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / Rule

[Previous](Condition.md) | [Next](OrId.md)

# IMTConAutoCondition::Rule

Get a method for comparing a condition with the specified value.

C++
    
    
    UINT  IMTConAutoCondition::Rule()  const

.NET (Gateway/Manager API)
    
    
    EnConditionRule  CIMTConAutoCondition.Rule()

Python
    
    
    MTConAutoCondition.Rule

### Return Value

[IMTConAutoCondition::EnConditionRule (#enconditionrule)](Enumerations.md#enconditionrule) enumeration value.

# IMTConAutoCondition::Rule

Set a method for comparing a condition with the specified value.

C++
    
    
    MTAPIRES  IMTConAutoCondition::Rule(
       const UINT       rule  // Comparison method
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.Rule(
       EnConditionRule  rule  // Comparison method
       )

Python
    
    
    MTConAutoCondition.Rule

### Parameters

**rule**  
[in] A method for comparing a condition with the specified value. The value is passed using theIMTConAutoCondition::EnConditionRuleenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
