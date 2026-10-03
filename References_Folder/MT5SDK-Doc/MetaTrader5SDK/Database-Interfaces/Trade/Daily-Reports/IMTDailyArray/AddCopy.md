[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTDailyArray::AddCopy

Add a copy of the daily report object at the end of an array.

C++
    
    
    MTAPIRES  IMTDailyArray::AddCopy(
       const IMTDaily*  daily      // The daily report that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.AddCopy(
       CIMTDaily        daily      // The daily report that is being added
       )

### Parameters

**daily**  
[in] An object of the daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the daily object and places it at the end of the array.

Unlike [IMTDailyArray::Add(IMTDaily* daily)](Add.md), calling this method does not set any additional conditions for the control of the daily object, but is more resource-intensive, since an additional object is created.

# IMTDailyArray::AddCopy

Add copies of the objects of daily report in an array.

C++
    
    
    MTAPIRES  IMTDailyArray::AddCopy(
       const IMTDailyArray*  array      // An array of daily reports that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.AddCopy(
       CIMTDailyArray        array      // An array of daily reports that is being added
       )

### Parameters

**array**  
[in] An object of the array of daily reports.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the objects of daily reports belonging to the array object, and inserts them at the end of the current array.
