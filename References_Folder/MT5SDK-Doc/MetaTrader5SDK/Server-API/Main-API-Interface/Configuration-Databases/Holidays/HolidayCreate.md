[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayCreate

[Previous](../Holidays.md) | [Next](HolidaySubscribe.md)

# IMTServerAPI::HolidayCreate

Create an object of the configuration of holidays.
    
    
    IMTConHoliday*  IMTServerAPI::HolidayCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConHoliday](../../../../Configuration-Interfaces/Holidays/IMTConHoliday.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConHoliday::Release](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Release.md) method of this object.
