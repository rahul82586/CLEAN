[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / TierClear

[Previous](TierDelete.md) | [Next](TierShift.md)

# IMTConLeverageRule::TierClear

Clear the list of levels in a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageRule::TierClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.TierClear()

Python (Manager API)
    
    
    MTConLeverageRule.TierClear()

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all rules from a rule.
