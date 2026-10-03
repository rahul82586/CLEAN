[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueSymbols

[Previous](ValueGroups.md) | [Next](ValueBool.md)

# IMTConParam::ValueSymbols

Gets a previously specified parameter value of the "symbol" type.

C++
    
    
    LPCWSTR  IMTConParam::ValueSymbols()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConParam.ValueSymbols()

Python
    
    
    MTConParam.ValueSymbols

### Return Value

A previously specified parameter value of the "symbol" type.

### Note

The type of the received parameter must be [IMTConParam:TYPE_SYMBOLS (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueSymbols

Sets a parameter value of the "symbol" type.

C++
    
    
    MTAPIRES  IMTConParam::ValueSymbols(
       const LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueSymbols(
       string         value      // Value
       )

Python
    
    
    MTConParam.ValueSymbols

### Parameters

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the call of the method, the parameter type is changed to [IMTConParam:TYPE_SYMBOLS (#paramtype)](Enumerations.md#paramtype).
