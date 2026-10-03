[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueMoney

[Previous](ValueColor.md) | [Next](ValueVolume.md)

# IMTConCondition::ValueMoney

Get the value of a condition that expresses the amount of money.

C++
    
    
    double  IMTConCondition::ValueMoney()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCondition.ValueMoney()

Python (Manager API)
    
    
    MTConCondition.ValueMoney

### Return Value

A value of the double type.

# IMTConCondition::ValueMoney

Set the value of a condition that expresses the amount of money.

C++
    
    
    MTAPIRES  IMTConCondition::ValueMoney(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueMoney(
       double        value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueMoney

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
