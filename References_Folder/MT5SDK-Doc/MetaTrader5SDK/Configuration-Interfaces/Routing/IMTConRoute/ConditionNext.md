[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ConditionNext

[Previous](ConditionTotal.md) | [Next](DealerAdd.md)

# IMTConRoute::ConditionNext

Get an additional condition to apply a rule by its index.

C++
    
    
    MTAPIRES  IMTConRoute::ConditionNext(
       const UINT        pos,           // Condition position
       IMTConCondition*  condition      // An object of the additional condition
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ConditionNext(
       uint              pos,           // Condition position
       CIMTConCondition  condition      // An object of the additional condition
       )

Python (Manager API)
    
    
    MTConRoute.ConditionNext(
       pos               # Condition position
       )
    
    
    MTConRoute.ConditionGet()

### Parameters

**pos**  
[in] Position of an additional condition in the list, starting with 0.

**condition**  
[out] An object of the additional condition. The condition object must be first created using theIMTAdminAPI::RouteConditionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
