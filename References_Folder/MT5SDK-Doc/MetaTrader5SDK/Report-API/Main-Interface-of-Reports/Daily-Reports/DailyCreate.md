[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Daily Reports](../Daily-Reports.md) / DailyCreate

[Previous](../Daily-Reports.md) | [Next](DailyCreateArray.md)

# IMTReportAPI::DailyCreate

Create an object of a daily report.
    
    
    IMTDaily*  IMTReportAPI::DailyCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDaily](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDaily::Release](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Release.md) method of this object.
