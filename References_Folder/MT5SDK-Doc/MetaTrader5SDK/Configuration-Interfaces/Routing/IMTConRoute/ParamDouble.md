[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamDouble

[Previous](ParamUInt.md) | [Next](ParamString.md)

# IMTConRoute::ParamDouble

Get the value of an additional parameter of the double type.

C++
    
    
    double  IMTConRoute::ParamDouble()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConRoute.ParamDouble()

Python (Manager API)
    
    
    MTConRoute.ParamDouble

### Return Value

The parameter value of a double type.

# IMTConRoute::ParamDouble

Set the value of a parameter of the double type.

C++
    
    
    MTAPIRES  IMTConRoute::ParamDouble(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamDouble(
       double        value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamDouble

### Parameters

**value**  
[in] Parameter value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
