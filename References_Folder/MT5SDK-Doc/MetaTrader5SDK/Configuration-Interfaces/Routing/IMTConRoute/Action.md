[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / Action

[Previous](Type.md) | [Next](ParamType.md)

# IMTConRoute::Action

Get the action that is applied to a request in accordance with a rule.

C++
    
    
    UINT  IMTConRoute::Action()  const

.NET (Gateway/Manager API)
    
    
    EnRouteAction  CIMTConRoute.Action()

Python (Manager API)
    
    
    MTConRoute.Action

### Return Value

A value of the [IMTConRoute::EnRouteAction (#enrouteaction)](Enumerations.md#enrouteaction) enumeration.

# IMTConRoute::Action

Set the action that is applied to a request in accordance with a rule.

C++
    
    
    MTAPIRES  IMTConRoute::Action(
       const UINT     action   // Type of action
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.Action(
       EnRouteAction  action   // Type of action
       )

Python (Manager API)
    
    
    MTConRoute.Action

### Parameters

**action**  
[in] The type of action that is applied to a request in accordance with a rule. To pass the type, theIMTConRoute::EnRouteActionenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
