[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / PositionShift

[Previous](PositionClear.md) | [Next](PositionTotal.md)

# IMTDaily::PositionShift

Move a [trade position](../../Positions.md) in the list.

C++
    
    
    MTAPIRES  IMTDaily::PositionShift(
       const UINT  pos,       // Position in the list
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.PositionShift(
       uint        pos,       // Position in the list
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a trade position, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
