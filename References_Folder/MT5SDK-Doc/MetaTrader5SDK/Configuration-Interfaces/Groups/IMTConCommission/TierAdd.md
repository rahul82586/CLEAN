[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / TierAdd

[Previous](TurnoverCurrency.md) | [Next](TierUpdate.md)

# IMTConCommission::TierAdd

Add commission range.

C++
    
    
    MTAPIRES  IMTConCommission::TierAdd(
       IMTConCommTier*  tier      // An object of commission range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.TierAdd(
       CIMTConCommTier  tier      // An object of commission range
       )

Python (Manager API)
    
    
    MTConCommission.TierAdd(
       tier             # An object of commission range
       )

### Parameters

**tier**  
[in] An object of the commission range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
