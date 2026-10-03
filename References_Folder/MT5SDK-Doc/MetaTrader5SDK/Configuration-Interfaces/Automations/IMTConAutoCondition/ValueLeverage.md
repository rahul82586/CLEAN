[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueLeverage

[Previous](ValueDatetime.md) | [Next](ValueBool.md)

# IMTConAutoCondition::ValueLeverage

Get a condition value expressing the leverage.

C++
    
    
    INT64  IMTConAutoCondition::ValueLeverage()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoCondition.ValueLeverage()

Python
    
    
    MTConAutoCondition.ValueLeverage

### Return Value

Value of the leverage from 1 to 500.

# IMTConAutoCondition::ValueLeverage

Set a condition value expressing the leverage.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueLeverage(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueLeverage(
       long         value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueLeverage

### Parameters

**value**  
[in] Value of the leverage from 1 to 500.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
