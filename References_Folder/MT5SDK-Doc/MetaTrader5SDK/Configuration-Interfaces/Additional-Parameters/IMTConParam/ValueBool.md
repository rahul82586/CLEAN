[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueBool

[Previous](ValueSymbols.md) | [Next](ValueColor.md)

# IMTConParam::ValueBool

Get a previously set bool parameter value.

C++
    
    
    bool  IMTConParam::ValueBool()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConParam.ValueBool()

Python
    
    
    MTConParam.ValueBool

### Return Value

Previously set bool parameter value.

### Note

The requested parameter type must be [IMTConParam::TYPE_BOOL (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueBool

Set the bool parameter value.

C++
    
    
    MTAPIRES  IMTConParam::ValueBool(
       const bool   value      // value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueBool(
       bool         value      // value
       )

Python
    
    
    MTConParam.ValueBool

### Parameters

**value**  
[in] Parameter value: TRUE or FALSE.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The parameter type is changed to [IMTConParam::TYPE_BOOL (#paramtype)](Enumerations.md#paramtype) after the method call.
