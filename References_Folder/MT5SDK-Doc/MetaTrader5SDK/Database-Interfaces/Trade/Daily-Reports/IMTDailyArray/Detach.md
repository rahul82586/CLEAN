[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTDailyArray::Detach

Detach an object of a daily report from an array.

C++
    
    
    IMTDaily*  IMTDailyArray::Detach(
       const UINT  pos      // Position of a daily report
       )

.NET (Gateway/Manager API)
    
    
    CIMTDaily  CIMTDailyArray.Detach(
       uint        pos      // Position of a daily report
       )

### Parameters

**pos**  
[in] Position of a daily report in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of the daily report.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
