[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTPositionArray::Shift

Shift a trade position in an array.

C++
    
    
    MTAPIRES  IMTPositionArray::Shift(
       const UINT  pos,       // Place of a trade position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCod  CIMTPositionArray.Shift(
       uint        pos,       // Place of a trade position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] The index of a trade position in an wrray, starting with 0.

**shift**  
[in] Shift a trade position relative to its current place. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
