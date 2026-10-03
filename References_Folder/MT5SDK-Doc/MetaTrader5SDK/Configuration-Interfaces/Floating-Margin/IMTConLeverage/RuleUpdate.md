[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleUpdate

[Previous](RuleAdd.md) | [Next](RuleDelete.md)

# IMTConLeverage::RuleUpdate

Update a rule in a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverage::RuleUpdate(
       const UINT           pos, // Rule position
       IMTConLeverageRule*  cfg  // Rule object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.RuleUpdate(
       uint                 pos, // Rule position
       CIMTConLeverageRule  cfg  // Rule object
       )

Python (Manager API)
    
    
    MTConLeverage.RuleUpdate(
       pos,                 # Rule position
       cfg                  # Rule object
       )

### Parameters

**pos**  
[in] Position of the rule in the list, starting from 0.

**cfg**  
[in]IMTConLeverageRulerule object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
