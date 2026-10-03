[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ConditionDelete

[Previous](ConditionUpdate.md) | [Next](ConditionClear.md)

# IMTConRoute::ConditionDelete

Delete an additional condition to apply a rule at the specified position.

C++
    
    
    MTAPIRES  IMTConRoute::ConditionDelete(
       const UINT  pos      // Position of a condition
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ConditionDelete(
       uint        pos      // Position of a condition
       )

Python (Manager API)
    
    
    MTConRoute.ConditionDelete(
       pos         # Position of a condition
       )

### Parameters

**pos**  
[in] Position of an additional condition in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
