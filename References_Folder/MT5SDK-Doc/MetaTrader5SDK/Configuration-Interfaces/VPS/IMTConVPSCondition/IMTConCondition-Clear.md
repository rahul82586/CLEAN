[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition Clear

[Previous](IMTConCondition-Assign.md) | [Next](IMTConCondition-Condition.md)

# IMTConVPSCondition::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConVPSCondition::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.Clear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
