[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueBool

[Previous](ValueLeverage.md) | [Next](ValueTime.md)

# IMTConAutoCondition::ValueBool

Get the condition value of the bool type.

C++
    
    
    bool  IMTConAutoCondition::ValueBool()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConAutoCondition.ValueBool()

Python
    
    
    MTConAutoCondition.ValueBool

### Return Value

True or false.

# IMTConAutoCondition::ValueBool

Set the condition value of the bool type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueBool(
       const bool  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueBool(
       bool        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueBool

### Parameters

**value**  
[in] True or false.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
