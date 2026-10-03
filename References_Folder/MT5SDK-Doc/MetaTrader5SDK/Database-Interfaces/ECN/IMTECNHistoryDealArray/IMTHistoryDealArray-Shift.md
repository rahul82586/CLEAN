[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Shift

[Previous](IMTHistoryDealArray-UpdateCopy.md) | [Next](IMTHistoryDealArray-Total.md)

# IMTECNHistoryDealArray::Shift

Change the position of a deal in an array.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Shift(
       const UINT  pos,       // deal position
       const int   shift      // shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.Shift(
       uint        pos,       // deal position
       int         shift      // shift
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

**shift**  
[in] Shift deal relative to its current position. A negative value means shift towards the array beginning, while a positive value means shift towards its end.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
