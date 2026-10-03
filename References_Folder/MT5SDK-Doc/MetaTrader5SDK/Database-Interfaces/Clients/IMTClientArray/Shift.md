[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTClientArray::Shift

Change the position of a client in an array.

C++
    
    
    MTAPIRES  IMTClientArray::Shift(
       const UINT  pos,       // Client position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Shift(
       uint        pos,       // Client position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the client in an array, starting with 0.

**shift**  
[in] Shift of the client relative to the current position. A negative value means shift towards the array beginning, a positive value means shift towards its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
