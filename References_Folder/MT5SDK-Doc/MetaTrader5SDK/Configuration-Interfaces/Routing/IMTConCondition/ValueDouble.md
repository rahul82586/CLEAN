[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueDouble

[Previous](ValueUInt.md) | [Next](ValueString.md)

# IMTConCondition::ValueDouble

Get the value of a condition of the double type.

C++
    
    
    double  IMTConCondition::ValueDouble()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCondition.ValueDouble()

Python (Manager API)
    
    
    MTConCondition.ValueDouble

### Return Value

The condition value of the double type.

# IMTConCondition::ValueDouble

Set the value of a condition of the double type.

C++
    
    
    MTAPIRES  IMTConCondition::ValueDouble(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueDouble(
       double        value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueDouble

### Parameters

**value**  
[in] A value of the double type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
