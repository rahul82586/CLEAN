[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon RuleAdd

[Previous](IMTCon-MQL5Password.md) | [Next](IMTCon-RuleUpdate.md)

# IMTConVPS::RuleAdd

Add a VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPS::RuleAdd(
       IMTConVPSRule*  rule      // Rule object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.RuleAdd(
       CIMTConVPSRule  rule      // Rule object
       )

Python
    
    
    MTConVPS.RuleAdd(
       rule            # Rule object
       )

### Parameters

**rule**  
[in]IMTConVPSRulerule object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
