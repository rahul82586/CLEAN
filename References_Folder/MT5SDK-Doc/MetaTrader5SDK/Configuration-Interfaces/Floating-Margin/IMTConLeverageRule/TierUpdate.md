[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / TierUpdate

[Previous](TierAdd.md) | [Next](TierDelete.md)

# IMTConLeverageRule::TierUpdate

Update a level in a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageRule::TierUpdate(
       const UINT           pos,  // Level position
       IMTConLeverageTier*  tier  // Level object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.TierUpdate(
       uint                 pos,  // Level position
       CIMTConLeverageTier  tier  // Level object
       )

Python (Manager API)
    
    
    MTConLeverageRule.TierUpdate(
       pos,                 # Level position
       tier                 # Level object
       )
    
    
    MTConLeverageRule.TierSet(
       tier_list            # A list of levels
       )

### Parameters

**pos**  
[in] Position of the level in the list, starting from 0.

**tier**  
[in]IMTConLeverageTierlevel object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
