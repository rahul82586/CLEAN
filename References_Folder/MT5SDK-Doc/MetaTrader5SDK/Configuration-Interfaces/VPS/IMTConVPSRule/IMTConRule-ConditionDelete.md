[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule ConditionDelete

[Previous](IMTConRule-ConditionUpdate.md) | [Next](IMTConRule-ConditionClear.md)

# IMTConVPSRule::ConditionDelete

Delete a condition from the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSRule::ConditionDelete(
       const UINT  pos      // Condition position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.ConditionDelete(
       uint        pos      // Condition position
       )

Python
    
    
    MTConVPSRule.ConditionDelete(
       pos         # Condition position
       )

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
