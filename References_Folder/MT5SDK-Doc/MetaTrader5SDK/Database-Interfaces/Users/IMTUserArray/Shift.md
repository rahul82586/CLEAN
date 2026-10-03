[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTUserArray::Shift

Change the position of a client record in an array.

C++
    
    
    MTAPIRES  IMTUserArray::Shift(
       const UINT  pos,       // The position of a client record
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.Shift(
       uint        pos,       // The position of a client record
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

**shift**  
[in] Shift of the client record relative to its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
