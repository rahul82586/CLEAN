[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamTime

[Previous](ParamBool.md) | [Next](ConditionAdd.md)

# IMTConRoute::ParamTime

Get the value of an additional parameter that expresses the time.

C++
    
    
    UINT  IMTConRoute::ParamTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConRoute.ParamTime()

Python (Manager API)
    
    
    MTConRoute.ParamTime

### Return Value

Time in minutes elapsed since 00:00.

# IMTConRoute::ParamTime

Set the value of an additional parameter that expresses the time.

C++
    
    
    MTAPIRES  IMTConRoute::ParamTime(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamTime(
       uint        value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamTime

### Parameters

**value**  
[in] A value in minutes elapsed since 00:00.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
