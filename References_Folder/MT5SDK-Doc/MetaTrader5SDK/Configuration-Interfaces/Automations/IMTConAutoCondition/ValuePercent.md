[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValuePercent

[Previous](ValueDate.md) | [Next](ValueLanguage.md)

# IMTConAutoCondition::ValuePercent

Get a condition value expressing a percentage.

C++
    
    
    UINT  IMTConAutoCondition::ValuePercent()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValuePercent()

Python
    
    
    MTConAutoCondition.ValuePercent

### Return Value

Percentage value.

# IMTConAutoCondition::ValuePercent

Set a condition value expressing a percentage.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValuePercent(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValuePercent(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValuePercent

### Parameters

**value**  
[in] Percentage value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
