[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / TierNext

[Previous](TierTotal.md) | [Next](../IMTConLeverageTier.md)

# IMTConLeverageRule::TierNext

Get a level from floating margin rules by index.

C++
    
    
    LPCWSTR  IMTConLeverageRule::TierNext(
       const UINT            pos   // Level position
       IMTConLeverageTier*   tier  // Level object
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConLeverageRule.TierNext(
       uint                  pos,  // Level position
       CIMTConLeverageTier   tier  // Level object
       )

Python (Manager API)
    
    
    MTConLeverageRule.TierNext(
       pos                   # Level position
       )
    
    
    MTConLeverageRule.TierGet()

### Parameters

**pos**  
[in] Position of the rule in the list.

**tier**  
[out]IMTConLeverageRulerule object. The object must be created in advance using theIMTServerAPI::LeverageTierCreate,IMTAdminAPI::LeverageTierCreate, orIMTManagerAPI::LeverageTierCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
