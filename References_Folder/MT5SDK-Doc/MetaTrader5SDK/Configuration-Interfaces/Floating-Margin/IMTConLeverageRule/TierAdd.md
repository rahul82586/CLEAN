[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / TierAdd

[Previous](RangeValueCurrency.md) | [Next](TierUpdate.md)

# IMTConLeverageRule::TierAdd

Add a level to a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageRule::TierAdd(
       IMTConLeverageTier*  tier  // Level object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.TierAdd(
       CIMTConLeverageTier   tier  // Level object
       )

Python (Manager API)
    
    
    MTConLeverageRule.TierAdd(
       tier                  # Level object
       )

### Parameters

**tier**  
[in]IMTConLeverageTierlevel object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
