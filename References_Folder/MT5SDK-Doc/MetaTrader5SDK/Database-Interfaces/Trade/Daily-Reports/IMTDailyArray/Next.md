[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTDailyArray::Next

Get an object of a daily report by its position.

C++
    
    
    IMTDaily*  IMTDailyArray::Next(
       const UINT  index      // Position of a daily report
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTDaily  CIMTDailyArray.Next(
       uint        index      // Position of a daily report
       )

### Parameters

**index**  
[in] Position of a daily report in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the object of a daily report at the specified position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
