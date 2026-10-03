[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon RuleDelete

[Previous](IMTCon-RuleUpdate.md) | [Next](IMTCon-RuleClear.md)

# IMTConVPS::RuleDelete

Delete a VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPS::RuleDelete(
       const UINT  pos      // Rule position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.RuleDelete(
       uint        pos      // Rule position
       )

Python
    
    
    MTConVPS.RuleDelete(
       uint        pos      // Rule position
       )

### Parameters

**pos**  
[in] Rule position in the list starting from 0.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
