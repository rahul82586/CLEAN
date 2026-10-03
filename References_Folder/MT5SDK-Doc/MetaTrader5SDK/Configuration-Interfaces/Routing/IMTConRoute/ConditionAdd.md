[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ConditionAdd

[Previous](ParamTime.md) | [Next](ConditionUpdate.md)

# IMTConRoute::ConditionAdd

Add an additional condition to apply a rule.

C++
    
    
    MTAPIRES  IMTConRoute::ConditionAdd(
       IMTConCondition*  condition      // An object of the additional condition
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ConditionAdd(
       CIMTConCondition  condition      // An object of the additional condition
       )

Python (Manager API)
    
    
    MTConRoute.ConditionAdd(
       condition         # An object of the additional condition
       )

### Parameters

**condition**  
[in] An object of the additional condition.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
