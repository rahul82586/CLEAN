[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition Assign

[Previous](IMTConCondition-Release.md) | [Next](IMTConCondition-Clear.md)

# IMTConVPSCondition::Assign

Assign the passed object to the current one.

C++
    
    
    MTAPIRES  IMTConVPSCondition::Assign(
       const IMTConVPSCondition*  param    // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.Assign(
       CIMTConVPSCondition        param    // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
