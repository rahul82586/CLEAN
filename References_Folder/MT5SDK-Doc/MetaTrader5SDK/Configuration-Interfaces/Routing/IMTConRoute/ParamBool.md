[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamBool

[Previous](ParamLeverage.md) | [Next](ParamTime.md)

# IMTConRoute::ParamBool

Get the value of an additional parameter of the bool type.

C++
    
    
    bool  IMTConRoute::ParamBool()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConRoute.ParamBool()

Python (Manager API)
    
    
    MTConRoute.ParamBool

### Return Value

Can be true or false.

# IMTConRoute::ParamBool

Set the value of an additional parameter of the bool type.

C++
    
    
    MTAPIRES  IMTConRoute::ParamBool(
       const bool  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamBool(
       bool        value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamBool

### Parameters

**value**  
[in] True or false.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
