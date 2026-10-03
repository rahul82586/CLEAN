[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderShift

[Previous](OrderClear.md) | [Next](OrderTotal.md)

# IMTDaily::OrderShift

Move a [trade order](../../Orders.md) in the list.

C++
    
    
    MTAPIRES  IMTDaily::OrderShift(
       const UINT  pos,       // Position in the list
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderShift(
       uint        pos,       // Position in the list
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] The position of a trade order in the list, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
