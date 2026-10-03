[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTDailyArray::Delete

Delete an object of a daily report by its position.

C++
    
    
    MTAPIRES  IMTDailyArray::Delete(
       const UINT  pos      // Position of a daily report
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Delete(
       uint        pos      // Position of a daily report
       )

### Parameters

**pos**  
[in] Position of a daily report in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTDaily::Release](../IMTDaily/Release.md) method.
