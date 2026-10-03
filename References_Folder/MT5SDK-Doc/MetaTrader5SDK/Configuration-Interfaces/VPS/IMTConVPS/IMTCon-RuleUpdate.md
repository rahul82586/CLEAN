[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon RuleUpdate

[Previous](IMTCon-RuleAdd.md) | [Next](IMTCon-RuleDelete.md)

# IMTConVPS::RuleUpdate

Edit a VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPS::RuleUpdate(
       const UINT               pos,      // Rule position
       const IMTConVPSRule*     rule      // Rule object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.RuleUpdate(
       uint                     pos,      // Rule position
       CIMTConVPSRule           rule      // Rule object
       )

Python
    
    
    MTConVPS.RuleUpdate(
       pos,                     # Rule position
       rule                     # Rule object
       )
    
    
    MTConVPS.RuleSet(
       rule_list                # List of rules
       )

### Parameters

**pos**  
[in] Rule position in the list starting from 0.

**rule**  
[in]IMTConVPSRulerule object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
