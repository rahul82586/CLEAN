[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueColor

[Previous](IMTConCondition-ValueString.md) | [Next](IMTConCondition-ValueMoney.md)

# IMTConVPSCondition::ValueColor

Get a condition value of the colorref type.

C++
    
    
    COLORREF  IMTConVPSCondition::ValueColor()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConVPSCondition.ValueColor()

Python
    
    
    MTConVPSCondition.ValueColor

### Return Value

The condition value of a colorref type.

# IMTConVPSCondition::ValueColor

Set a condition value of the colorref type.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueColor(
       const COLORREF  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueColor(
       uint            value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueColor

### Parameters

**value**  
[in] A value of colorref type.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
