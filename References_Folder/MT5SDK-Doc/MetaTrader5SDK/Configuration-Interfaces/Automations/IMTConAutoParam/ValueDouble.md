[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueDouble

[Previous](ValueUInt.md) | [Next](ValueString.md)

# IMTConAutoParam::ValueDouble

Get a parameter value of double type.

C++
    
    
    double  IMTConAutoParam::ValueDouble()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConAutoParam.ValueDouble()

Python
    
    
    MTConAutoParam.ValueDouble

### Return Value

The parameter value of a double type.

# IMTConAutoParam::ValueDouble

Set a parameter value of double type.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueDouble(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueDouble(
       double        value      // Value
       )

Python
    
    
    MTConAutoParam.ValueDouble

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
