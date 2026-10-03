[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / TierNext

[Previous](TierTotal.md) | [Next](../IMTConCommTier.md)

# IMTConCommission::TierNext

Get a commission range by the index.

C++
    
    
    MTAPIRES  IMTConCommission::TierNext(
       const UINT       pos,      // Position of the range
       IMTConCommTier*  tier      // An object of commission range
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.TierNext(
       uint             pos,      // Position of the range
       CIMTConCommTier  tier      // An object of commission range
       )

Python (Manager API)
    
    
    MTConCommission.TierNext(
       pos              # Position of the range
       )
    
    
    MTConCommission.TierGet()

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**tier**  
[out] An object of the commission range. The tier object must be first created using theIMTAdminAPI::GroupTierCreateorIMTManagerAPI::GroupTierCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of the range with a specified index to the tier object.
