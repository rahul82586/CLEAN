[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Shift

[Previous](Requests-UpdateCopy.md) | [Next](Requests-Total.md)

# IMTRequestArray::Shift

Change the position of a trade request in an array.

C++
    
    
    MTAPIRES  IMTRequestArray::Shift(
       const UINT  pos,       // Request position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.Shift(
       uint        pos,       // Request position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a trade request in an array, starting with 0.

**shift**  
[in] Shift a trade request relative to its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
