[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamDatetime

[Previous](ParamVolumeExt.md) | [Next](ParamLeverage.md)

# IMTConRoute::ParamDatetime

Get the value of an additional parameter that expresses date and time.

C++
    
    
    INT64  IMTConRoute::ParamDatetime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConRoute.ParamDatetime()

Python (Manager API)
    
    
    MTConRoute.ParamDatetime

### Return Value

Date and time in seconds that have elapsed since 01.01.1970.

# IMTConRoute::ParamDatetime

Set the value of an additional parameter that expresses date and time.

C++
    
    
    MTAPIRES  IMTConRoute::ParamDatetime(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamDatetime(
       long         value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamDatetime

### Parameters

**value**  
[in] Date and time in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
