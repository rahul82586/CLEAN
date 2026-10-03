[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueLeverage

[Previous](ValueDatetime.md) | [Next](ValueBool.md)

# IMTConAutoParam::ValueLeverage

Get the value of the parameter that expresses the leverage.

C++
    
    
    INT64  IMTConAutoParam::ValueLeverage()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoParam.ValueLeverage()

Python
    
    
    MTConAutoParam.ValueLeverage

### Return Value

Value of the leverage from 1 to 500.

# IMTConAutoParam::ValueLeverage

Set the value of the parameter that expresses the leverage.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueLeverage(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueLeverage(
       long         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueLeverage

### Parameters

**value**  
[in] Value of the leverage from 1 to 500.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
