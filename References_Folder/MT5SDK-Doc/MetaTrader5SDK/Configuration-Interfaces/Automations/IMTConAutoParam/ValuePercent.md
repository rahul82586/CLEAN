[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValuePercent

[Previous](ValueDate.md) | [Next](ValueLanguage.md)

# IMTConAutoParam::ValuePercent

Get the value of the parameter that expresses the percentage.

C++
    
    
    UINT  IMTConAutoParam::ValuePercent()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoParam.ValuePercent()

Python
    
    
    MTConAutoParam.ValuePercent

### Return Value

Percentage value.

# IMTConAutoParam::ValuePercent

Set the value of the parameter that expresses the percentage.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValuePercent(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValuePercent(
       uint        value      // Value
       )

Python
    
    
    MTConAutoParam.ValuePercent

### Parameters

**value**  
[in] Percentage value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
