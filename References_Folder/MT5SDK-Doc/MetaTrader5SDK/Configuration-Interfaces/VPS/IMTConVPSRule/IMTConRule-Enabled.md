[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule Enabled

[Previous](IMTConRule-Clear.md) | [Next](IMTConRule-Name.md)

# IMTConVPSRule::Enabled

Get the state of the VPS allocation rule.

C++
    
    
    bool  IMTConVPSRule::Enabled()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConVPSRule.Enabled()

Python
    
    
    MTConVPSRule.Enabled

### Return Value

If the rule is enabled, the method returns TRUE; otherwise, it returns FALSE.

# IMTConVPSRule::Enabled

Set the state of the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSRule::Enabled(
       const bool   enabled  // Rule state
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.Mode(
       bool         enabled  // Rule state
       )

Python
    
    
    MTConVPSRule.Enabled

### Parameters

**enabled**  
[in] Hosting allocation rule state: TRUE — enabled, FALSE — disabled.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
