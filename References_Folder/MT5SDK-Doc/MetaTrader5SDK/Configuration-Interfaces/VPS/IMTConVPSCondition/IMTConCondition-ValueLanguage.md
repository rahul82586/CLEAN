[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueLanguage

[Previous](IMTConCondition-ValuePercent.md) | [Next](../IMTConGroup.md)

# IMTConVPSCondition::ValueLanguage

Get a condition value expressing the language.

C++
    
    
    UINT  IMTConVPSCondition::ValueLanguage()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConVPSCondition.ValueLanguage()

Python
    
    
    MTConVPSCondition.ValueLanguage

### Return Value

The language in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (a value from Prim.lang.identifier).

# IMTConVPSCondition::ValueLanguage

Set a condition value expressing the language.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueLanguage(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueLanguage(
       uint        value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueLanguage

### Parameters

**value**  
[in] The language in the LANGID format used inMS Windowssystems (a value from Prim.lang.identifier).

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
