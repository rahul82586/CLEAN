[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueMoney

[Previous](ValueColor.md) | [Next](ValueVolume.md)

# IMTConAutoParam::ValueMoney

Get the value of the parameter that expresses the amount of money.

C++
    
    
    double  IMTConAutoParam::ValueMoney()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConAutoParam.ValueMoney()

Python
    
    
    MTConAutoParam.ValueMoney

### Return Value

A value of the double type.

# IMTConAutoParam::ValueMoney

Set the value of the parameter that expresses the amount of money.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueMoney(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueMoney(
       double        value      // Value
       )

Python
    
    
    MTConAutoParam.ValueMoney

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
