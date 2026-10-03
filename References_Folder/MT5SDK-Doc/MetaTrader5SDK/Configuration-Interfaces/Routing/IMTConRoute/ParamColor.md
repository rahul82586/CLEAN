[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamColor

[Previous](ParamString.md) | [Next](ParamMoney.md)

# IMTConRoute::ParamColor

Get the value of an additional parameter of the colorref type.

C++
    
    
    COLORREF  IMTConRoute::ParamColor()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConRoute.ParamColor()

Python (Manager API)
    
    
    MTConRoute.ParamColor

### Return Value

The parameter value of a colorref type.

# IMTConRoute::ParamColor

Set the value of an additional parameter of the colorref type.

C++
    
    
    MTAPIRES  IMTConRoute::ParamColor(
       const COLORREF  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamColor(
       uint            value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamColor

### Parameters

**value**  
[in] The parameter value of a colorref type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
