[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ConditionUpdate

[Previous](ConditionAdd.md) | [Next](ConditionDelete.md)

# IMTConRoute::ConditionUpdate

Change an additional condition to apply a rule at the specified position.

C++
    
    
    MTAPIRES  IMTConRoute::ConditionUpdate(
       const UINT              pos,           // Position of a condition
       const IMTConCondition*  condition      // An object of the additional condition
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ConditionUpdate(
       uint                    pos,           // Position of a condition
       CIMTConCondition        condition      // An object of the additional condition
       )

Python (Manager API)
    
    
    MTConRoute.ConditionUpdate(
       pos,                    # Position of a condition
       condition               # An object of the additional condition
       )
    
    
    MTConRoute.ConditionSet(
       condition_list          # A list of additional conditions
       )

### Parameters

**pos**  
[in] Position of an additional condition in the list, starting with 0.

**condition**  
[in] An object of the additional condition.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
