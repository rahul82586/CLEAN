[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleDelete

[Previous](RuleUpdate.md) | [Next](RuleClear.md)

# IMTConLeverage::RuleDelete

Delete a rule from a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverage::RuleDelete(
       const UINT  pos      // Rule position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.RuleDelete(
       uint        pos      // Rule position
       )

Python (Manager API).NET (Gateway/Manager API)
    
    
    MTConLeverage.RuleDelete(
       pos         # Rule position
       )

### Parameters

**pos**  
[in] Position of the rule in the list, starting from 0.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
