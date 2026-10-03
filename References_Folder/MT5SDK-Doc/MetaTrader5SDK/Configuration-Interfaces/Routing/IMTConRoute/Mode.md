[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / Mode

[Previous](Name.md) | [Next](Request.md)

# IMTConRoute::Mode

Get the state of the routing rule.

C++
    
    
    UINT  IMTConRoute::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnRouteMode  CIMTConRoute.Mode()

Python (Manager API)
    
    
    MTConRoute.Mode

### Return Value

A value of the [IMTConRoute::EnRouteMode (#enroutemode)](Enumerations.md#enroutemode) enumeration.

# IMTConRoute::Mode

Set the state of the routing rule.

C++
    
    
    MTAPIRES  IMTConRoute::Mode(
       const UINT   mode     // State of a rule
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.Mode(
       EnRouteMode  mode     // State of a rule
       )

Python (Manager API)
    
    
    MTConRoute.Mode

### Parameters

**mode**  
[in] The state of a routing rule. To pass the state, theIMTConRoute::EnRouteModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
