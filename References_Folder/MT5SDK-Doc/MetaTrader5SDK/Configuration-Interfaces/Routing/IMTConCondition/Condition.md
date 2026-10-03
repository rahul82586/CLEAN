[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / Condition

[Previous](Clear.md) | [Next](Rule.md)

# IMTConCondition::Condition

Get the type of an additional condition for a rule.

C++
    
    
    UINT  IMTConCondition::Condition()  const

.NET (Gateway/Manager API)
    
    
    EnRouteCondition  CIMTConCondition.Condition()

Python (Manager API)
    
    
    MTConCondition.Condition

### Return Value

A value of the [IMTConCondition::EnRouteCondition (#enroutecondition)](Enumerations.md#enroutecondition) enumeration.

# IMTConCondition::Condition

Set the type of an additional condition for a rule.

C++
    
    
    MTAPIRES  IMTConCondition::Condition(
       const UINT        condition  // Condition type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.Condition(
       EnRouteCondition  condition  // Condition type
       )

Python (Manager API)
    
    
    MTConCondition.Condition

### Parameters

**condition**  
[in] Type of an additional condition for a rule. To pass the type, theIMTConCondition::EnRouteConditionenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
