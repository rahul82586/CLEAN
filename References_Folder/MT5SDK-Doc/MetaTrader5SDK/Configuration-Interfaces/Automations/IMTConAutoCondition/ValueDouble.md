[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueDouble

[Previous](ValueUInt.md) | [Next](ValueString.md)

# IMTConAutoCondition::ValueDouble

Get a condition value of the double type.

C++
    
    
    double  IMTConAutoCondition::ValueDouble()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConAutoCondition.ValueDouble()

Python
    
    
    MTConAutoCondition.ValueDouble

### Return Value

The condition value of the double type.

# IMTConAutoCondition::ValueDouble

Set a condition value of the double type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueDouble(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueDouble(
       double        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueDouble

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
