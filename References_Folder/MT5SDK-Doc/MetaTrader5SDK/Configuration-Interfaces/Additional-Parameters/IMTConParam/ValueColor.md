[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueColor

[Previous](ValueBool.md) | [Next](../IMTConParamArray.md)

# IMTConParam::ValueColor

Get a previously set colorref parameter value.

C++
    
    
    COLORREF  IMTConParam::ValueColor()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConParam.ValueColor()

Python
    
    
    MTConParam.ValueColor

### Return Value

The previously set colorref parameter value.

### Note

The parameter received must be of type [IMTConParam::TYPE_COLOR (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueColor

Sett a colorref parameter value.

C++
    
    
    MTAPIRES  IMTConParam::ValueColor(
       const COLORREF   value   // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueColor(
       uint             value   // Value
       )

Python
    
    
    MTConParam.ValueColor

### Parameters

**value**  
[in] The colorref type parameter value.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.

### Note

The parameter type is changed to [IMTConParam::TYPE_COLOR (#paramtype)](Enumerations.md#paramtype) after the method call.
