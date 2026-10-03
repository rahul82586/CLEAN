[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTDailyArray::Update

Change a daily report at the specified position of an array.

C++
    
    
    MTAPIRES  IMTDailyArray::Update(
       const UINT  pos,       // Position
       IMTDaily*   daily      // An object of a daily report
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Update(
       uint        pos,       // Position
       CIMTDaily   daily      // An object of a daily report
       )

### Parameters

**pos**  
[in] Position of a daily report in an array, starting with 0.

**daily**  
[in] An object of the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTDailyArray::Update method deletes the previous element (call of [IMTDaily::Release](../IMTDaily/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTDailyArray::Release), an earlier inserted object will be automatically removed.

### Example
    
    
    //--- Example
       IMTDailyArray *array =api->DailyCreateArray();   
       IMTDaily      *daily1=api->DailyCreate();
       IMTDaily      *daily2=api->DailyCreate();
    //---
       array->Add(daily1);
       array->Update(0,daily2); // The first element (object daily1) is replaced by daily2
       //--- After that the daily1 element will be released using Release, and the daily2 lifetime will be controlled by the array
