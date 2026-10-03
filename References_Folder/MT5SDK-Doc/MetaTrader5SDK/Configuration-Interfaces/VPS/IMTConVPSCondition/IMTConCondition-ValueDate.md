[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueDate

[Previous](IMTConCondition-ValueTime.md) | [Next](IMTConCondition-ValuePercent.md)

# IMTConVPSCondition::ValueDate

Get a condition value expressing a date.

C++
    
    
    INT64  IMTConVPSCondition::ValueDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConVPSCondition.ValueDate()

Python
    
    
    MTConVPSCondition.ValueDate

### Return Value

Date in seconds since 01.01.1970 (00:00 of the specified day).

# IMTConVPSCondition::ValueDate

Set a condition value that expresses a date.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueDate(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueDate(
       long         value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueDate

### Parameters

**value**  
[in] Date in seconds since 01.01.1970 (00:00 of the specified day).

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
