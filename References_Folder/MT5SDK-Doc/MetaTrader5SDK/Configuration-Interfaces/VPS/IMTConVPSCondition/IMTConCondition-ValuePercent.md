[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValuePercent

[Previous](IMTConCondition-ValueDate.md) | [Next](IMTConCondition-ValueLanguage.md)

# IMTConVPSCondition::ValuePercent

Get a condition value expressing a percentage.

C++
    
    
    UINT  IMTConVPSCondition::ValuePercent()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConVPSCondition.ValuePercent()

Python
    
    
    MTConVPSCondition.ValuePercent

### Return Value

Percentage value.

# IMTConVPSCondition::ValuePercent

Set a condition value expressing a percentage.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValuePercent(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValuePercent(
       uint        value      // Value
       )

Python
    
    
    MTConVPSCondition.ValuePercent

### Parameters

**value**  
[in] Percentage value.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
