[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / Request

[Previous](Mode.md) | [Next](Type.md)

# IMTConRoute::Request

Get requests for which the rule is applicable.

C++
    
    
    UINT  IMTConRoute::Request()  const

.NET (Gateway/Manager API)
    
    
    EnRouteFlags  CIMTConRoute.Request()

Python (Manager API)
    
    
    MTConRoute.Request

### Return Value

A value of the [IMTConRoute::EnRouteFlags (#enrouteflags)](Enumerations.md#enrouteflags) enumeration.

# IMTConRoute::Request

Set requests for which the rule is applicable.

C++
    
    
    MTAPIRES  IMTConRoute::Request(
       const UINT    request    // Types of requests
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.Request(
       EnRouteFlags  request    // Types of requests
       )

Python (Manager API)
    
    
    MTConRoute.Request

### Parameters

**request**  
[in] The requests for which the rule is applicable. To pass the types, theIMTConRoute::EnRouteFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
