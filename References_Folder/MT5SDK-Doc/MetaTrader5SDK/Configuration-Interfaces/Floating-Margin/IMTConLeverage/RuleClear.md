[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleClear

[Previous](RuleDelete.md) | [Next](RuleShift.md)

# IMTConLeverage::RuleClear

Clear the list of rules in a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverage::RuleClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.RuleClear()

Python (Manager API)
    
    
    MTConLeverage.RuleClear()

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all rules from a configuration.
