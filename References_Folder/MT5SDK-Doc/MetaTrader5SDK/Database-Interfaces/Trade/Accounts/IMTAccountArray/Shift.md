[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTAccountArray::Shift

Changes the position of a trading account in an array.

C++
    
    
    MTAPIRES  IMTAccountArray::Shift(
       const UINT  pos,       // Trade account position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Shift(
       uint        pos,       // Trade account position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the trading account in an array, starting with 0.

**shift**  
[in] Shift of a trade account relative to its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
