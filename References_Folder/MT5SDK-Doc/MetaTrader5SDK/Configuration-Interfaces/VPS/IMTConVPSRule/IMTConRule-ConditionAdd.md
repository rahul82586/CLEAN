[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule ConditionAdd

[Previous](IMTConRule-Name.md) | [Next](IMTConRule-ConditionUpdate.md)

# IMTConVPSRule::ConditionAdd

Add a condition to the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSRule::ConditionAdd(
       IMTConVPSCondition*  cfg       // Condition object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ConditionAdd(
       CIMTConVPSCondition  cfg       // Condition object
       )

Python
    
    
    MTConRoute.ConditionAdd(
       cfg                  # Condition object
       )

### Parameters

**cfg**  
[in]IMTConVPSConditioncondition object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
