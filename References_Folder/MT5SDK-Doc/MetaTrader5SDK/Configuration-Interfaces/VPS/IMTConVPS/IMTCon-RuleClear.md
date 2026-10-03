[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon RuleClear

[Previous](IMTCon-RuleDelete.md) | [Next](IMTCon-RuleShift.md)

# IMTConVPS::RuleClear

Clear the list of VPS allocation rules.

C++
    
    
    MTAPIRES  IMTConVPS::RuleClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.RuleClear()

Python
    
    
    MTConVPS.RuleClear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method deletes all rules from the VPS allocation settings.
