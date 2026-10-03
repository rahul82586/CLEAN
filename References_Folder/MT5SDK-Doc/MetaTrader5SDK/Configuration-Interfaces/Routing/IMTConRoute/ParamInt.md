[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamInt

[Previous](ParamType.md) | [Next](ParamUInt.md)

# IMTConRoute::ParamInt

Get the value of an additional parameter of the INT type.

C++
    
    
    INT64  IMTConRoute::ParamInt()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConRoute.ParamInt()

Python (Manager API)
    
    
    MTConRoute.ParamInt

### Return Value

The parameter value of the INT type.

# IMTConRoute::ParamInt

Set the value of an additional parameter of the INT type.

C++
    
    
    MTAPIRES  IMTConRoute::ParamInt(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamInt(
       long         value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamInt

### Parameters

**value**  
[in] Parameter value of INT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
