[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ReasonSet

[Previous](Reason.md) | [Next](Gateway.md)

# IMTDeal::ReasonSet

Sets the reason for a deal.

C++
    
    
    MTAPIRES  IMTDeal::ReasonSet(
       const UINT  reason    // Reason
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.ReasonSet(
       uint        reason    // Reason
       )

### Parameters

**reason**  
[in] Reason for deal execution. The reason is passed using theIMTDeal::EnDealReasonenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

To preserve the integrity of data, do not change deal reasons unless you have a special need.
