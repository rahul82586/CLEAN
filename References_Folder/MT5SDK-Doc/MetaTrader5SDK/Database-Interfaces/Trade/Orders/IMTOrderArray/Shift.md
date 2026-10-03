[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTOrderArray::Shift

Change the position of an order in an array.

C++
    
    
    MTAPIRES  IMTOrderArray::Shift(
       const UINT  pos,       // Position of an order
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Shift(
       uint        pos,       // Position of an order
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of an order in an array, starting with 0.

**shift**  
[in] Shift of an oder relative to its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
