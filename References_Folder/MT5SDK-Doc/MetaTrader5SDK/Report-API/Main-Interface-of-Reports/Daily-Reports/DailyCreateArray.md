[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Daily Reports](../Daily-Reports.md) / DailyCreateArray

[Previous](DailyCreate.md) | [Next](DailyGet.md)

# IMTReportAPI::DailyCreateArray

Create an object of the array of daily reports.
    
    
    IMTDailyArray*  IMTReportAPI::DailyCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTConDailyArray](../../../Database-Interfaces/Trade/Daily-Reports/IMTDailyArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDailyArray::Release](../../../Database-Interfaces/Trade/Daily-Reports/IMTDailyArray/Release.md) method of this object.
