[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueMoney

[Previous](IMTConCondition-ValueColor.md) | [Next](IMTConCondition-ValueDatetime.md)

# IMTConVPSCondition::ValueMoney

Get the value of a condition that expresses the amount of money.

C++
    
    
    double  IMTConVPSCondition::ValueMoney()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConVPSCondition.ValueMoney()

Python
    
    
    MTConVPSCondition.ValueMoney

### Return Value

A value of the double type.

# IMTConVPSCondition::ValueMoney

Set the value of a condition that expresses the amount of money.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueMoney(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueMoney(
       double        value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueMoney

### Parameters

**value**  
[in] A value of the double type.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
