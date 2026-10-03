[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule ConditionNext

[Previous](IMTConRule-ConditionTotal.md) | [Next](../IMTConCondition.md)

# IMTConVPSRule::ConditionNext

Get a condition in the VPS allocation rule by index.

C++
    
    
    MTAPIRES  IMTConVPSRule::ConditionNext(
       const UINT           pos,        // Condition position
       IMTConVPSCondition*  cfg         // Condition object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.ConditionNext(
       uint                 pos,        // Condition position
       CIMTConVPSCondition  cfg         // Condition object
       )

Python
    
    
    MTConVPSRule.ConditionNext(
       pos                  # Condition position
       )
    
    
    MTConVPSRule.ConditionGet()

### Parameters

**pos**  
[in] Position of a condition in the list, starting from 0.

**cfg**  
[out]IMTConVPSConditioncondition object. The object must first be created using theIMTServerAPI::VPSCreateConditionorIMTAdminAPI::VPSCreateCondition.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
