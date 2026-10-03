[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleAdd

[Previous](Name.md) | [Next](RuleUpdate.md)

# IMTConLeverage::RuleAdd

Add a rule to a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverage::RuleAdd(
       IMTConLeverageRule*  cfg  // Rule object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.RuleAdd(
       CIMTConLeverageRule   cfg  // Rule object
       )

Python (Manager API)
    
    
    MTConLeverage.RuleAdd(
       cfg                   # Rule object
       )

### Parameters

**cfg**  
[in]IMTConLeverageRulerule object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
