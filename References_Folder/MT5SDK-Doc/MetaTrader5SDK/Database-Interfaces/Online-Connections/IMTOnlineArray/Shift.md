[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTOnlineArray::Shift

Change the position of a connection record in an array.

C++
    
    
    MTAPIRES  IMTOnlineArray::Shift(
       const UINT  pos,       // Connection record position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Shift(
       uint        pos,       // Connection record position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a connection record in an array, starting with 0.

**shift**  
[in] Shift the connection record relative to its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
