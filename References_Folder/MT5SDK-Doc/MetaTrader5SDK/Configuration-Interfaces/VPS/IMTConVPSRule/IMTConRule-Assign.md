[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule Assign

[Previous](IMTConRule-Release.md) | [Next](IMTConRule-Clear.md)

# IMTConVPSRule::Assign

Assign the passed object to the current one.

C++
    
    
    MTAPIRES  IMTConVPSRule::Assign(
       const IMTConVPSRule*  param    // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.Assign(
       CIMTConVPSRule        param    // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
