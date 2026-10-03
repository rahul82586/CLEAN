[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / TierDelete

[Previous](TierUpdate.md) | [Next](TierClear.md)

# IMTConLeverageRule::TierDelete

Delete a level from a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageRule::TierDelete(
       const UINT  pos      // Level position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.TierDelete(
       uint        pos      // Level position
       )

Python (Manager API)
    
    
    MTConLeverageRule.TierDelete(
       pos         # Level position
       )

### Parameters

**pos**  
[in] Position of the level in the list, starting from 0.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
