[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionDelete

[Previous](CommissionUpdate.md) | [Next](CommissionClear.md)

# IMTConGroup::CommissionDelete

Delete a commission setting by the index.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionDelete(
       const UINT  pos      // Position of the commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CommissionDelete(
       uint        pos      // Position of the commission
       )

Python (Manager API)
    
    
    MTConGroup.CommissionDelete(
       pos         # Position of the commission
       )

### Parameters

**pos**  
[in] Position of a commission in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
