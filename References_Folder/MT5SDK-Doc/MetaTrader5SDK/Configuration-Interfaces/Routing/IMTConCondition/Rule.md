[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / Rule

[Previous](Condition.md) | [Next](ValueType.md)

# IMTConCondition::Rule

Get a method for comparing a condition with the specified value.

C++
    
    
    UINT  IMTConCondition::Rule()  const

.NET (Gateway/Manager API)
    
    
    EnConditionRule  CIMTConCondition.Rule()

Python (Manager API)
    
    
    MTConCondition.Rule

### Return Value

A value of the [IMTConCondition::EnConditionRule (#enconditionrule)](Enumerations.md#enconditionrule) enumeration.

# IMTConCondition::Rule

Set a method for comparing a condition with the specified value.

C++
    
    
    MTAPIRES  IMTConCondition::Rule(
       const UINT       rule  // A method for comparison
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.Rule(
       EnConditionRule  rule  // A method for comparison
       )

Python (Manager API)
    
    
    MTConCondition.Rule

### Parameters

**rule**  
[in] A method for comparing a condition with the specified value. To pass the method, theIMTConCondition::EnConditionRuleenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
