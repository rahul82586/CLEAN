[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ConditionClear

[Previous](ConditionDelete.md) | [Next](ConditionShift.md)

# IMTConRoute::ConditionClear

Clear the list of all additional conditions to apply a rule.

C++
    
    
    MTAPIRES  IMTConRoute::ConditionClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ConditionClear()

Python (Manager API)
    
    
    MTConRoute.ConditionClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all an additional conditions to apply a rule.
