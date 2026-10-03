[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamLeverage

[Previous](ParamDatetime.md) | [Next](ParamBool.md)

# IMTConRoute::ParamLeverage

Get the value of an additional parameter that expresses the leverage.

C++
    
    
    INT64  IMTConRoute::ParamLeverage()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConRoute.ParamLeverage()

Python (Manager API)
    
    
    MTConRoute.ParamLeverage

### Return Value

Value of the leverage from 1 to 500.

# IMTConRoute::ParamLeverage

Set the value of an additional parameter that expresses the leverage.

C++
    
    
    MTAPIRES  IMTConRoute::ParamLeverage(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamLeverage(
       long         value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamLeverage

### Parameters

**value**  
[in] Value of the leverage from 1 to 500.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
