[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamMoney

[Previous](ParamColor.md) | [Next](ParamVolume.md)

# IMTConRoute::ParamMoney

Get the value of an additional parameter that expresses the amount of money.

C++
    
    
    double  IMTConRoute::ParamMoney()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConRoute.ParamMoney()

Python (Manager API)
    
    
    MTConRoute.ParamMoney

### Return Value

A value of the double type.

# IMTConRoute::ParamMoney

Set the value of an additional parameter that expresses the amount of money.

C++
    
    
    MTAPIRES  IMTConRoute::ParamMoney(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamMoney(
       double        value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamMoney

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
