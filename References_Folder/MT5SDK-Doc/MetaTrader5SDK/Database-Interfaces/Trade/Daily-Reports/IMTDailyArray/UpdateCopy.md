[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTDailyArray::UpdateCopy

Change a daily report at the specified position of an array by copying the parameters of a passed object of a daily report.

C++
    
    
    MTAPIRES  IMTDailyArray::UpdateCopy(
       const UINT        pos,       // Position
       const IMTDaily*   daily      // An object of a daily report
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.UpdateCopy(
       uint              pos,       // Position
       CIMTDaily         daily      // An object of a daily report
       )

### Parameters

**pos**  
[in] Position of a daily report in an array, starting with 0.

**order**  
[in] An object of the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the daily object into an object of a daily report at the specified position of an array.
