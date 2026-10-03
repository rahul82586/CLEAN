[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ReasonSet

[Previous](Reason.md) | [Next](TimeSetup.md)

# IMTOrder::ReasonSet

Sets the order placing reason.

C++
    
    
    MTAPIRES  IMTOrder::ReasonSet(
       const UINT  reason    // Reason
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ReasonSet(
       uint        reason    // Reason
       )

Python
    
    
    MTOrder.Reason()

### Parameters

**reason**  
[in] Reason for placing the order. The reason is passed using theIMTOrder::EnOrderReasonenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

To preserve the integrity of data, do not change order reasons unless you have a special need.
