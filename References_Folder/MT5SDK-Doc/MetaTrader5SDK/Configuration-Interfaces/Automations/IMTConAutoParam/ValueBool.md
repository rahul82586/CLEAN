[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueBool

[Previous](ValueLeverage.md) | [Next](ValueTime.md)

# IMTConAutoParam::ValueBool

Get a parameter value of bool type.

C++
    
    
    bool  IMTConAutoParam::ValueBool()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConAutoParam.ValueBool()

Python
    
    
    MTConAutoParam.ValueBool

### Return Value

True or false.

# IMTConAutoParam::ValueBool

Set a parameter value of bool type.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueBool(
       const bool  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueBool(
       bool        value      // Value
       )

Python
    
    
    MTConAutoParam.ValueBool

### Parameters

**value**  
[in] True or false.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
