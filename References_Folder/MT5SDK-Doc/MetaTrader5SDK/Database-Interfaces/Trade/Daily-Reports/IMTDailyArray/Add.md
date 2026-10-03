[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTDailyArray::Add

Add an object of the daily report at the end of an array.

C++
    
    
    MTAPIRES  IMTDailyArray::Add(
       IMTDaily*  daily      // An object of a daily report
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Add(
       CIMTDaily  daily      // An object of a daily report
       )

### Parameters

**daily**  
[in] An object of the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the daily object is passed to the array object. Thus, when deleting an array object (call of [IMTDailyArray::Release](Release.md)), an earlier inserted object will be automatically removed.

# IMTDailyArray::Add

Add an object of the array of daily reports at the end of an array.

C++
    
    
    MTAPIRES  IMTDailyArray::Add(
       IMTDailyArray*  array      // An array of daily reports that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Add(
       CIMTDailyArray  array      // An array of daily reports that is being added
       )

### Parameters

**array**  
[in] An object of the array of daily reports.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTDailyArray *array=api->DailyCreateArray();   
       IMTDaily      *daily=api->DailyCreate();
    //---
       array->Add(daily);   // After that the lifetime is controlled by the array
       array->Delete(0);    // Delete the first element, and the pointer in daily becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTDailyArray  *array=api->DailyCreateArray();   
       IMTDaily       *daily=api->DailyCreate();
    //---
       array->Add(daily);
       array->Add(daily); // In this case the array contains two pointers to the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
