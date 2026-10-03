[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / TierDelete

[Previous](TierUpdate.md) | [Next](TierClear.md)

# IMTConCommission::TierDelete

Delete a commission range by the index.

C++
    
    
    MTAPIRES  IMTConCommission::TierDelete(
       const UINT  pos      // Position of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.TierDelete(
       uint        pos      // Position of the range
       )

Python (Manager API)
    
    
    MTConCommission.TierDelete(
       pos         # Position of the range
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
