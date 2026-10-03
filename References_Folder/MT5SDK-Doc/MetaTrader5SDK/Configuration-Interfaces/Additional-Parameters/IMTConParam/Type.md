[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / Type

[Previous](Name.md) | [Next](Value.md)

# IMTConParam::Type

Get the type of a parameter.

C++
    
    
    UINT  IMTConParam::Type()  const

.NET (Gateway/Manager API)
    
    
    ParamType  CIMTConParam.Type()

Python
    
    
    MTConParam.Type

### Return Value

A value from [IMTConParam::ParamType (#paramtype)](Enumerations.md#paramtype).

# IMTConParam::Type

Set the parameter type.

C++
    
    
    MTAPIRES  IMTConParam::Type(
       const UINT  type      // Parameter type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.Type(
       ParamType   type      // Parameter type
       )

Python
    
    
    MTConParam.Type

### Parameters

**type**  
[in] The parameter type is set using theIMTConParam::ParamTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
