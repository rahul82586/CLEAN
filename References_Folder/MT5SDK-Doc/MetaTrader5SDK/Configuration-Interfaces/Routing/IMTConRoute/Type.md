[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / Type

[Previous](Request.md) | [Next](Action.md)

# IMTConRoute::Type

Get orders for which the rule is applicable.

C++
    
    
    UINT  IMTConRoute::Type()  const

.NET (Gateway/Manager API)
    
    
    EnTypeFlags  CIMTConRoute.Type()

Python (Manager API)
    
    
    MTConRoute.Type

### Return Value

A value of the [IMTConRoute::EnTypeFlags (#entypeflags)](Enumerations.md#entypeflags) enumeration.

# IMTConRoute::Type

Set orders for which the rule is applicable.

C++
    
    
    MTAPIRES  IMTConRoute::Type(
       const UINT   type     // Types of orders
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.Type(
       EnTypeFlags  type     // Types of orders
       )

Python (Manager API)
    
    
    MTConRoute.Type

### Parameters

**type**  
[in] Types of orders for which the rule is applicable. To pass the types, theIMTConRoute::EnTypeFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
