[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule Clear

[Previous](IMTConRule-Assign.md) | [Next](IMTConRule-Enabled.md)

# IMTConVPSRule::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConVPSRule::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.Clear()

Python
    
    
    MTConVPSRule.Clear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
