[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionShift

[Previous](CommissionClear.md) | [Next](CommissionTotal.md)

# IMTConGroup::CommissionShift

Move a commission setting in the list.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionShift(
       const UINT  pos,       // Position of the commission
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode CIMTConGroup.CommissionShift(
       uint        pos,       // Position of the commission
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConGroup.CommissionShift(
       pos,        # Position of the commission
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of a commission in the list, starting with 0.

**shift**  
[in] Shift of a commission relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
