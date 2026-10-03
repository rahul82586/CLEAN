[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule ConditionUpdate

[Previous](IMTConRule-ConditionAdd.md) | [Next](IMTConRule-ConditionDelete.md)

# IMTConVPSRule::ConditionUpdate

Edit a condition in the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSRule::ConditionUpdate(
       const UINT              pos,           // Condition position
       const IMTConVPSRule*    condition      // Condition object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.ConditionUpdate(
       uint                    pos,           // Condition position
       CIMTConVPSRule          condition      // Condition object
       )

Python
    
    
    MTConVPSRule.ConditionUpdate(
       pos,                    # Condition position
       condition               # Condition object
       )
    
    
    MTConVPSRule.ConditionSet(
       condition_list          # List of conditions
       )

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

**condition**  
[in]IMTConVPSConditioncondition object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
