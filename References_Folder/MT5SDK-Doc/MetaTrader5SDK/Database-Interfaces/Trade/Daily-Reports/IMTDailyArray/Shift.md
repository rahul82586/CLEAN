[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTDailyArray::Shift

Change the position of a daily report in an array.

C++
    
    
    MTAPIRES  IMTDailyArray::Shift(
       const UINT  pos,       // Position of a daily report
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Shift(
       uint        pos,       // Position of a daily report
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a daily report in an array, starting with 0.

**shift**  
[in] Shift the daily report relative to its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
