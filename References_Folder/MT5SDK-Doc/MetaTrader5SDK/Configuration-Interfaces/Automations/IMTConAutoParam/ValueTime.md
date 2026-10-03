[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueTime

[Previous](ValueBool.md) | [Next](ValueDate.md)

# IMTConAutoParam::ValueTime

Get the value of the parameter expressing time.

C++
    
    
    UINT  IMTConAutoParam::ValueTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoParam.ValueTime()

Python
    
    
    MTConAutoParam.ValueTime

### Return Value

Time in minutes elapsed since 00:00.

# IMTConAutoParam::ValueTime

Set the value of the parameter expressing time.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueTime(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueTime(
       uint        value      // Value
       )

Python
    
    
    MTConAutoParam.ValueTime

### Parameters

**value**  
[in] A value in minutes elapsed since 00:00.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
