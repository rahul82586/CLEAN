[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayAdd

[Previous](HolidayUnsubscribe.md) | [Next](HolidayDelete.md)

# IMTServerAPI::HolidayAdd

Add or update a holiday configuration.
    
    
    MTAPIRES  IMTServerAPI::HolidayAdd(
       IMTConHoliday*  config      // Holiday configuration object
       )

### Parameters

**config**  
[in] An object of a holiday configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. The key fields for comparison are the date ([IMTConHoliday::Year](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Year.md), [IMTConHoliday::Month](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Month.md), [IMTConHoliday::Day](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Day.md)), time ([IMTConHoliday::WorkFrom](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/WorkFrom.md), [IMTConHoliday::WorkTo](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/WorkTo.md)) and description ([IMTConHoliday::Description](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Description.md)). When you try to add a completely identical record, no changes are made, and therefore the [IMTConHolidaySink::OnHolidayUpdate](../../../../Configuration-Interfaces/Holidays/IMTConHolidaySink/OnHolidayUpdate.md) notification method is not called.
