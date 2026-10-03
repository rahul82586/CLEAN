[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayUpdate

[Previous](HolidayUnsubscribe.md) | [Next](HolidayUpdateBatch.md)

# IMTAdminAPI::HolidayUpdate

Add or update a holiday configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::HolidayUpdate(
       IMTConHoliday*  config      // Holiday configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HolidayUpdate(
       CIMTConHoliday  config      // Holiday configuration object
       )

Python
    
    
    AdminAPI.HolidayUpdate(
       holiday         # Holiday configuration object
       )

### Parameters

**config**  
[in] An object of a holiday configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. The key fields for comparison are the date ([IMTConHoliday::Year](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Year.md), [IMTConHoliday::Month](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Month.md), [IMTConHoliday::Day](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Day.md)), time ([IMTConHoliday::WorkFrom](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/WorkFrom.md), [IMTConHoliday::WorkTo](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/WorkTo.md)) and description ([IMTConHoliday::Description](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Description.md)). When you try to add a completely identical record, no changes are made, and therefore the [IMTConHolidaySink::OnHolidayUpdate](../../../../Configuration-Interfaces/Holidays/IMTConHolidaySink/OnHolidayUpdate.md) notification method is not called.
