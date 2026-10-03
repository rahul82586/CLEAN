[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule ConditionClear

[Previous](IMTConRule-ConditionDelete.md) | [Next](IMTConRule-ConditionShift.md)

# IMTConVPSRule::ConditionClear

Clear the list of conditions in the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSRule::ConditionClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.ConditionClear()

Python
    
    
    MTConVPSRule.ConditionClear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method deletes all conditions from the VPS allocation rule.
