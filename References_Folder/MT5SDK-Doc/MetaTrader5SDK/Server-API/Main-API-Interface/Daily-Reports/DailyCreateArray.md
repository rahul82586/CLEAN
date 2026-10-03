[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailyCreateArray

[Previous](DailyCreate.md) | [Next](DailySubscribe.md)

# IMTServerAPI::DailyCreateArray

Create an object of the array of daily reports.
    
    
    IMTDailyArray*  IMTServerAPI::DailyCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTConDailyArray](../../../Database-Interfaces/Trade/Daily-Reports/IMTDailyArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDaily::Release](../../../Database-Interfaces/Trade/Daily-Reports/IMTDailyArray/Release.md) method of this object.
