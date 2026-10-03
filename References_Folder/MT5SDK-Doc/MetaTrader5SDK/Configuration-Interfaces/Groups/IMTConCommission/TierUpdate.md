[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / TierUpdate

[Previous](TierAdd.md) | [Next](TierDelete.md)

# IMTConCommission::TierUpdate

Update commission range.

C++
    
    
    MTAPIRES  IMTConCommission::TierUpdate(
       const UINT       pos,      // Position of the range
       IMTConCommTier*  tier      // An object of commission range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.TierUpdate(
       uint             pos,      // Position of the range
       CIMTConCommTier  tier      // An object of commission range
       )

Python (Manager API)
    
    
    MTConCommission.TierUpdate(
       pos,             # Position of the range
       tier             # An object of commission range
       )
    
    
    MTConCommission.TierSet(
       tier_list        # A list of commission ranges
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**tier**  
[in] An object of the commission range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
