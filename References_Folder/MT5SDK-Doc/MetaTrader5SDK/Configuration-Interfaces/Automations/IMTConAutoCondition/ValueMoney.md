[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueMoney

[Previous](ValueColor.md) | [Next](ValueVolume.md)

# IMTConAutoCondition::ValueMoney

Get a condition value that expresses the amount of money.

C++
    
    
    double  IMTConAutoCondition::ValueMoney()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConAutoCondition.ValueMoney()

Python
    
    
    MTConAutoCondition.ValueMoney

### Return Value

A value of the double type.

# IMTConAutoCondition::ValueMoney

Set a condition value that expresses the amount of money.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueMoney(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueMoney(
       double        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueMoney

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
